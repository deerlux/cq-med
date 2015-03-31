def singleton(cls, *args, **kw):
    '''function to decorate a class to single instance.'''
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

