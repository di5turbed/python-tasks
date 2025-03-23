#Задание 3
def возраст():
    try:
        число = input("Введите возраст:");
        if not число.isdigit():
            raise ValueError("Возраст не может быть отрицательным! :D ")
        
        число = int(число)

        if число >=18:
            print("Вы совершеннолетний!")
        else:
            print("Вы несовершеннолетний!")

    except ValueError as e:
        print(e)

возраст()