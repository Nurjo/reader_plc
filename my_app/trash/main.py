# # main.py
from hmi_popup import hmi_popup_func
# #if __name__ == "__main__":
# login_data = log_psw()  # Вызов функции и получение данных
# print(f"Received login data: {login_data}")
# # Выводим полученные данные

# from checkbox import checkbox
# print(checkbox)
data_from_hmi_popup = (hmi_popup_func())
print(data_from_hmi_popup)