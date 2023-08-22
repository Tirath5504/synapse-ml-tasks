""" Task 1.2 """

lst = ["0001", "0011", "0101", "1011", "1101", "1111"]

new_lst = []

for l in lst:
    new_lst.append(int(l, base=2))

length = len(new_lst) - 2
    
for i in range(length):

    ele1 = new_lst[0]
    ele2 = new_lst[1]

    new_lst.append(ele1 + ele2)

    new_lst = sorted(new_lst[2:])

print(new_lst)