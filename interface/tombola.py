import abc

class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        '''
        load element from iterable collections to this object
        '''

    @abc.abstractmethod
    def pick(self):
        '''
        return an elemenet when called, throw LookupError when there is no element
        '''

    def loaded(self, elem):
        ''' return trueis there is at lest one element, otherwise false'''
        return bool(self.inspect())

    def inspect(self):
        '''inspect the elements in the obj, return a tuple of the elems'''
        elems = []
        while True:
            try:
                elems.append(self.pick())
            except LookupError:
                break
        self.load(elems)
        return tuple(sorted(elems))


class Fake(Tombola):
    def pick(self):
        return 23


f = Fake()
