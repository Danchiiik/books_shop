from django.core.mail import send_mail


def send_confirmation_email(email, code):
    full_link = f'http://localhost:8000/account/activate/{code}'
    send_mail(
        'User\'s activation code',
        f'Here is your activation code: {full_link} \n' 'Good luck!',
        'dcabatar@gmail.com',
        [email],
    )