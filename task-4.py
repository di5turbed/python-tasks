#Задание 4
def length():
    while True:
        digit = input("Введите число (или 'exit' для выхода):")
        
        if digit.lower() == "exit":
            print("Выход из программы...")
            break
        
        try:
            num = int(digit)
            length = len(digit.lstrip('-'))
            print(f"В этом числе {length} цифр.")
        except:
            print("Ошибка: введённые данные не являются целым числом.")

length()
