"""
@author: Murodjon
"""

'''Kiritilgan sonni RIM raqamlarida ifodalash'''
a=[(1000,'M'),(900,"CM"),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,"L"),(40,'XL'),(10,"X"),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
def rim(n):
    s=''
    while n>0:
        for i,r in a:
            while n>=i:
                s+=r
                n-=i
    print(s)
n=int(input("n ni kiriting "))
rim(n)