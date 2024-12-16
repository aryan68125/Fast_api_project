import os
from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from decouple import config
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

class Envs:
    MAIL_USERNAME = config('EMAIL_HOST_USER_GMAIL')
    MAIL_PASSWORD = config('EMAIL_HOST_PASSWORD_GMAIL')
    MAIL_FROM = config('EMAIL_HOST_USER_GMAIL')
    MAIL_PORT = int(config('EMAIL_PORT_GMAIL'))
    MAIL_SERVER = config('EMAIL_HOST_GMAIL')

conf = ConnectionConfig(
    MAIL_USERNAME=Envs.MAIL_USERNAME,
    MAIL_PASSWORD=Envs.MAIL_PASSWORD,
    MAIL_FROM=Envs.MAIL_FROM,
    MAIL_PORT=Envs.MAIL_PORT,
    MAIL_SERVER=Envs.MAIL_SERVER,
    MAIL_STARTTLS=True,        # Replace MAIL_TLS
    MAIL_SSL_TLS=False,        # Replace MAIL_SSL
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER=os.path.join(os.getcwd(), "utility/email_templates")  # Correct directory path
)

# Setup Jinja2 environment to load templates
env = Environment(loader=FileSystemLoader(searchpath=str(Path(__file__).parent / "email_templates")))

async def send_email_async(subject: str, email_to: str, body: dict):
    # Render template with Jinja2
    template = env.get_template("email.html")
    rendered_body = template.render(**body)  # Unpack the dictionary
    
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=rendered_body,  # Pass the rendered HTML string
        subtype='html',
    )
    fm = FastMail(conf)
    await fm.send_message(message)

def send_email_background(background_tasks: BackgroundTasks, subject: str, email_to: str, body: dict):
    # Render template with Jinja2
    template = env.get_template("email.html")
    rendered_body = template.render(**body)  # Unpack the dictionary
    
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=rendered_body,  # Pass the rendered HTML string
        subtype='html',
    )
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
