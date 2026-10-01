import math_expr
import sum_multiples

def menu():
    while True:
        print("\n================ МЕНЮ ================")
        print("1. Обчислити значення виразу y = (|a - b| + cos(x)) / (1 + sqrt(y_in))")
        print("2. Знайти суму чисел, кратних 5, у діапазоні [500, 1000]")
        print("0. Вихід")
        print("======================================")
        
        choice = input("Оберіть пункт меню (0-2): ").strip()
        
        if choice == '1':
            try:
                a = float(input("Введіть a: "))
                b = float(input("Введіть b: "))
                x = float(input("Введіть x (в радіанах): "))
                y_in = float(input("Введіть y (y >= 0): "))
                
                if y_in < 0:
                    print("Помилка: підкореневе значення y_in не може бути від'ємним!")
                    continue
                
                result = math_expr.calculate_y(a, b, x, y_in)
                print(f"\n[Результат]: y = {result:.6f}")
            except ValueError as e:
                print(f"Помилка введення або розрахунку: {e}")

        elif choice == '2':
            result_sum = sum_multiples.calculate_sum_multiples_of_5(500, 1000)
            print(f"\n[Результат]: Сума чисел, кратних 5 від 500 до 1000 = {result_sum}")

        elif choice == '0':
            print("Завершення роботи програми.")
            break
        else:
            print("Некоректний вибір! Спробуйте ще раз.")

if __name__ == "__main__":
    menu()