import tkinter as tk
# Step 1: Create the main window

root = tk.Tk()
root.title("Choose the data you want to get!")
# Step 2: List of checkbox labels (text shown next to each checkbox)
checkbox_labels = ["Date and time", "Device name", "Device description", "Firmware",
                   "Main task usage", "Serial number","Current project"]
checkbox_vars = {}

checkbox_result = list(range(len(checkbox_labels)))

for label in checkbox_labels:

    var = tk.BooleanVar(value=False)

    checkbox = tk.Checkbutton(root, text=label, variable=var)
    checkbox.pack(anchor="w")  # Align checkboxes to the left side
    checkbox_vars[label] = var

def show_selections():
    # Iterate through the dictionary and print the checkbox state
    j = 0
    for label, var in checkbox_vars.items():
        print(f"{label}: {'Selected' if var.get() else 'Not selected'}")
        checkbox_result[j] = var.get()
        j=j+1
        root.quit()
# Step 6: Add a button to trigger the show_selections function
button = tk.Button(root, text="Submit", command=show_selections)
button.pack()
# Step 7: Run the application
root.mainloop()
print(checkbox_result)

# import tkinter as tk
# # Create the main window
# root = tk.Tk()
# root.title("Choose the data, that you want to get")
#
# # Define a variable to hold the checkbox state
# checkbox_var = tk.IntVar()
# checkbox_var1 = tk.IntVar()
#
# # Create a checkbox
# checkbox = tk.Checkbutton(root, text="Task usage", variable=checkbox_var)
# checkbox1 = tk.Checkbutton(root, text="Firmware version", variable=checkbox_var1)
# checkbox.pack()
# checkbox1.pack()
#
# # Define a function to show the checkbox state
# def show_selection():
#     #print("Checkbox selected" if checkbox_var.get() else "Checkbox not selected")
#     #print("Checkbox1 selected" if checkbox_var1.get() else "Checkbox1 not selected")
#     data_arr = [checkbox_var.get(), checkbox_var1.get()]
#     print(data_arr)
#     root.quit()
# # Add a button to trigger the show_selection function
# button = tk.Button(root, text="Show Selection", command=show_selection)
# button.pack()
#
# # Run the application
# root.mainloop()