n = int(input())
for i in range(0,n):
    for j in range(i,n):
        print(" ",end="")
    for k in range(0,i+1):
        print("x " ,end="")
    print()

# #Ans
# # Simple Python program to print the simple reversed right angle pyramid pattern    
# rows = int(input("Enter the number of rows:"))   
# # Here, we are declaring the integer variable to store the input rows   
# k = 2 * rows - 2     # Here, the K is used for number of spaces    
# # Here, we are declaring an outer loop to handle number of rows  
# for i in range(0, rows):    
#       # Here, we are declaring an inner loop to handle number of spaces  
#     for j in range(0, k):    
#         print(end=" ")    
#     k = k - 2      # Here, we are decrementing the k value after each iteration    
# # Here, we are declaring an for loop to handle number of rows      
# for j in range(0, i + 1):    
#         print("* ", end="")   # Here, we are printing the star pattern    
#     print("")    