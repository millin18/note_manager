# Создаем словарь
note = {}

# Собираем данные
note['username'] = input('Введите имя пользователя: ')
note['content'] = input('Введите описание заметки: ')
note['status'] = input('Введите статус заметки (например, "Активна" или "Выполнена": ')
note['created_date'] = input('Введите дату создания заметки в формате "день-месяц-год": ')
note['issue_date'] = input('Введите дату истечения заметки в формате "день-месяц-год": ')

#Добавляем заголовки в списки, список - внутрь словаря
note['titles'] = []
for i in range(3) :
    title = input(f'Введите заголовок заметки {i + 1}: ')
    note['titles'].append(title)

#Выводим данные на экран
print('\nСобранная информация о заметке:')
for key, value in note.items():
    print(f'{key.capitalize()} : {value}')
