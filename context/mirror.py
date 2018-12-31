class LookingGlass:
    def __enter__(self):
        import sys
        self.orig_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.orig_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.orig_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True