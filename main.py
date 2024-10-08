day_in_month = int(input("Введите день в месяце(число): "))
month = int(input("Введите номер месяца: "))
if ((day_in_month < 1 or day_in_month > 31) or (month < 1 or month > 12)):
    print("Вы некорректно ввели дату,такой даты не существует!")
else:
    if month == 1 :
        season = "Зима(Январь)"
    elif month == 2 :
        season = "Зима(Февраль)"
    elif month == 3 :
        season = "Весна(Март)"
    elif month == 4 :
        season = "Весна(Апрель)"
    elif month == 5 :
        season = "Весна(Май)"
    elif month == 6 :
        season = "Лето(Июнь)"
    elif month == 7 :
        season = "Лето(Июль)"
    elif month == 8 :
        season = "Лето(Август)"
    elif month == 9 :
        season = "Осень(Сентябрь)"
    elif month == 10 :
        season = "Осень(Октябрь)"
    elif month == 11 :
        season = "Осень(Ноябрь)"
    else :
        season = "Зима(Декабрь)"
print(f"Ваша пора года: {season}" )
        