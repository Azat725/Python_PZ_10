num = int(input('Введите число: '))
faktorial = 1

for i in range(1, num + 1):
    faktorial = faktorial * i
    print(faktorial)