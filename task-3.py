#Задание 3
def age():
    while True:
        try:
            age_stroka = input("Введите возраст: ")
            age_int = int(age_stroka)

            if age_int < 0:
                raise ValueError("Возраст не может быть отрицательным! :D ")

            if age_int >= 18:
                print("Вы совершеннолетний!")
            else:
                print("Вы несовершеннолетний!")
            break

        except ValueError as e:
            print(f"Ошибка: {e}")
            print("Пожалуйста, введите целое положительное число.")

age()
