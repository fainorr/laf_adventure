
# -----------------------------------------------
# sends an email with the player's name and score
# -----------------------------------------------

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def send_score(player_name, final_score, player_inventory):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "laf.adventure.host@gmail.com"
    receiver_email = "laf.adventure.host@gmail.com"
    password = "leopard2020"

    # set up message
    msg = MIMEMultipart()
    msg['From'] = 'laf.adventure.host@gmail.com'
    msg['To'] = 'laf.adventure.host@gmail.com'
    msg['Subject'] = 'SCOREBOARD UPDATE'
    message = """

    A new player just completed the 'Laf Adventure' treasure hunt!

    Name: {}
    Score: {}
    Items: {}

    """

    # set up list of items for including in message
    items_string = ""
    for item in player_inventory:
        items_string += item.name
        items_string += " (" + str(item.value) + ") "
    msg.attach(MIMEText(message.format(player_name, final_score, items_string)))

    # send message
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email,msg.as_string())

    server.quit()
