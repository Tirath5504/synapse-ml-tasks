""" Task 1.2 """

lst = ["0001", "0011", "0101", "1010", "1011"]

new_lst = []

for l in lst:
    new_lst.append(int(l, base=2))

if len(new_lst) % 2 == 0:
    length = len(new_lst) // 2
else:
    length = (len(new_lst) // 2) + 1
    
for i in range(length):
    ele1 = new_lst[0]
    ele2 = new_lst[len(new_lst) - 1 - i]
    new_lst.remove(ele1)
    new_lst.remove(ele2)
    new_lst.append(ele1 + ele2)

print(new_lst)