# Загружаем встроенную библиотеку datetime
from datetime import datetime

# Программа показывает текущую дату
current_date = datetime.now().date()
print('Текущая дата: ', current_date.strftime('%d-%m-%Y'))

# Запрашиваем у пользователя дату дедлайна
while True:
    issue_date = input('\nВведите дату истечения дедлайна заметки '
                   'в формате дд-мм-гггг, например 25-12-2025: ')
    try:
# Преобразуем введённую строку в объект datetime
        issue_date = datetime.strptime(issue_date, '%d-%m-%Y').date()
        print('Дата дедлайна успешно введена!\n')
        break
    except ValueError:
        print('Неверный формат даты, попробуйте снова.')

# Сравниваем даты
if current_date == issue_date:
    print('Дедлайн истекает сегодня!')
elif current_date < issue_date:
    diff = issue_date - current_date
    print('До дедлайна осталось', diff.days, 'дней.')
else:
    diff = issue_date - current_date
    print('Дедлайн просрочен на', abs(diff.days), 'дней!')