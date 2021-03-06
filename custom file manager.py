import tkinter as tk
import os
from tkinter import filedialog
from tkinter import messagebox as mb

win = tk.Tk()

icon = tk.PhotoImage(file='icon.png')
win.iconphoto(False, icon)
win.title('custom file manager v0.1 beta')
# win.geometry('305x280')
win.geometry('465x600')
win.resizable(False, False)

filename = str()


def open_dir():
    """диалоговое окно для выбора папки
    так же подтягивает путь директорию в первое поле ввода"""

    filename = filedialog.askdirectory()
    entry_1.insert(0, filename)
    return str(filename)

def show_error_warning():
    mb.showwarning("Предупреждение", 'Системе не удается найти указанный путь')

def get_entry_filename():
    """получает директорию из поля entry_1"""
    entry_value = entry_1.get()
    return entry_value

def dir_delaem_delo():
    dir_result = os.listdir(path=get_entry_filename())
    dir_result = dir_result[::-1]
    if os.path.isdir(get_entry_filename()) == True:
        for i in range(len(dir_result)):
            print(dir_result[i], '\n')
            field_1.insert(1.0, (dir_result[i]+'\n'))
    else:
        msg = "Неверно указан путь"
        mb.showwarning("Предупреждение", msg)


def close_window():
    """закрывает окно"""
    win.destroy()

def about_soft():
    """информационное окно"""
    mb.showinfo(
        title="О Программе",
        message='Версия 0.1 beta'
                '\n  '
                '\nИсходный код: https://github.com/Delovem/fogstream-custom-file-manager'
                '\n  '
                '\nДанная программа является учебным проектом и разработана в рамках обучения в компании Forgstream на курсе "Основы Python Сентябрь" в 2021 году'
                '\n  '
                '\nCopyright (c) Delovem software 2021-2022')


label_1 = tk.Label(text='Выберите папку').grid(row=0, column=0)
label_2 = tk.Label(text='Вывести каталог').grid(row=1, column=0)
label_3 = tk.Label(text='Вывод: ').grid(row=2, column=0)

entry_1 = tk.Entry()
entry_1.grid(row=0, column=1, stick='we')

# entry_2 = tk.Entry()
# entry_2.grid(row=1, column=1)

button_1 = tk.Button(text='...', command=open_dir).grid(row=0, column=2, stick='we')
button_2 = tk.Button(text='Готово', command=dir_delaem_delo).grid(row=1, column=1, columnspan=2, stick='we')
button_3 = tk.Button(text='О программе', command=about_soft).grid(row=4, column=0, stick='we')
button_4 = tk.Button(text='Закрыть', command=close_window).grid(row=4, column=1, columnspan=2, stick='we')

field_1 = tk.Text(win, height=30, width=55, wrap='word')
field_1.grid(row=3, column=0, columnspan=3)

scroller_1 = tk.Scrollbar(win, command=field_1.yview)
scroller_1.grid(row=2, column=3, rowspan=2, columnspan=2, stick='ns')

win.mainloop()
