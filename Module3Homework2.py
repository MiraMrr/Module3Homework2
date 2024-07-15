def send_email(message, recipient, *, sender = 'university.help@gmail.com'):

    if '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if '@' not in recipient or not recipient.endswith(('.com', '.ru', '.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return
    
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        return
    print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Приветствую вас на нашем курсе', 'student@mail.ru')
send_email('Hello World', 'english.student@mail.uk')
send_email('Поздравляем с завершением обучения', 'student@mail.ru', sender = 'university.info@gmail.com')
send_email('Проверка связи', 'university.help@gmail.com')
