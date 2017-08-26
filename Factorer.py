# factorer program finds all factors of a given number or tells you that it is prime
# by Jeremy Gleeson
import time

print ("**Welcome to the factorer**\n\n")
number = int ( input ("Enter a number to factor\n:"))
while number <=1:
    number = int ( input ("Please enter a positive integer\n:"))
start = time.clock()
initialNumber = number

factors = []
# prime list needed to check future primes
primeList = []

currentPrime = 2

# checks numbers such that largest possible prime factor squared is smaller than number
while number >= currentPrime**2:
    isPrime = 1
    for i in primeList:
        # checks if number is prime
        if i**2 > currentPrime:
            break
        if currentPrime%i == 0:
            # number isn't prime, stop checking it and exit loop
            isPrime = 0
            break
    if isPrime == 1:
        # add prime to prime list
        primeList.append(currentPrime)
        # check if number is a factor and add to factors list and adjust number accordingly
        while number%currentPrime == 0:
            factors.append(currentPrime)
            number = number/currentPrime
    currentPrime += 1


# print output below based on a variety of factors
if number == 1:
    print ("\n\nYour number, {0}, has the following factors:".format(initialNumber))
    for i in factors:
        print (i)
else:
    if number != initialNumber:
        print ("\n\nYour number, {0}, has the following factors".format(initialNumber))
        for i in factors:
            print (i)
        print (int(number))
    else:
        print("Your number, {0}, is prime".format(int(number)))
'''
print ("\nPrimelist:")
for i in primeList:
    print (i)
'''
end = time.clock()
print ("Start: {0}\nEnd: {1}\nTotal: {2}".format(start, end, end-start))