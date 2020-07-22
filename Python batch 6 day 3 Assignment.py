#!/usr/bin/env python
# coding: utf-8

# # sum of N number using while loop

# In[1]:


sum = 0 
value = 1
print ("enter the number ")
num = int (input())

print("you have entered " ,  num )

while value <= num :
        sum = sum +value
        value = value + 1
        print("at step " , value -1 , "sum is" , sum )
    
print("final sum of " , num , "is" , sum)


# # Check whether number is prime or not

# In[4]:


print("enter the number")
value =int(input(""))


if value > 1 :

    for no in range(2, value) :
        if (value % no) == 0 :
            print("The number" ,value, "is not a Prime no .")
            break 
    else :
        print("The number" , value , "is a Prime no ." )
        


# In[ ]:




