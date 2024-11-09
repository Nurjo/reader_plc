from tkinter import *
import tkinter as tk
from pathway import pathway_func


def hmi_popup_func():
    # Создаем главное окно
    root = tk.Tk()
    root.title("Login")

    label5 = tk.Label(root, text='Put your credentials', font=('Arial', 14, 'bold'))
    label5.pack(pady=15, padx=10)

    label3 = tk.Label(root, text="Login:", font=('Arial', 14))
    label3.pack(pady=0, padx=10)

    entry1 = tk.Entry(root, width=10)
    entry1.pack(pady=0, padx=10)

    label4 = tk.Label(root, text="Password:", font=('Arial', 14))
    label4.pack(pady=0, padx=10)

    entry2 = tk.Entry(root, width=10, show="*")
    entry2.pack(pady=0, padx=10)

    # Checkbox section
    label5 = tk.Label(root, text='Choose the data you want to get', font=('Arial', 14, 'bold'))
    label5.pack(pady=10, padx=10)

    checkbox_labels = ["Date and time", "Device name", "Device description", "Firmware",
                       "Main task usage", "Serial number", "Current project"]
    checkbox_vars = {}
    checkbox_result = list(range(len(checkbox_labels)))

    for j in checkbox_labels:
        var = tk.BooleanVar(value=False)
        checkbox = tk.Checkbutton(root, text=j, variable=var)
        checkbox.pack(anchor="w")
        checkbox_vars[j] = var

    def show_selections():
        # Сохранение значений перед закрытием окна
        credentials = [str(entry1.get()), str(entry2.get())]
        for i, (label, var) in enumerate(checkbox_vars.items()):
            checkbox_result[i] = var.get()
            print(i, label, var.get())
            print(checkbox_result[i])
        root.quit()  # Остановить основной цикл
        root.destroy()  # Полностью закрыть окно
        return credentials + [str(pathway_func())] + checkbox_result

    # Кнопка для подтверждения
    button = tk.Button(root, text="Submit", command=lambda: [globals().update({'output': show_selections()})])
    button.pack(pady=10, padx=10)

    # Запуск главного цикла
    root.mainloop()

    # Возвращаем сохраненные данные
    return globals().get('output')
