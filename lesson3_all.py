import os

# print(list(map(lambda x: x*x, [2, 5, 12, -2])))

path = 'c:\\1'
file_name = 'info.txt'
path = os.path.join(path, file_name)
#catalods = os.listdir(path)
print(path)
#print(catalods)
with open(path, 'r', encoding='UTF-8') as file:
    print(file.read())

