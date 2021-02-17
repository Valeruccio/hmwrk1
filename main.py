year = int(input("Какой сейчас год?"))
user_data = int(input("Каков твой стаж?"))
stage_1 = int(input("В каком году ты родился?"))
stage_0 =int(year - stage_1)

if stage_0 <= 18: stage_0>= 27:
    print("Ты не годен к призыву!")
else:
 print("Ты уже годен к призыву!")

print("Ты работаешь с " ,2021 - user_data, "года.")

stage_2 = (year - user_data)

if user_data >=5:
    print("Тебе пора менять работу!")
else: print("Ты что, гедонист?")

stage_3 = ((stage_1 - stage_2 )*(-1))
print("Ты не работал",stage_3, "лет своей жизни.")

stage_4 = (stage_1 + 65)
stage_5 = stage_4 - year
print("Год выхода на пенсию:",stage_4,"лет.", "Тебе осталось работать:", stage_5,"лет.")

