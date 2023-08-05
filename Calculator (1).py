#!/usr/bin/env python
# coding: utf-8

# In[14]:


def Calc(x,y,op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "/":
        while y == 0:
            print("you can't devide by zero")
            y=int(input("enter a new number\n"))
        return x / y
    elif op == "*":
        return x * y
    else:
        print("you entered wrong operator")
    


# In[15]:


Calc(10,0,"/")


# In[ ]:





# In[ ]:




