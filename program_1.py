"""
Implement a class that represent complex number in form of abstract data type. 
Implement the following operations: addition, multiplication 

Hint : Use the @property 

"""

class ComplexNumber:
    def _init_(self, real, imaginary):
        self._real = real
        self._imaginary = imaginary

    @property
    def real(self):
        return self._real
    
    @real.setter
    def real(self, value):
        self._real = value
        
    @real.deleter
    def real(self):
        del self._real

    @property
    def imaginary(self):
        return self._imaginary
    
    @imaginary.setter
    def imaginary(self, value):
        self._imaginary = value

    @imaginary.deleter
    def imaginary(self):
        del self._imaginary


def add_complex_numbers(*args):
    real = 0
    imaginary = 0
    for i in args:
        real += i.real
        imaginary += i.imaginary
    return ComplexNumber(real, imaginary)

def multiply_complex_numbers(*args):
    real = 1
    imaginary = 1
    for i in args:
        real *= i.real
        imaginary *= i.imaginary
    return ComplexNumber(real, imaginary)

