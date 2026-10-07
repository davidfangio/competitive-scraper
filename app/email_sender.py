import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()

EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
EMAIL_SENHA_APP = os.getenv("EMAIL_SENHA_APP")

SMTP_SERVIDOR = "smtp.gmail.com"
SMTP_PORTA = 587

def enviar_email(assunto, mensagem, destinatario):
    email = EmailMessage()

    email["From"] = EMAIL_REMETENTE
    email["To"] = destinatario
    email["Subject"] = assunto

    email.set_content(mensagem)

    with smtplib.SMTP(SMTP_SERVIDOR, SMTP_PORTA) as servidor:
        servidor.starttls()
        servidor.login(EMAIL_REMETENTE, EMAIL_SENHA_APP)
        servidor.send_message(email)