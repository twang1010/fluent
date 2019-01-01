import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    ori_writer = sys.stdout.write

    def reverse_write(text):
        ori_writer(text[::-1])

    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = ori_writer