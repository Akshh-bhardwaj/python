from abc import ABC, abstractmethod

# ----------------------------------------------------
# 1. Method Resolution Order (MRO)
# ----------------------------------------------------
print("--- 1. MRO and C3 Linearization ---")

class Base:
    def greet(self):
        print("Base greeting")

class A(Base):
    def greet(self):
        print("A greeting")
        super().greet()

class B(Base):
    def greet(self):
        print("B greeting")
        super().greet()

class C(A, B):
    def greet(self):
        print("C greeting")
        super().greet()

# Instantiating C and calling greet
c = C()
c.greet()
print("MRO of C:", [cls.__name__ for cls in C.__mro__])
print()


# ----------------------------------------------------
# 2. Custom Metaclass
# ----------------------------------------------------
print("--- 2. Custom Metaclass validation ---")

class LowercaseMethodsMeta(type):
    def __new__(mcs, name, bases, attrs):
        # We check if any method/attribute name has uppercase characters
        for key in attrs:
            if not key.startswith("__") and any(c.isupper() for c in key):
                raise TypeError(f"Attribute or method '{key}' must not contain uppercase characters.")
        return super().__new__(mcs, name, bases, attrs)

# This class compiles fine
class SafeClass(metaclass=LowercaseMethodsMeta):
    def hello_world(self):
        return "safe"

print("SafeClass created successfully.")

try:
    # This class will raise a TypeError during definition/import
    class UnsafeClass(metaclass=LowercaseMethodsMeta):
        def badMethod(self):
            pass
except TypeError as e:
    print(f"Intercepted expected error: {e}")
print()


# ----------------------------------------------------
# 3. Descriptor Protocol
# ----------------------------------------------------
print("--- 3. Descriptors (Attribute validation) ---")

class RangeValidationDescriptor:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
        self.name = None  # Will be set dynamically by __set_name__ in modern Python

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Value for {self.name} must be numeric.")
        if not (self.min_val <= value <= self.max_val):
            raise ValueError(f"Value {value} for {self.name} must be between {self.min_val} and {self.max_val}.")
        instance.__dict__[self.name] = value

class Product:
    # Set the range descriptor rules
    price = RangeValidationDescriptor(10, 1000)
    rating = RangeValidationDescriptor(1, 5)

    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

prod = Product("Smart Watch", 150, 4.5)
print(f"Product: {prod.name}, Price: {prod.price}, Rating: {prod.rating}")

try:
    prod.price = 5000  # Raises ValueError
except ValueError as e:
    print(f"Intercepted validation error: {e}")
print()


# ----------------------------------------------------
# 4. Abstract Base Classes (ABCs)
# ----------------------------------------------------
print("--- 4. Abstract Base Classes ---")

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started: Vroom!")

    def stop_engine(self):
        print("Car engine stopped.")

car = Car()
car.start_engine()
car.stop_engine()

try:
    # Attempting to instantiate ABC directly (will fail)
    v = Vehicle()
except TypeError as e:
    print(f"Intercepted abstract instantiation error: {e}")
