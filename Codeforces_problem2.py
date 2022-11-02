#версия 1
# import sys
# №разобраться со строчкой ниже
# n = int(sys.stdin.readline().split()[0])


# words=[]

# for line in sys.stdin:
#     for word in line.split():
#         words.append(word)
# for word in words:
#     if len(word)>10:
#         print(word[0]+str(len(word)-2)+word[-1])
#     else:
#         print(word)
  

#версия 1
n = input()

print(n)

words=[]

for line in n:
    for word in line.split():
        words.append(word)
for word in words:
    if len(word)>10:
        print(word[0]+str(len(word)-2)+word[-1])
    else:
        print(word)