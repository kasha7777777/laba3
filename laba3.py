def a1():
    list = []
    word = input("Введите слово: ")
    while word != "stop":
        list += word.split()
        word = input("Введите слово: ")
        continue
    print(list)

def a2():
    word = input("Введите слово: ")
    z = "з"
    if z in word:
        print("Редкое слово!")
    else:
        print("обычное слово!")

def a3():
    import random
    life = 3
    answer = 0
    while life <= 3:
        if life == 0:
            print(f"Игра окончена! Правильных ответов: {answer}")
            break
        chislo1 = random.randint(0, 9)
        chislo2 = random.randint(0, 9)
        v = chislo1 + chislo2
        v2 = int(input(f"Кол-во жизней: {life}. {chislo1} + {chislo2}? Ответ: "))
        if v == v2:
            print("Верно!")
            answer += 1
        else:
            print("Неверно!")
            life -= 1
        continue

a1()
a2()
a3()