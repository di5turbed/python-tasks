имя = input("Введите ваше имя: ")
фамилия = input("Введите вашу фамилию: ")
возраст = input("Введите ваш возраст: ")

a = "Ваше имя: {}, Фамилия: {}, Возраст: {} лет.".format(имя, фамилия, возраст)
print(a)

b = f"Ваше имя: {имя}, Фамилия: {фамилия}, Возраст: {возраст} лет."
print(b)

def schitatel():
    try:
        число = input("Введите положительное число:");
        if not число.isdigit():
            raise ValueError("Ошибка: Введено не число")
        
        число = int(число)

        if число <0:
            print("Ошибка: введено отрицательное число")
            return

        if число % 2 == 0:
            print(f"Число {число} является чётным")
        else:
            print(f"Число {число} нечётное")

    except ValueError as e:
        print(e)

schitatel()

def schitatel():
    try:
        число = input("Введите положительное число:");
        if not число.isdigit():
            raise ValueError("Ошибка: Введено не число")
        
        число = int(число)

        if число <0:
            print("Ошибка: введено отрицательное число")
            return

        if число % 2 == 0:
            print(f"Число {число} является чётным")
        else:
            print(f"Число {число} нечётное")

    except ValueError as e:
        print(e)

schitatel()

def age():
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

age()

def длина():
    while True:
        ввод = input("Введите число: → ")
        
        if ввод.lower() == "exit":
            print("Выход из программы...")
            break
        
        if ввод.lstrip('-').isdigit():
            количество = len(ввод.lstrip('-'))
            print(f"В этом числе {количество} цифр.")
        else:
            print("Ошибка: данные не являются числом.")
длина()