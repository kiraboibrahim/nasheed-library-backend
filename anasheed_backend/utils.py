from .settings import MAX_RESULTS_PER_PAGE
from django.http  import StreamingHttpResponse
import re
import os

def paginated_results(page, queryset):
    if  page is not None:
        # Donot accept a page <= 0 because the offset will be negative
        page = int(page)
        if page <= 0:
            page = 1
        offset = (page - 1) * MAX_RESULTS_PER_PAGE
        end = offset + MAX_RESULTS_PER_PAGE
        # Add the number of songs each artist has
        return queryset[offset:end]
    else:
        # Return all the data without pagination
        return queryset

# The code below has benn obtained from https://github.com/broadinstitute/seqr

def file_iter(file_path, byte_range=None):
    with open(file_path, "rb") as f:
        if byte_range:
            f.seek(byte_range[0])
            for line in f:
                # file cursor position should be less than the last byte requested, else break
                if f.tell() < byte_range[1]:
                    yield line
                else:
                    break
        else:
            for line in f:
                yield line


def stream_file(request, file):
    #content_type = 'application/octet-stream'
    content_type = 'audio/mpeg'
    range_header = request.META.get('HTTP_RANGE', None)
    file_size = os.path.getsize(file)
    if range_header:
        range_match = re.compile(r'bytes\s*=\s*(\d+)\s*-\s*(\d*)', re.I).match(range_header)
        first_byte, last_byte = range_match.groups()
        first_byte = int(first_byte) if first_byte else 0
        # if last byte is not specified, then the last byte of file is considered
        last_byte = int(last_byte) if last_byte else file_size
        length = last_byte - first_byte + 1
        resp = StreamingHttpResponse(
            file_iter(file, byte_range=(first_byte, last_byte)), status=206, content_type=content_type)
        resp['Content-Length'] = str(length)
        resp['Content-Range'] = 'bytes %s-%s' % (first_byte, last_byte)
    else:
        resp = StreamingHttpResponse(file_iter(file), content_type=content_type)
    resp['Accept-Ranges'] = 'bytes'
    return resp
