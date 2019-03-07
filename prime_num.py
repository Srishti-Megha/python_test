############## Check if given number is a prime number.
############## Print Prime Number in the range (1, 100) #########################


# number to check for prime number: num
num = 81


#### check if num is a prime number ########
if all(num % j != 0 for j in range(2, num)):
    print(num, "is a prime number")
    
else:
    print(num, "is not a prime number")


    
# Print Prime Number in the range (1, 100)
print([i for i in range(1, 100) if all(i % j != 0 for j in range(2, i) )])




