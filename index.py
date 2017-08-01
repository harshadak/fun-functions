# Odd/Even:

def odd_even():
    for i in range(1, 2001):
        
        if i % 2 == 0:
            print "Number is {}. This is an even number.". format(i)
        else:
            print "Number is {}. This is an odd number.". format(i)

odd_even()


# Multiply:

def multiply(arr,num):
    for x in range(len(arr)):
        print arr[x]     
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b


# Multiply:

#def multiply(arr, num):
#    for i in arr:
#        arr[i] = arr[i] * num
#        print arr
#    return arr
#    
#
#    
#    
#b = multiply([2,4,10,16], 5)
#print b


# Hacker Challenge:

def layered_multiples(arr):
    # your code here
    new_array = []
    
    for i in arr:
        temp_array = []
        for j in range(0,i):
            temp_array.append(1)
        new_array.append(temp_array)
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x


# [6, 12, 15]