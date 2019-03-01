import re
import sys


def is_jpg(b: bytes) -> bool:
    """バイナリの先頭部分からJPEGファイルかどうかを判定する。"""
    return bool(re.match(br"\xff\xd8", b[:2]))


def is_png(b: bytes) -> bool:
    """バイナリの先頭部分からPNGファイルかどうかを判定する。"""
    return bool(re.match(br"^\x89\x50\x4e\x47\x0d\x0a\x1a\x0a", b[:8]))


def main():
    checkers = (is_jpg, is_png)
    data = sys.stdin.buffer.read()
    return any(checker(data) for checker in checkers)


if __name__ == '__main__':
    if main():
        sys.exit('Input data is valid image data.')
    else:
        sys.exit('Input data is invalid image data.')
