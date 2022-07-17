"""
Write a Python program to get the Fibonacci series between 0 to 50
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
"""

#initail no. of fabonacci series
last_no=1
second_last_no=0
next_no=last_no

#loop to ask for valid range from user untill , a valid range is given
while True:
    lower_limit,upper_limit=int(input("Enter range between which need to print fibonacci series")),int(input())
    if(lower_limit >upper_limit):
        upper_limit,lower_limit=lower_limit,upper_limit
    if( lower_limit<0):
        print("Invalid lower range")
    else:
        break

# To check some specil case of upper & lower limit
if(lower_limit==upper_limit or upper_limit==1):
    print("no value")

#loop to print fibonacci series which is in the range
while next_no<upper_limit:
    if( next_no>lower_limit):
        print(next_no,end=" ")
    next_no= last_no + second_last_no
    second_last_no=last_no
    last_no=next_no
    