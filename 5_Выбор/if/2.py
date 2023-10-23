r1 = float(input('Величина 1 сопротивления (Ом) -> '))
r2 = float(input('Величина 2 сопротивления (Ом) -> '))
connection_type = int(input('Как соединены? -> (1 – последовательное, 2 – параллельное) -> '))
if connection_type == 1:
    print('Сопротивление цепи', (r1 * r2) / (r1 + r2))
elif connection_type == 2:
    print('Сопротивление цепи', r1 * r2)
else:
    print('Некорректный ввод типа соединения!')

