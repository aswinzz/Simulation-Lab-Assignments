import time
import random 

# Chi Square Table Provided
table = [
    [1.73,0.995],
    [2.09,0.99],
    [3.33,0.95],
    [4.17,0.90],
    [5.90,0.75],
    [8.34,0.50],
    [11.4,0.25],
    [14.7,0.10],
    [16.9,0.05],
    [21.7,0.01],
    [23.6,0.005]
]

# Function For Chi Square Test
def chisqTest(result):
    # Initializing Frequence Array for 10 Classes
    frequency = [0,0,0,0,0,0,0,0,0,0]
    # Setting Frequencies according to the provided list of numbers
    for item in result:
        if(item<100):
            frequency[0] += 1
        elif(item<200):
            frequency[1] += 1
        elif(item<300):
            frequency[2] += 1
        elif(item<400):
            frequency[3] += 1
        elif(item<500):
            frequency[4] += 1
        elif(item<600):
            frequency[5] += 1
        elif(item<700):
            frequency[6] += 1
        elif(item<800):
            frequency[7] += 1
        elif(item<900):
            frequency[8] += 1
        elif(item<1000):
            frequency[9] += 1

    print("Frequency Obtained : "+str(frequency))
    # Calculating Chi Square Value
    omine = []
    chisq = 0
    for i in range(10):
        ans = ((frequency[i]-100)*(frequency[i]-100))/100
        chisq += ans
        omine.append(ans)

    print("(O - E) * (O - E) / E : "+str(omine))
    print("ChiSquare Value : "+str(chisq))

    # Finding Probability Using Chi Square Table
    prob=0.995
    for item in table:
        if(chisq>=item[0]):
            prob=item[1]
        else:
            break
    print("Probability from matching the given Chi Square Table : "+str(prob))


# X(i+1) = (a*X(i) + c) % m

# Mixed Congruence Method

class Mixed:
    def __init__(self):
        self.a = 48271
        self.m = 2147483647
        self.c = 1

    def generate(self,n):
        seed = (time.time()*1000)
        result = []
        for i in range(n):
            seed = ((self.a * seed) + self.c) % self.m
            result.append(seed%1000)
        return result

# Additive Congruence Method
class Additive:
    def __init__(self):
        self.m = 2147483647

    def generate(self,n):
        increment = 1928
        seed = (time.time()*1000)
        result = []
        for i in range(n):
            seed = (seed + increment) % self.m
            result.append(seed%1000)
        # print(result)
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
        seed = (time.time()*1000)
        for i in range(n):
            seed = (seed * self.a) % self.m
            result.append(seed%1000)
        return result

# Inbuilt random number function
class InBuilt:

    def generate(self,n):
        result = []
        for i in range(n):
            number = random.randint(0,1000)
            result.append(number%1000)
        return result

# using Multiplicative Congruence
print("\nMultiplicative")
mult = Multiplicative()
result = mult.gen(1000)
chisqTest(result)

# using Additive Congruence
print("\nAdditive")
additive = Additive()
result = additive.generate(1000)
chisqTest(result)

# using Mixed Congruence
print("\nMixed")
mixed = Mixed()
result = mixed.generate(1000)
chisqTest(result)

# using Inbuilt generator function
print("\nInBuilt")
inbuilt = InBuilt()
result = inbuilt.generate(1000)
chisqTest(result)
            