
# -----------------------------------------------
# sends an email with the player's name and score
# -----------------------------------------------

import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import smtplib, ssl

def send_score(player_name, final_score, player_inventory):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "laf.adventure.host@gmail.com"  # Enter your address
    receiver_email = "laf.adventure.host@gmail.com"  # Enter receiver address
    password = "leopard2020"

    items_string = ""
    for item in player_inventory:
        items_string += item.name
        items_string += " (" + item.value + ") "

    message = """\
    Subject: SCOREBOARD UPDATE

    A new player just complete the 'Laf Adventure' treasure hunt!

    Name: {}
    Score: {}
    Items: {}
    """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.format(player_name, final_score, items_string))
