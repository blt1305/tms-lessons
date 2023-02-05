#Напишите функцию my_round, аналог встроенной round (ссылка на документацию). Использование самой функции round запрещено.
def my_round(number: float, digit: int) -> float:
    factor = 10.0 ** digit         #коэффициент пересчета - 10 в степени того числа, сколько знаков нужно оставить
    resalt = number * factor       #умножаем число на коэффициент
    resalt = resalt + 0.5          #добавляем 0,5, если после знака число > 0,5, то случится переход через 1
    resalt = int(resalt)           #отбрасываем знаки после запятой
    resalt = resalt / factor       #делим на тот же коэффициент
    return resalt

print(my_round(1.235, 2))
print(my_round(78.565941, 3))
