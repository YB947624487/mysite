import os
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

os.environ["DJANGO_SETTINGS_MODULE"] = 'mysite.settings'

"""
send_mail(
        '来自瓜瓜的测试邮件',
        'Thanks For Your Visit ---->♥这里瓜瓜大哥哥的QQ空间！',
        'melon_b_yang@sina.com',
        ['947624487@qq.com'],
    )
"""
if __name__ == "__main__":
    subject, from_email, to = '来自♥瓜瓜的测试邮件', 'melon_b_yang@sina.com', 'melon_b_yang@sina.com'
    text_content = '欢迎访问瓜瓜的QQ空间，♥♥♥.'
    html_content = '<p>Thanks for your visit ---><a href="https://user.qzone.qq.com/947624487?ADUIN=1285359449&ADSESSION=1560521325&ADTAG=CLIENT.QQ.5563_FriendTip.0&ADPUBNO=26785&source=namecardhoverstar" target=blank>瓜瓜大哥哥的空间!</a>0_0</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

