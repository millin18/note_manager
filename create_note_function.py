# импортируем библиотку datetime
from datetime import datetime

# запрашиваем данные пользователя
def create_note():
    username = input("Введите Ваше имя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите описание заметки: ")
    status = input("Введите статус заметки (новая, в процессе, выполнена): ")

# Запрашиваем дату дедлайна, проверяем корректность даты
    while True:
        issue_date = input("Введите дату дедлайна в формате день-месяц-год: ")
#преобразуем полученную строку в дату
        try:
            datetime.strptime(issue_date, '%d-%m-%Y')
            break
        except ValueError:
            print("Неверный формат даты. Пожалуйста, введите дату в формате день-месяц-год")

# добавляем сегодняшнюю дату
    created_date = datetime.now().strftime("%d-%m-%Y")

# Создаем словарь
    note = {
        "Имя пользователя": username,
        "Заголовок": title,
        "Описание": content,
        "Статус": status,
        "Дата создания заметки": created_date,
        "Дедлайн": issue_date
    }
    return note
if __name__ == '__main__':
    new_note = create_note()
    print('Создана заметка:', new_note)