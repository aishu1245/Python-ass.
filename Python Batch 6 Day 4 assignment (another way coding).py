#!/usr/bin/env python
# coding: utf-8

# # assignment day 4
# 

# 1.Find the occurance of substring in a string

# In[10]:


string=  " letsupgrade is a good platformm to learn ; i am learning python with letsupgrade and enjoying the sessions "
substring="letsupgrade"

string.count("letsupgrade")
print("substring occurs :" , +string.count("letsupgrade"), "times")


# In[11]:


string.index("letsupgrade")
lst=[ string.index("letsupgrade") , string.rindex("letsupgrade")]
print("substring occurse at positions : " ,lst)


# In[2]:


#another way : 

test_str = "we are learning python , we are programmers"
test_sub = "we"

print("The original string is : " + test_str)
res = [i for i in range(len(test_str)) if test_str.startswith(test_sub, i)] 

print("The start indices of the substrings are : " + str(res)) 


# In[ ]:


#2.How to use : islower() and isupper() with differnt strings


# In[3]:


a= "i am learning python"
a.islower()


# In[22]:


a= "I am learning python , batch 6"
a.islower()


# In[4]:


a= "I am learning python"
a.islower()


# In[5]:


a= "# i am learning python"
a.islower()


# In[6]:


a= "#I am learning python"
a.islower()


# In[7]:


a= "123456"
a.islower()


# In[8]:


a= "@$#@$"
a.islower()


# In[9]:


a= "2345 @#%"
a.islower()


# In[10]:


a= "I am learning python"
a.isupper()


# In[11]:


a= "i am learning python"
a.isupper()


# In[13]:


a= "I AM LEARNING PYTHON"
a.isupper()


# In[14]:


a= "I AM LEARNING PYTHON IN BATCH 6"
a.isupper()


# In[15]:


a= "I AM LEARNING PYTHON IN BATCH #6"
a.isupper()


# In[16]:


a= "I am learning python  6"
a.isupper()


# In[17]:


a= "123456"
a.isupper()


# In[18]:


a= "@#$%$"
a.isupper()


# In[19]:


a= " 2345 @#$%$"
a.isupper()


# In[20]:


a= "END"
a.isupper()


# In[ ]:




