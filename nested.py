"""22/11/2024"""
rows=int(input("Enter number of rows: "))
print("Increasing Triangle")
for i in range(1,rows+1):
    for j in range(i):
        print("*",end="\t")
    print()
print("Decreasing Triangle")
for i in range(rows,0,-1):
    for j in range(i):
        print("*",end="\t")
    print()
print("Hill Triangle")
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ", end="\t")
    for k in range(2*i-1):
        print("*",end="\t")
    print()
print("Reverse Hill Triangle")
for i in range(rows,0,-1):
    for j in range(rows-i):
        print(" ", end="\t")
    for k in range(2*i-1):
        print("*",end="\t")
    print()


