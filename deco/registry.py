# for fast access, replace list with set
registry = set()


def register(active=True):
    def decorate1(func):
        print('running register (active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate1


@register()
def f1():
    print('running f1()')


@register(active=False)
def f2():
    print('running f2()')

@register()
def f3():
    print('running f3()')


def f4():
    print('running f4()')


def main():
    print('running main()')
    print('registry->', registry)
    f1()
    f2()
    f3()
    print('again registry->', registry)

    #register f4()
    register()(f4)
    print('again registry->', registry)

    #de-register f4()
    register(active=False)(f4)
    print('again registry->', registry)

if __name__ == '__main__':
    main()
