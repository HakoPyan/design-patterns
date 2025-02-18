# YAGNI = You ain't gonna need it
import threading


# Non-pythonic way
class ClassicSingleton:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def get_instance(cls):
        # Optimization technique: Lazy instantiation - you often find you don't need to do the creation at all
        if not cls._instance:
            cls._instance = cls.__new__(cls)

        return cls._instance


# s1 = ClassicSingleton.get_instance()
# s2 = ClassicSingleton.get_instance()
# print(s1 is s2)


# Pythonic way
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


# s1 = Singleton()
# s2 = Singleton()
# print(s1 is s2)


# Metaclass way
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonByMetaclass(metaclass=SingletonMeta):
    pass


class SingletonTwoByMetaclass(metaclass=SingletonMeta):
    pass


# s1 = SingletonByMetaclass()
# s2 = SingletonTwoByMetaclass()
# s3 = SingletonTwoByMetaclass()
# print(s1 is not s2)
# print(s2 is s3)


# Metaclass: Eager version
class EagerSingletonMeta(type):
    _instances = {}

    def __init__(cls, *args, **kwargs):
        # __init__ of metaclass is being called when the class is defined, not initialized!
        super().__init__(*args, **kwargs)
        cls._instances[cls] = super().__call__()

    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]


class EagerSingleton(metaclass=EagerSingletonMeta):
    pass


# s1 = EagerSingleton()
# s2 = EagerSingleton()
# print(s1 is s2)


# Thread-safe
# We should make possible only 1 thread to access the critical section
class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class ThreadSafeSingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]


class SingletonWithThreadSafeMeta(metaclass=ThreadSafeSingletonMeta):
    pass
