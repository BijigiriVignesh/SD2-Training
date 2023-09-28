class Siva:
    def c1(ho):
        print("i am c1")
    def c2(ho):
        print("i am c2")
class Baby1(Siva):
    def d1(ho):
        print("i am d1")
class Baby2(Siva):
    def i(ho):
        print("method i")
class Gbaby(Baby1):
    def m(ho):
        print("i am m")
a=Baby2()
a.c1()
a.c2()
a.i()
b=Gbaby()
b.c1()
b.c2()
b.d1()
b.m()