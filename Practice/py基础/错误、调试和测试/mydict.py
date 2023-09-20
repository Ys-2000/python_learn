class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


# 这是一个自定义的Dict类，它继承了内置的dict类，并重写了__getattr__和__setattr__方法，实现了类似字典的行为。
# Dict类继承了内置的dict类，因此它拥有字典的所有方法和特性。
# Dict类的__init__方法用于初始化对象。它接受任意数量的关键字参数kw，并将这些参数传递给父类的__init__方法，这样在创建Dict对象时可以直接传递键值对来初始化字典。
# __getattr__方法用于获取属性。当访问Dict对象的属性时，如果属性不存在，就会调用__getattr__方法。在这里，它的实现是通过字典的键值对来获取属性的值。如果属性不存在于字典中，就会抛出AttributeError异常，提示对象没有该属性。
# __setattr__方法用于设置属性。当给Dict对象的属性赋值时，就会调用__setattr__方法。在这里，它的实现是将属性和对应的值添加到字典中。