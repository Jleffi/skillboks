quantity = int(input('Введите колличество сотрудников: '))
wages_of_workers = []

for _ in range(quantity):
    wage = int(input(f'зарплата {_ + 1} сотрудника: '))
    if wage > 0:
        wages_of_workers.append(wage)


print('\nЗарплата сотрудников:', len(wages_of_workers))
print('Зарплаты', wages_of_workers)

print('\nДопполнительное задание')

print('максимальная З/п:', max(wages_of_workers))
print('Минимальная З/п:', min(wages_of_workers))



