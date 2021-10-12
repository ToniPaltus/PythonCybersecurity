import requests
# 9.3
'''
Просто введите этот код
и запустите его.
Попробуй получить
данные по тегам из
json и поместите его в
дикт!
Исследуй и читай
этот код, гугл
могу помочь тебе/
** Приятно иметь: попробуйте
поместить ваши данные в
* .txt и добавить func
писать и читать
в / из файла по строке.
'''

class HhGrabber():
    HOME = "https://spb.hh.ru/"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win 64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-Us, en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://spb.hh.ru/",
        "Content-Type": "application/x-www-form-urlencoded",
        "DND": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "TE": "Trailers",
    }

    def __init__(self, username, password):
        self.session = requests.Session()
        self.session.headers = self.HEADERS
        self.auth(username, password)

    def getPage(self, url):
        return self.session.get(url).text

    def auth(self, username, password):
        get = self.session.get(self.HOME)
        print(get.text)
        abc = input("x: ")
        data = {
            "backUrl": "https://spb.hh.ru/",
            "action": "Войти",
            "username": username,
            "password": password,
            "_xsrf": abc
    }

grabber = HhGrabber("username", "password")
print(grabber.getPage(url="https://spb.hh.ru/account/login?backurl=/"))

