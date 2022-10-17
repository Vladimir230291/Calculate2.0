print("*" * 15, "КАЛЬКУЛЯТОР", "*" * 15, "\n",
      "Введите номер операции для продолжения: ""\n"
      "1. Для вычисления рациональных чисел" "\n"
      "2. Для вычисления комплексных чисел" "\n"
      "3. Для вывода журнала совершенных операций" "\n"
      "4. Для очистки журнала совершенных операций""\n"
      "5. Для завершения работы""\n")
print("*" * 43)
flag = True
while flag:
    what = input("==>")
    if what == "1":
        flag = False
        pass
    elif what == "2":
        flag = False
        pass
    elif what == "3":
        flag = False
        pass
    elif what == "4":
        flag = False
        pass
    elif what == "5":
        break
    else:
        print("Введите только нужную цифру")
