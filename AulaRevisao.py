class A():
    def __init__(self,a,b):
        self.a = a
        self.b = b

class B(A):
    def __init__(self,a,b,c):
        A.__init__(self,a,b)
        self.c = c


x = B(1,2,3)
