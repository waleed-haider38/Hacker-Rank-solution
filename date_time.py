import datetime

today_time = datetime.datetime.now()
today_date = datetime.date.today()

# print(today_date)
# print(today_time)

# birthday_str = input("Enter your birthday (YYYY-MM-DD): ")

# 2) string → datetime convert karo
# birthday_date = datetime.datetime.strptime(birthday_str, "%Y-%m-%d").date()

# 3) aaj ki date lo
# today_date = datetime.date.today()

# 4) difference nikal lo
# remaining_days = birthday_date - today_date

# 5) result print
# print("Days left:", remaining_days.days)
now = datetime.datetime.now()
print(datetime.datetime.now())
print(now.strftime("%H:%M:%S"))
