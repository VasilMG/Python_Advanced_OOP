
class cache:
    def __init__(self, func):
        
        self.func = func
        self.cache = {}

    def __call__(self, *args, **kwargs):
        
        self.__ensure_value_in_cache(*args, **kwargs)
        key = self.__build_key(*args, **kwargs)
        return self.cache[key]

    def __ensure_value_in_cache(self, *args, **kwargs):
        key = self.__build_key(*args, **kwargs)
        if key not in self.cache:
            self.cache[key] = self.func(*args, **kwargs)

    def __build_key(self, *args, **kwargs):
        return args + tuple(kwargs.items())


