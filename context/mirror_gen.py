import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    ori_writer = sys.stdout.write

    def reverse_write(text):
        ori_writer(text[::-1])

    sys.stdout.write = reverse_write
    msg=''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please NO NOT divide by zero!'
    finally:
        sys.stdout.write = ori_writer
        if msg:
            print(msg)