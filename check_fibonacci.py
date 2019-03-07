#################################################################FIBONACCI SERIES #############################################


#check if first element of the list is in fibonacci series
#call function check_fibonacci to check if the rest part of the series follow fibonacci series

# List to check if it is a part of Fibonacci series: p
p = [8, 13, 21, 35]
#p = [1, 1, 2, 3, 5]

#initialization of fibonacci series
k = [0, 1]

i = 2

# check if the rest part of list follow fibonnaci series
def check_fibonacci(p):
    for i in range(2, len(p)):
        if p[i] == p[i-1] + p[i-2] and i == len(p) - 1:
            print("fibonacci series")
            
        elif p[i] == p[i-1] + p[i-2]:
            continue
        else:
            print("not a part of fibonacci")
            break
        
        

#check if first element of the list is in fibonacci series
while p[0] >= k[i-1]:
    if p[0] == k[0] and p[1] == k[1]:
        check_fibonacci(p)
        break
        
    elif p[0] == k[1] and p[1] == p[0] + k[0]:
        check_fibonacci(p)
        break
        
    else:
        #generate subsequent elements of fibonacci series
        j = k[i-1] + k[i-2]
        
        k[i-2] = k[i-1]
        k[i-1] = j
        
        if p[0] < j:
            print("not a part of fibonacci")
            break

