from abc import ABC, abstractmethod


class IPerson(ABC):
    @staticmethod
    @abstractmethod
    def person_method():
        pass

class Person(IPerson):
    @staticmethod
    def person_method():
        print("I am a person")

class ProxyPerson(IPerson):
    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("I am the proxy functionality")
        self.person.person_method()