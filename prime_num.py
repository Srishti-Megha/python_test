############## Check if number is a prime number and print Prime Number in the range (1, 100) #########################


# number to check for prime number: num
num = 81


#### short code ########
if all(num % j != 0 for j in range(2, num)):
    print(num, "is a prime number")
    
else:
    print(num, "is not a prime number")


############# long Code ###########
# Check if number is a prime number
for i in range(2, num):
#    print(i)
    if num % i == 0:
        print(num, "is not a prime number")
        break
       
    elif i == num-1: 
        print(num, "is a prime number")
    
    else:
        continue
    
        

    
# Print Prime Number in the range (1, 100)
    
l = [i for i in range(1, 100) if all(i % j != 0 for j in range(2, i) )]

print(l)
#print([i for i in range(1, 100) if all(i % j != 0 for j in range(2, i) )])



