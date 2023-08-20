from datetime import datetime, timedelta

def date_in_future(integer:int):
    try:
        days = int(integer)
        future_date = datetime.now() + timedelta(days=days)
        return future_date.strftime('%d-%m-%Y %H:%M:%S')
    except ValueError:
        current_date = datetime.now()
        return current_date.strftime('%d-%m-%Y %H:%M:%S')

# Примеры использования
days_in_future = 10
result = date_in_future(days_in_future)
print(result)  # Вывод: дата, которая будет через 10 дней от текущего момента

non_integer_input = "abc"
result = date_in_future(non_integer_input)
print(result)  # Вывод: текущая дата, так как введено не целое число
