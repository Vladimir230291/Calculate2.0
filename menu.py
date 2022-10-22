import sys
from calculator import main as calculator
from base import readLog, clearLog, deleteLog

menuText = [
    "*" * 15 + "КАЛЬКУЛЯТОР" + "*" * 15,
    "Введите номер операции для продолжения:",
    "1. Сделать вычисление на калькуляторе",
    "2. Для вывода журнала совершенных операций",
    "3. Для очистки журнала совершенных операций",
    "4. Для завершения работы",
    "*" * 43
]

for mt in menuText:
    print(mt)


def terminate():
    deleteLog()
    sys.exit("Bye!!")


menuActions = {
    '1': calculator,
    '2': readLog,
    '3': clearLog,
    '4': terminate
}


while True:
    action = input("==>")
    if action not in menuActions:
        print("--Выбран неверный пункт меню--")
    else:
        menuActions[action]()
