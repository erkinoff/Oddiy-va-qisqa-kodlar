"""
@author: Murodjon
"""

'''Sonning xonalarini yig'indisini hisoblash'''
def yigindi(n):
    s = 0
    a = len(n)
    for i in range(a):
        s+=int(n[i])
    print(s)
n = input()
yigindi(n)