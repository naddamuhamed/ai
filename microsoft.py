
import itertools


def changetohex(s):
    return int(s,base=16)
    
def xorstr(str1,str2):
    a = changetohex(str1)
    b = changetohex(str2)
    return hex(a ^ b)

def solution(A):    
    l=[]
    for pair in itertools.combinations(A,2):
        if xorstr(*pair)==hex(4369) or xorstr(*pair)==hex(273) or xorstr(*pair)==hex(69905) or xorstr(*pair)==hex(1118481) or xorstr(*pair)==hex(17895697):
            l.append(str(pair))
    return l
      

# x=["1001", "0011", "1001", "11011", "0110"]
x=["11011", "1010", "00100", "110", "1110", "0111"]
print(solution(x))


