# for fast access, replace list with set
registry = set()


def register(active=True):
    def decorate(func):
        print('running register (active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate


@register()
def f1():
    print('running f1()')


@register(active=False)
def f2():
    print('running f2()')

@register()
def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry->', registry)
    f1()
    f2()
    f3()
    print('again gregistry->', registry)


if __name__ == '__main__':
    main()
