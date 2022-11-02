import sys

n = int(sys.stdin.readline().split()[0])

tasks = [[0 for x in range(3)] for y in range(n)]

row=0

for line in sys.stdin:
    column = 0
    for word in line.split():
        tasks(row)[column]=int(word)
        column += 1
    row +=1
    
print(tasks)