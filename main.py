day_in_month = int(input("Введите день в месяце(число): "))
month = int(input("Введите номер месяца: "))
if (day_in_month < 1 or day_in_month > 31) or (month < 1 or month > 12) or (month == 2 and day_in_month > 29):
    print("Вы некорректно ввели дату,такой даты не существует!")
else:
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day_in_month > days_in_month[month - 1]:
        print("Некорректный ввод даты.")
    else:
        # Проверяем, к какому времени года относится введенная дата
        if (month == 3 and day_in_month >= 1) or (month in [4, 5]) or (month == 6 and day_in_month < 1):
            season = "Весна"
        elif (month == 6 and day_in_month >= 1) or (month in [7, 8]) or (month == 9 and day_in_month < 1):
            season = "Лето"
        elif (month == 9 and day_in_month >= 1) or (month in [10, 11]) or (month == 12 and day_in_month < 1):
            season = "Осень"
        else:
            season = "Зима"
    print(f"Ваша дата относится к сезону: {season}")

