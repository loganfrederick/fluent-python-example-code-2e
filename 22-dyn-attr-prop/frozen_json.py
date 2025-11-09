from collections import abc
"""
What collecionts.abc does

collections.abc provides abstract base classes (ABCs) for collection types. 
They define interfaces for collections, 
so you can check if an object implements a collection protocol rather 
than checking a specific concrete type.

Why use ABC?

Flexibility: Works with any type that implements the interface, not just built-ins.
Duck typing: Checks behavior, not exact type.
Future-proof: Works with custom types that implement the protocol.
"""

class FrozenJSON:
    """ A read only facade for navigating a JSON object
    using attribute notation
    """

    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        try:
            return getattr(self.__data, name)
        except AttributeError:
            return FrozenJSON.build(self.__data[name])
        
    def __dir__(self):
        return self.__data.keys()
    
    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj

