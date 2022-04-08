#!/usr/bin/env python
# coding: utf-8

# # Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the parent 
# class and function to calculate the area should be defined in subclass

# In[7]:


class side:
    def __init__(self,a,b,c):
        self.a=float(a)
        self.b=float(b)
        self.c=float(c)
        self.area = 0
    
class triangle(side):
    def triangle_area(self,a,b,c):
        side.__init__(self,a,b,c)
    
    def calculate_area(self):
        s=(self.a+self.b+self.c)/2
        self.area=float((s*(s-self.a)*(s-self.b)*(s-self.c)) )**0.5
    def show_area(self):
        return self.area
a, b, c = input("a = "), input("b = "), input("c = ")
    
t=triangle(a,b,c)
t.calculate_area()
print("area: {}".format(t.show_area()))


# # Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

# In[23]:


def filterlong_words(lst, n):
    return list(filter(lambda ele: len(ele) > n, lst))


test = ["Akankshya", "nayak", "priyansi", "oops", "hi", "hole", "o"]
filterlong_words(test, 3)
    


# # Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words.
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.
# 

# In[38]:


listofwords = input('List of Word: ').split() 
listofints = []
 
for i in range(len(listofwords)):
    listofints.append(len(listofwords[i]))
     
print ("List of wordlength:"+str(listofints))


# # Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise

# In[24]:


def if_vowel(char):
    vowel = ["a", "e", "i", "o", "u"]
    if len(char) > 1:
        print("Please enter only one character")
    elif char in vowel:
        return True
    else:
        return False


char = input("Enter a character :")
new_char = char.lower()
print("Is {} a vowel?: ".format(char),if_vowel(new_char))

