n = input("Enter number: ")
n = int(n)
d1= n % 10
d2= n % 100 // 10
d3= n % 1000// 100
d4= n % 10000// 1000
d5= n % 100000// 10000
print("Result:",d1+d2+d3+d4+d5)
