year = int(input("Какой сейчас год?"))
user_data = int(input("Каков твой стаж?"))
stage_1 = int(input("В каком году ты родился?"))
stage_0 =int(year - stage_1)

if stage_0 < 18 and stage_0 > 27:
    print("Ты не годен к призыву!")
else:
 print("Ты не годен к призыву!")

print("Ты работаешь с " ,2021 - user_data, "года.")

stage_2 = (year - user_data)

if user_data >=5:
    print("Тебе пора менять работу!")
else: print('Ты что, гедонист?')

stage_3 = ((stage_1 - stage_2 )*(-1))
print("Ты не работал",stage_3, "лет своей жизни.")

stage_4 = (stage_1 + 65)
stage_5 = stage_4 - year
print("Год выхода на пенсию:",stage_4,"лет.", "Тебе осталось работать:", stage_5,"лет.")

print("--------------------------------------------------------------------------------")

print("ЗАДАЧА 1")

name = input("Введите свое имя:")
fingers = int(input("Введите актуальное количество пальцев на Ваших руках и ногах:"))

print(name,",")

if fingers < 20:
    print("cочувствую")
else: print("ты читал и подписывал требования безопасности!")

print("--------------------------------------------------------------------------------")

print("ЗАДАЧА 2")

time = int(input("Запиши время в секундах: "))
hour = time // 3600
min = (time - hour * 3600) // 60
sec = time - (hour * 3600 + min * 60)
print(f"Время на обычных часах: {hour} : {min} : {sec}")

print("--------------------------------------------------------------------------------")

print("ЗАДАЧА 3")

n = int(input("Введите требуемое число:"))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print("Сумма этих чисел в формате n+nn+nnn: %d" % total)

print("--------------------------------------------------------------------------------")

print("ЗАДАЧА 4")

n = abs(int(input("Введите любое многозначное число: ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Самая жирная цифра в числе: ", max)
        break

print("--------------------------------------------------------------------------------")

print("ЗАДАЧА 5")

profit = float(input("Введите выручку: "))
costs = float(input("Введите издержки: "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников "))
    print(f"Прибыль на одного сторудника составила {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

print("--------------------------------------------------------------------------------")

print("ЗАДАЧА 6")

a = int(input("Введите результат первого дня в км "))
b = int(input("Введите желаемый результат "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"Вы достигнете показателей на %.d день" % result_days)

print("--------------------------------------------------------------------------------")

print("Конец задания, спасибо за внимание!")

