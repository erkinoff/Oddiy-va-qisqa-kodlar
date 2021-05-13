"""
@author: Murodjon
"""

'''Dars'''
n = input()
a = len(n)
s1 = ''
s2 = ''
for i in range(a):
    if n[i]==' ':
        s1 = int(n[:i])
        s2 = int(n[i+1:])
print(s1*s2)