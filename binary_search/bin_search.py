def binary_search(given_arr,key):
    low=0
    high=len(given_arr)-1
    mid = 0
    
    while low <= high:
        mid = (high+low) // 2
        if given_arr[mid] < key:
           low=mid+1
        elif given_arr[mid]> key:
            high=mid-1
        else: 
           return mid  
    return -1

given_arr=[]
n=int(input("Enter the number of elements in your array : "))
for i in range (0,n):
    element = int(input())
    given_arr.append(element)
       
print ("Enterend Elements are :  ",given_arr)
key = int(input("Enter the number to get its index "))
key_found = binary_search(given_arr,key)

if key_found!=-1:
 print(" you got that  element at index ", str(key_found))
else:
 print("figure out")