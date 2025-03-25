def schitatel():
    try:
        digit = input("Введите положительное число: ")
        
        if not digit.lstrip('-').isdigit():
            raise ValueError("Ошибка: Вы ввели не число!")
        
        digit = int(digit)

        if digit < 0:
            print("Ошибка: число отрицательное!")
            return

        if digit % 2 == 0:
            print(f"Число {digit} является чётным")
        else:
            print(f"Число {digit} нечётное")

    except ValueError as e:
        print(e)
        
schitatel()
