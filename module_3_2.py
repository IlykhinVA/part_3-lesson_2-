def send_email(message, recipient, sender='university.help@gmail.com'):
    domens = ['.net', '.ru', '.com']
    default_sender = 'university.help@gmail.com'
    for i in range(len(domens)):
        start_find = len(recipient) - len(domens[i])
        end_find = len(recipient)
        if recipient[start_find:end_find] == domens[i]:
            domen_rec = True
            break
    else:
        domen_rec = False

    for k in range(len(domens)):
        start_find = len(sender) - len(domens[k])
        end_find = len(sender)
        if sender[start_find:end_find] == domens[k]:
            domen_sen = True
            break
    else:
        domen_sen = False

    if recipient.find('@') >= 0:
        rec_dog = True
    else:
        rec_dog = False

    if sender.find('@') >= 0:
        sen_dog = True
    else:
        sen_dog = False

    if sender != recipient:
        m_box = True
    else:
        m_box = False

    if sender == 'university.help@gmail.com':
        lic_sen = True
    else:
        lic_sen = False

    if domen_rec + domen_sen + rec_dog + sen_dog + m_box + lic_sen == 6:
        message = 'Письмо успешно отправлено с адреса ' + str(sender) + ' на адрес ' + str(recipient)
        return (message)
    elif domen_rec + domen_sen + rec_dog + sen_dog < 4:
        message = 'Невозможно отправить письмо с адреса ' + str(sender) + ' на адрес ' + str(recipient)
        return (message)
    elif m_box == 0:
        message = 'Нельзя отправить письмо самому себе'
        return (message)
    elif domen_rec + domen_sen + rec_dog + sen_dog + m_box + lic_sen == 5:
        message = 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отпралено с адреса ' + str(sender) + ' на адрес ' + str(recipient)
        return (message)


print(send_email('Ппроверка связи', 'to_grandpa_s_village@comtv.ru'))
print(send_email('Ппроверка связи', 'to_grandpa_s_village@comtv.de'))
print(send_email('Ппроверка связи', 'to_grandpa_s_villagecomtv.ru'))
print(send_email('Ппроверка связи', 'to_grandpa_s_villagecomtv.ru', 'university.helpgmail.ua'))
print(send_email('Ппроверка связи', 'to_grandpa_s_village@comtv.ru', 'to_grandpa_s_village@comtv.ru'))
print(send_email('Ппроверка связи', 'to_grandpa_s_village@comtv.ru', 'university.teacher@gmail.com'))
