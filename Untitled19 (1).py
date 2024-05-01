#!/usr/bin/env python
# coding: utf-8

# In[35]:


s='13 23 33 45'.split()
s1=0
for x in s:
    if x[len(x)-1]=='3':
        s1=s1+int(x)
        
print(s1)


# In[ ]:




