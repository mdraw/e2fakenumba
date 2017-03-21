import warnings
import functools

class guvectorize(object):  # see elektronn2.utils.DecoratorBase
    def __init__(self, *args, **kwargs):
        warnings.warn('Using fake version of numba.guvectorize. This should only be used for sphinx builds and destroys actual functionality!')
        self.func = None
        self.dec_args = None
        self.dec_kwargs = None
        if len(args)==1 and not len(kwargs):
            assert hasattr(args[0], '__call__')
            func = args[0]
            self.func = func
            self.__call__.__func__.__name__ = func.__name__
        else:
            self.dec_args = args
            self.dec_kwargs = kwargs

    def __call__(self, *args, **kwargs):
        if not self.func is None:
            ret = self.func(*args, **kwargs)
            return ret
        elif len(args)==1 and not len(kwargs):
            assert hasattr(args[0], '__call__')
            func = args[0]

            @functools.wraps(func)
            def decorated(*args0, **kwargs0):
                ret = func(*args0, **kwargs0)
                return ret
            return decorated
        else:
            raise ValueError()
