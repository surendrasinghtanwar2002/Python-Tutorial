                                            ## In this section we will practise MRO Concepts in Python ##

class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    def greet(self):
        return "Hello from C"


class D(B,C):           ## D Inheriting from B and C
    pass

##Creating the instance of Class D
obj = D()
print(obj.greet())
print(D.__mro__)
