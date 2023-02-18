#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1.What are the two values of the Boolean data type? How do you write them?

Ans : True and false We usr Bool keyword.


# In[ ]:


# 2. What are the three different types of Boolean operators?
Ans: And ,Or ,Not 


# In[ ]:


# 3. Make a list of each Boolean operator&#39;s truth tables (i.e. every possible combination of Boolean
 values for the operator and what it evaluate ).
    
Ans : OR                    AND                      NOT 
     
    A    B     A+B=C     A    B     A*B=C          A    B      
    
    0    0      0       0     0      0            0     1
    0    1      1       0     1      0            1     0 
    1    0      1       1     0      1
    1    1      1       1     1      1
    
Note : Here 1 = True and 0 = False
    
    


# In[ ]:


# 4. What are the values of the following expressions?
(5>4) and (3 == 5)
Ans : Flase (0)
not (5>4)
Ans : Flase (0)
(5>4) or (3 == 5)
Ans : True (1)
not ((5>4) or (3 == 5))
Ans : Flase (0)
(True and True) and (True == False)
Ans : Flase (0)
(not False) or (not True)
Ans :True 


# In[ ]:


get_ipython().set_next_input('5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')

Ans : >,<,>=,<=,!=,==


# In[ ]:


6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.

Ans:
    Assigment  (=) operator is use to assigenr value to the variable 
    Equal(==) operator is use to compare to values 
    


# In[ ]:


7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')

Ans:  ham ,spam,spam


# In[6]:


# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
# Greetings! if anything else is stored in spam
spam = 0
if spam==1:
    print("Hello")
if spam ==2:
    print("Hoedy")
else:
    print("Greetings")
    

    


# 9.If your programme is stuck in an endless loop, what keys you’ll press?
# 
# Ans :CTRL + C 

# In[ ]:


get_ipython().set_next_input('10.How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')

Ans : Break statment is used to terminate the specific conditaion and stop that particulat itertation
    Continue statment is used to skip particular itertation 
    


# In[ ]:


11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

Ans : range (10) = range from 0 to 9
      range(0, 10)=  range from 0 to 9
      range(0, 10, 1) = range from 0 to 9 with step 1


# In[ ]:


# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
 # program that prints the numbers 1 to 10 using a while loop.
    
# for loop                      
i=1                          
for i in range (0,11):       
    print(i)                   
                            


# In[ ]:


# while loop
   
i=1
while i<=10:
   print(i)
   i=+1


# In[ ]:


13.If you had a function named bacon() inside a module named spam, how would you call it after
get_ipython().set_next_input('importing spam');get_ipython().run_line_magic('pinfo', 'spam')
 Ans : The function can be caller spam.bacon()

