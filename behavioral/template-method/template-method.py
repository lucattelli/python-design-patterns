# https://refactoring.guru/design-patterns/template-method/python/example

from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def template_method(self) -> None:
        print("AbstractClass.template_method")
        self.base_operation1()
        self.base_operation2()
        self.required_operation1()
        self.required_operation2()
    
    def base_operation1(self) -> None:
        print("AbstractClass.base_operation1")

    def base_operation2(self) -> None:
        print("AbstractClass.base_operation2")

    @abstractmethod
    def required_operation1(self) -> None:
        pass
    
    @abstractmethod
    def required_operation2(self) -> None:
        pass

class ConcreteClass1(AbstractClass):

    def required_operation1(self) -> None:
        print("ConcreteClass1.required_operation1")
    
    def required_operation2(self) -> None:
        print("ConcreteClass1.required_operation2")

def client_code(abstract_class: AbstractClass) -> None:

    abstract_class.template_method()

client_code(ConcreteClass1())