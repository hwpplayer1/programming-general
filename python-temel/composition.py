class A:
    pass

class B:
    def __init__(self):
        self.a = A()
        pass

b = B()
print(b)
