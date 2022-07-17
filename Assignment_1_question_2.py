"""
Write a Python program that accepts a word from the user and reverse it.
"""

word=input("enter a word ")
rev_word=""
for i in word:
    rev_word=i + rev_word
print("reverse word :",rev_word)


#Blow code show error , can't we none type to any other type? it is not automatically type casted?
"""
word=input("enter a word ")
rev_word=None
for i in word:
    rev_word=i + rev_word
print("reverse word :",rev_word)
"""