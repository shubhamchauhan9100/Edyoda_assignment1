"""
Write a Python program to count the number of even and odd numbers from a series of numbers.
"""
#Take input from used, untill user write stop
numbers=[]
while True:
    element=input("enter the element or type stop to stop input: ")
    if(element=="stop" or element=="Stop"):
        break
    numbers.append(int(element))

#counter & loop to count even & odd numbers
even_count=odd_count=0
for i in numbers:
    if (i%2==0):
        even_count+=1
    else:
        odd_count+=1

# print even and odd count
print("Even count:",even_count)
print("Odd count:", odd_count)
    