
for i in range(1, 6):
 print(str(i) * i)

 
for i in range(1, 6):
 for j in range(65, 65+i):
    print(chr(j), end=" ")
 print()

for i in range(5, 0, -1):
 print("*" * i)