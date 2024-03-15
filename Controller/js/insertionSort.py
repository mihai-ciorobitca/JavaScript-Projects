t=[27,10,12,8,11]
print(t)

def insert(k, i):
    while i>=0 and t[i]<k:
        t[i+1]=t[i]
        i=i-1

def insertFunction(j):
    i=j-1
    k=t[j]
    insert(k, i)
    t[i+1]=k

def main():
    for j in range(1, len(t)):
        insertFunction(j)
    print(t)

main()