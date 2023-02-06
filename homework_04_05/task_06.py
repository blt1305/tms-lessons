#Напишите функцию is_year_leap, которая принимает число (год) и возвращает True если год високосный
#(см. комментарий к слайда), False если нет.
#Распределение високосных годов:
#год, номер которого кратен 400, — високосный;
#остальные годы, номер которых кратен 100, — невисокосные (например, годы 1700, 1800, 1900, 2100, 2200, 2300);
#остальные годы, номер которых кратен 4, — високосные[5];
#все остальные годы — невисокосные.

def is_year_leap(year: int) -> bool:
    resalt = False
    if year % 4 == 0:                #если год делится на 4, то проверяем дальше, иначе - год не високосный
        if year % 100 != 0:          #если не делится на 100, значит не столетие - год високосный
            resalt = True
        else:                        #если делится - значит столетие, проверяем дальше
            if year % 400 == 0:      #год кратен 400 - значит високосный
                resalt = True
    return resalt


for i in [1700, 1800, 2020, 1980, 2001]:
    print(f'год {i}: {is_year_leap(i)}')

