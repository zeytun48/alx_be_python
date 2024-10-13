# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"  # Class attribute

    @staticmethod
    def add(a, b):
        return a + b  # Static method to add two numbers

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")  # Access class attribute
        return a * b  # Class method to multiply two numbers

