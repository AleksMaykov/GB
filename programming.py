number = list (input('Введите целое число: '))

sort_list = sorted(number)
print (*sort_list)
a = 0
for el in sort_list:
    if el == '0':
       a +=1
sort_list[0],sort_list[a] = sort_list[a],sort_list[0]


#
#
# print(number)3
#
print(*sort_list)