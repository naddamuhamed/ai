
# QUESTION 1

# hours = int(input("input hours: "))
# ratehour = int(input("input rate/hour: "))
# if hours>40:
#     pay=int((40*ratehour)+((hours-40)*ratehour*1.5))
# else:
#     pay=int(40*ratehour)
# print("gross pay is: ",pay)    


# QUESTION 2

# def piglatin(w):
#     if len(w)==1:
#         print("word not valid\n")
#     else:
#         print(w[1:]+w[0]+'ay')    
# word=input("enter a word in english: ")
# print("pig latin for the word is: "); piglatin(word)



# QUESTION 3



# for i in range(5):
#     for j in range(i):
#         print('*',end="")
#     print('') 


# for i in range(5,0,-1):
#     for j in range(i):
#         print('*',end="")
#     print('')           



# QUESTION 4


# def div(x):
#     d=[]
#     for i in range(1,x):
#         if x%i==0 and i!=1:
#             d.append(i)
#     if len(d)==0:
#         print("no divisors")
#     else:
#         print(d)


# no=int(input("enter a number: "))
# print("divisors are: ")
# div(no)


# QUSTION 5


def rev(x):
    s=-(len(x)+1)
    str=''
    for i in range(-1,s,-1):
        str+=x[i]
    return str


x=input("enter any number to see it in reverse: ")
print("your number in reverse is: ",rev(x))



    