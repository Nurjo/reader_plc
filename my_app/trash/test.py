# import tkinter as tk
# from tkinter import simpledialog
#
#
# def hmi_popup_func():
#     # Create a new Tkinter window
#     popup = tk.Tk()
#     popup.withdraw()  # Hide the main window
#
#     # Use simpledialog to prompt for input
#     data = simpledialog.askstring("Input", "Enter data from HMI:")
#
#     # Destroy the popup window after getting the input
#     popup.destroy()
#
#     return data
#
#
# # Example usage
# data_from_hmi_popup = hmi_popup_func()
# print("Data from HMI Popup:", data_from_hmi_popup)


a = [10, 20, 30]
b =(enumerate((a)))
#print(a[0])

c =(list(enumerate(a)))
#print(c)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)
print(car['brand'])