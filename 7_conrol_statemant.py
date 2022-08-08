# simple if stetment 
var = 10
if(var==10):
    print("the value of variable is 10 ")
# if else 
a = int(input(" enter the valu of a "))# take a value  of user 
b = int(input(" enter the valu of b "))
if(a>b):
    print(" a ia greater ")
elif(a<b):
    print("b is greater ") 
#que print a persanage 
p = int (input("enter your persantage : "))
if(p>= 85  and p<=100 ):
    print("you persantage is vary good  you are in a+ grade \n")
elif(p>= 70 and p<=84):
    print("your persantage is good you are in a grade\n ") 
elif(p>= 50 and p<69):
    print(" you are in b grade \n")  
else:
    print("you are fale ")
    # nestade if statement 
age  = int (input(" enter your age  : ")) 
weight = int (input("enter your weight : "))
if age>=18 :
    weight = int (input("enter your weight : "))
    if weight>=50 :
        print("you are eligibal for blood donate ")
    else:
        print("under weight ")
else:
    print(" undetr age ")