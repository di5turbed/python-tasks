def schitatel():
    try:
        число = input("Введите положительное число: ")
        
        if not число.lstrip('-').isdigit():
            raise ValueError("Ошибка: Вы ввели не число!")
        
        число = int(число)

        if число < 0:
            print("Ошибка: число отрицательное!")
            return

        if число % 2 == 0:
            print(f"Число {число} является чётным")
        else:
            print(f"Число {число} нечётное")

    except ValueError as e:
        print(e)
        
schitatel()
