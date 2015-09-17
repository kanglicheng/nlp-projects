import os

class lazy_property(object):
    """Meant to be used for lazy evaluation of an object attribute.
    property should represent non-mutable data, as it replaces itself.

    http://stackoverflow.com/questions/3012421/python-lazy-property-decorator"""

    def __init__(self,fget):
        self.fget = fget
        self.func_name = fget.__name__


    def __get__(self,obj,cls):
        if obj is None:
            return None
        value = self.fget(obj)
        setattr(obj,self.func_name,value)
        return value


def get_text_files(directory):
    nested_files = [w[2] for w in os.walk(directory)]
    files = sum(nested_files, [])
    return [f for f in files if f.endswith('.txt')]
