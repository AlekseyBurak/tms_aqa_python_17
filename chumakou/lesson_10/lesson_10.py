class MyClass_1:
    def too(self):
        print("foo")

class MyClass_2:
    def foo(self):
        print("bar")

class Cat(MyClass_1, MyClass_2):
    def baz(self):
        self.foo()

cat = Cat()
cat.baz()