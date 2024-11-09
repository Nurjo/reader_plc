import tkinter as tk
from tkinter import filedialog

def pathway_func():
    # Создаем основное окно (необязательно, если только нужно окно для выбора файла)
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно

    # Открываем диалоговое окно для выбора файла
    file_path = filedialog.askopenfilename(title="Choose IP list file", filetypes=(("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")))

    # Проверяем путь
    # if file_path:
    #     print(f"Выбранный путь к файлу: {file_path}")
    # else:
    #     print("Файл не выбран")
    return file_path

