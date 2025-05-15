import smtplib
from email.message import EmailMessage

email_origem = 'lucasagoncalves2019@gmail.com'
senha = 'tbxabozrfybucqrs'  # sem espaços/acentos
email_destino = 'lalvesgoncalves147@gmail.com'

msg = EmailMessage()
msg.set_content('Olá! Temos uma promoção imperdível para você! 😍')
msg['Subject'] = 'Promoção Exclusiva!'
msg['From'] = email_origem
msg['To'] = email_destino

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_origem, senha)
    smtp.send_message(msg)

print("Email enviado com sucesso!")
