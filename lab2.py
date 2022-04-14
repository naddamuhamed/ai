

# QUESTION 1

def perfect(n):
    l=[]
    for i in range(1,n):
        if(n%i==0):
            l.append(i)

    sum=0
    for i in range(len(l)):
        sum+=l[i]
    if sum==n:
        print("perfect")
    else:
        print("not perfect")

# x=int(input("enter a number"))
# perfect(x)


# QUESTION 2

def sepsort(s,l):
    x=l.split(s)
    sl=x.sort()
    for i in range(len(x)):
        if i==len(x)-1:
            print(x[i], end="")
        else:
            print(x[i]+'-',end="")


# sep=input("enter separator: ")
# seq=input("enter sequence: ")
# sepsort(sep,seq)


# QUESTION 3

def unique(l):
    u=[]
    for i in range(len(l)):
        if l[i] not in u:
            u.append(l[i])
    return u

# l=list(input("enter list: "))
# u=unique(l)
# print(u)


# QUESTION 4

def sublist(l,s):
    sub=True
    for i in range(len(s)):
        if s[i] not in l:
            sub=False
    return sub

# l=list(input("enter list: "))
# subl=list(input("enter sublist: "))
# s=sublist(l,subl)
# if s:
#     print(subl,end=""); print(" is a sublist of ",end=""); print(l)
# lse:
#    print(subl,end=""); print(" is not a sublist of ",end=""); print(l)


# QUESTION 5


# x = (1,2,3,4)
# y = (3,5,2,1)
# z = (2,2,3,1)
# print("Original lists:")
# print(x)
# print(y)
# print(z)
# print("\nlement-wise sum of the said tuples:")
# result = tuple(map(sum, zip(x, y, z)))
# print(result)


# QUESTION 6

def listuple(t):
    result = [list(l) for l in t]
    return result



# t = [(1,2), (2,3), (3,4)]
# print("Original list of tuples:")
# print(t)
# print("Convert the said list of tuples to a list of lists:")
# print(listuple(t))
# t = [(1,2), (2,3,5), (3,4), (2,3,4,2)]
# print("\nOriginal list of tuples:")
# print(t)
# print("Convert the said list of tuples to a list of lists:")
# print(listuple(t))


# QUESTION 7

def maxmin(dic):
    mx=0
    mn=0
    for i in dic:
        mx=max(i,mx)    
        mn=min(i,mn)     
    return mx,mn            
    

# dic = {
# 					1 : 'dfgd',
# 					2 : 'fdgdf',
# 					3 : 'erge',
# 					4 : 'erger'
# 					}
# mx,mn=maxmin(dic)
# print("dict= ",end=""); print(dic)
# print("max key is: ",end=""); print(mx); print("min key is: ",end=""); print(mn)


# QUESTION 8

dic = {
					3 : 'dfgd',
					6 : 'fdgdf',
					7 : 'erge',
					1 : 'erger'
					}
x=dic.keys()
# s=x.sort()
d={}
for i in sorted(dic):
    d[i]=dic.get(i)
print("dict: ",end=""); print(dic); print("sorted dict: ",end=""); print(d)   


# QUESTION 9

def shortest(dic):
    min_value=1
    result = [k for k, v in dic.items() if len(v) == (min_value)] 
    return result    

dic = {
 'V': [10, 12],
 'VI': [10],
 'VII': [10, 20, 30, 40],
 'VIII': [20],
 'IX': [10,30,50,70],
 'X': [80]
 }

print("\nOriginal Dictionary:")
print(dic)
print("\nShortest list of values with the keys of the said dictionary:")
print(shortest(dic))






					


