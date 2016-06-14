def A():
    yield 1
    yield 2
    print('A')
    yield 4
    b = yield 5

# надуманный пример
def B():
    state = 0
    while True:
        a = yield state
        print(a)
        state = raw_input()

if __name__ == "__main__":
    b = A()
    for a in A():
        print(a)
        # b.__next__()
    # b.send(1)

    # надуманный пример
    b = B()
    while True:
        h = b.send(cmd or "Start")
        cmd = engine.calculate(in)
