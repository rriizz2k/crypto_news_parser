import telegram_send

def send_email(href, title, new, reason):
    f1 = ""
    for i in new:
        f1 += str(i) + " "
    new = f1

    telegram_send.send(messages=[title])
    telegram_send.send(messages=[new])

