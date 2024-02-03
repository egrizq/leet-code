'''
Program to check if a number is a prime number!

prime number is a number that divisible by 1 and itself
example of prime number: 2,3,5,7,89,91

the calculation behind prime number are factors!
2 -> 1,2
3 -> 1,3
5 -> 1,5

number which are NOT prime number is
6 -> 1,2,3,6
10 -> 1,2,5,10
12 -> 1,2,3,4,6,12

'''

def primeNumber(number):
    prime = True # define a flag variable 
        
    if number == 1:
        return print(number, "not")
    elif number > 1:
        # check for factors
        # this looping will check if any other number in range 2 to n, who are divisible is 0
        for i in range(2, number):
            if number%i == 0:
                # if number is divide by i is 0 the it is NOT prime
                prime = False
                break
    
        if prime:
            return print(number, "prime number")
        else:
            return print(number, "not")
         
for n in range(89): 
    primeNumber(n)