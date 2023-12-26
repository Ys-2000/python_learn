class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name} with bases {bases} and attributes {dct}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    my_attr = 123
    def my_method(self):
        pass
