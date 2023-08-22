from datetime import datetime, timedelta

def date_in_future(integer):
    if not isinstance(integer, int):
        return datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    future_date = datetime.now() + timedelta(days=integer)
    return future_date.strftime('%d-%m-%Y %H:%M:%S')


days_in_future = 10
result = date_in_future(days_in_future)
print(result)  # Вывод: дата, которая будет через 10 дней от текущего момента

non_integer_input = "abc"
result = date_in_future([])
print(result)  # Вывод: текущая дата, так как введено не целое число
