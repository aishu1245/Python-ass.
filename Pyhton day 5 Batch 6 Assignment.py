#!/usr/bin/env python
# coding: utf-8

# # Assignment day 5 Batch 6 

# # Assignment 1
# 
# - [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
# - sort increasing order but all zeros should be at right hand side .
# - use fuction
# 

# In[45]:



def fun1(x):
    a = [0 for i in range(x.count(0))]
    lst = [ i for i in x if i != 0]
    lst.extend(a)
    return(lst)

print(fun1([0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]))


# # Assignment 2
# -  list1] = [10,20,40,70,80] 
# -  list2= [5 ,15,25,35,45,60] 
# - without sort method ,merge these 2 list produce one sorted list .

# In[ ]:





# In[12]:



list1 = [10,20,40,70,80] 
list2 = [5 ,15,25,35,45,60] 
   
print ("The original list 1 is : " + str(list1)) 
print ("The original list 2 is : " + str(list2)) 
length1 = len(list1) 
length2 = len(list2) 
  
result = [] 
i, j = 0, 0
  
while i < length1 and j < length2: 
    if list1[i] < list2[j]: 
      result.append(list1[i]) 
      i += 1
  
    else: 
      result.append(list2[j]) 
      j += 1
  
result = result + list1[i:] + list2[j:] 
print ("The sorted list is : " + str(result)) 

