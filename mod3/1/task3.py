
films = [

    'Крепкий орешек', 'Назад в будущее', 'Таксист', 

    'Леон', 'Богемская рапсодия', 'Город грехов',

    'Мементо', 'Отступники', 'Деревня', 

    'Проклятый остров', 'Начало', 'Матрица'

]
quantity = int(input('Сколько фильмов хотите добавить? '))
my_list = []
while len(my_list) < quantity:
        print('Ваш текущий топ фильмов:', my_list)
        name_films = input('Введите название фильма: ')
        if name_films in films:
            command = input('Команды: добавить, вставить, удалить: ')
            if command == 'добавить':
                if name_films not in my_list:
                    my_list.append(name_films)
                else:
                    print('Фильм уже есть в вашем топе!')
            elif command == 'удалить':
                if name_films in my_list:
                    my_list.remove(name_films)
                else:
                    print('Фильма нету в вашем топе')
            elif command == 'вставить':
                insert_index = int(input('введите номер позиции (с 1): '))
                my_list.insert(insert_index - 1, name_films)
            else:
                print('Неизвестная комманда')
        else:
            print('этого фильма у нас нет')    

print("\nПоздравляем! Ваш итоговый топ сформирован:")
print(my_list)