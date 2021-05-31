import os
import re
import mimetypes
from wsgiref.util import FileWrapper

from django.http.response import StreamingHttpResponse
from django.utils import timezone
from rest_framework import exceptions

from cinema import settings
from movies.models import MovieSubscription

range_re = re.compile(r'bytes\s*=\s*(\d+)\s*-\s*(\d*)', re.I)


def check_subscription(user, movie):
    movie_in_subscription = MovieSubscription.objects.filter(movies=movie)
    if user.is_anonymous and movie.subscriptions.exists():
        return 'Please register subscription for watching this movie'
    if not movie_in_subscription.exists():
        return True
    user_subscription = movie_in_subscription.filter(users=user, movies=movie)
    if not user_subscription.exists():
        raise exceptions.ValidationError('Please register subscription for watching this movie')
    user_subscription: MovieSubscription = movie_in_subscription.first()
    if user_subscription.subscription_users.get(user=user, subscription=user_subscription).time_end < timezone.now():
        raise exceptions.ValidationError('Your subscription ended, please subscribe again to watch this movie')
    return True


class RangeFileWrapper(object):
    def __init__(self, filelike, blksize=8192, offset=0, length=None):
        self.filelike = filelike
        self.filelike.seek(offset, os.SEEK_SET)
        self.remaining = length
        self.blksize = blksize

    def close(self):
        if hasattr(self.filelike, 'close'):
            self.filelike.close()

    def __iter__(self):
        return self

    def __next__(self):
        if self.remaining is None:
            # If remaining is None, we're reading the entire file.
            data = self.filelike.read(self.blksize)
            if data:
                return data
            raise StopIteration()
        else:
            if self.remaining <= 0:
                raise StopIteration()
            data = self.filelike.read(min(self.remaining, self.blksize))
            if not data:
                raise StopIteration()
            self.remaining -= len(data)
            return data


def stream_video(request, path):
    range_header = request.META.get('HTTP_RANGE', '').strip()
    range_match = range_re.match(range_header)
    path = os.path.join(settings.MEDIA_ROOT, path)
    try:
        size = os.path.getsize(path)
    except FileNotFoundError:
        raise exceptions.NotFound('File not found')
    content_type, encoding = mimetypes.guess_type(path)
    content_type = content_type or 'application/octet-stream'
    if range_match:
        first_byte, last_byte = range_match.groups()
        first_byte = int(first_byte) if first_byte else 0
        last_byte = int(last_byte) if last_byte else size - 1
        if last_byte >= size:
            last_byte = size - 1
        length = last_byte - first_byte + 1
        response = StreamingHttpResponse(RangeFileWrapper(open(path, 'rb'), offset=first_byte, length=length), status=206, content_type=content_type)
        response['Content-Length'] = str(length)
        response['Content-Range'] = 'bytes %s-%s/%s' % (first_byte, last_byte, size)
    else:
        response = StreamingHttpResponse(FileWrapper(open(path, 'rb')), content_type=content_type)
        response['Content-Length'] = str(size)
    response['Accept-Ranges'] = 'bytes'
    return response
