import time

# X(i+1) = (a*X(i) + c) % m

# Mixed Congruence Method
class Mixed:
    def __init__(self):
        self.a = 48271
        self.m = 2147483647
        self.c = 1

    def generate(self,n):
        # seed will be a unique number in each iteration by using current time in micro seconds
        seed = (time.time()*1000)
        result = []
        # Generating N numbers
        for i in range(n):
            seed = ((self.a * seed) + self.c) % self.m
            result.append(seed)
        return result

# Additive Congruence Method
class Additive:
    def __init__(self):
        self.m = 2147483647

    def generate(self,n):
        increment = 1
        # seed will be a unique number in each iteration by using current time in micro seconds
        seed = (time.time()*1000)
        result = []
        # Generating N numbers
        for i in range(n):
            seed = (seed + increment) % self.m
            result.append(seed)
        return result

# Multiplicative Congruence Method
class Multiplicative:
    def __init__(self):
        self.a = 48271
        self.m = 2147483647
        self.q = 44488
        self.r = 3399

    def gen(self,n):
        result = []
        # seed will be a unique number in each iteration by using current time in micro seconds
        seed = (time.time()*1000)
        # Generating N numbers
        for i in range(n):
            seed = (seed * self.a) % self.m
            result.append(seed)
        return result

# number of random numbers to be generated
n = int(input())

# using Multiplicative Congruence
print("\nMultiplicative")
mult = Multiplicative()
print(mult.gen(n))

# using Additive Congruence
print("\nAdditive")
additive = Additive()
print(additive.generate(n))

# using Mixed Congruence
print("\nMixed")
mixed = Mixed()
print(mixed.generate(n))
            