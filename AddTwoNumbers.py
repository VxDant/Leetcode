l1 = [9,9,9,9,9,9,9]
l2= [9,9,9,9]
lis = []
str1 = ''
str2 = ''

# I have to code using linked list and not type list


for n in range(len(l1)):
    str1 += str(l1[n])

for n in range(len(l2)):
    str2 += str(l2[n])

str1 = str1[::-1]
str2 = str2[::-1]


print(str1)
print(str2)

sum = int(str1) + int(str2)

print(sum)

for i in str(sum)[::-1]:
    lis.append(int(i))

print(lis)