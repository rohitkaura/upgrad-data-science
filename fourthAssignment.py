#!/usr/bin/env python
# coding: utf-8

# In[ ]:


myUniqueList = []
x = input()
def addList(x):
    if x in myUniqueList:
        return False
    else:
        myUniqueList.append(x)
        return True
myUniqueList.append("rohit")
addList(x)

print(myUniqueList)


# In[ ]:




