name  = input(int('名前を入力'))
from datetime import datetime

def greet():
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
         message = 'Hello, ' + name + '-san!'
    else:
        message = 'Good evening'
    print(message)


greet()
