import tkinter, os

PATH = 'nums'
SIZE = 4


main_window = tkinter.Tk()

# label_1 = tkinter.Label (main_window, text = 'Hello World')
# # label_1.grid(row = 0, column = 0)
# label_1.grid()

files_list = os.listdir(PATH)

# print(files_list)

files_list_with_path = []

for file in files_list:
    # files_list_with_path.append(PATH + '/' + file)
    files_list_with_path.append(os.path.join(PATH, file))

# print(*files_list_with_path)

images_list = []

for file_path in files_list_with_path:
    image = tkinter.PhotoImage(file = file_path)
    images_list.append(image)

labels_list = []

for _x, image in enumerate (images_list):
    _i = _x //SIZE
    _j = _x % SIZE
    label = tkinter.Label(main_window, image = image)
    label.grid(row = _i, column = _j)
    label.x = _x
    label.row = _i
    label.column = _j
    labels_list.append(label)


curr = labels_list[-1]

def key_press(arg):
    print(arg)

main_window.bind('<Right>', lambda e: key_press('r'))

main_window.mainloop()