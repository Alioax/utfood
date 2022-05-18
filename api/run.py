import requests
import random
from bs4 import BeautifulSoup
import datetime
from datetime import date
import calendar

from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        print('I raaaaan!!!!')
        cookies = {
            '__RequestVerificationToken': '2CVOfIo4TxTJ05ZpuoFpc43B7_np5prStM6q__qY1BR6j9Mxgk4UN174ZVBi6pX1S7AmhULkfewSy_dBAmtfnDfNGMHbn70R54a3K3T0ogs1',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': '__RequestVerificationToken=2CVOfIo4TxTJ05ZpuoFpc43B7_np5prStM6q__qY1BR6j9Mxgk4UN174ZVBi6pX1S7AmhULkfewSy_dBAmtfnDfNGMHbn70R54a3K3T0ogs1',
            'Origin': 'http://canmeal.ut.ac.ir',
            'Referer': 'http://canmeal.ut.ac.ir/Account/Login?ReturnUrl=%2f',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
        }

        data = {
            '__RequestVerificationToken': 'ZsrELH8GLjA2i04IXBYmT4yX51ktS4z7vMgDLA-1HKY2PKyoSzyzdkBGcSQ9o5uGuLlYyNprpkbmpr3yNp0suaV-VE-pF7W3vmgTHZCuGOc1',
            'UserName': '2283642868',
            'Password': 'Free8Wild!',
            'RememberMe': 'false',
        }

        response = requests.post('http://canmeal.ut.ac.ir/Account/Login?ReturnUrl=%2f',
                                 cookies=cookies, headers=headers, data=data, verify=False)
        print('sessionID = ' + str(response.status_code))
        sessionID = response.cookies['ASP.NET_SessionId']

        cookies = {
            '__RequestVerificationToken': '2CVOfIo4TxTJ05ZpuoFpc43B7_np5prStM6q__qY1BR6j9Mxgk4UN174ZVBi6pX1S7AmhULkfewSy_dBAmtfnDfNGMHbn70R54a3K3T0ogs1',
            'DGAUTH': 'AAD5758C7C2CD5718D4891ED7F60EB01FE68E853B684A82F05F48916898E06B49FA065F1A277D355C8840BA3A4047C2FC68B2A286EF8859862FD5D73A56CEA2A382828465D5C535C3C40AFEA93863B024F57E87198B599977AE23B078C4CC96A',
            '.AspNet.ApplicationCookie': '32lxAa3Irq2EHESlcC-O_Nf0jn-6XChZc6fGw9ABpNgSqlgayokjpo7FsxoA-dciDn5aD8bm7QLSmfoRGsIFd7tHQj2epsbvvIM5VvSIi1D5g3dwEDXrvEevramaES6pxdF8MFToXE7dIff4Xuq-mXI7qxGZcHJqPmTxQ5DXuHdCL-1dmiJ_4cXD0twygvam6C_Wx9ItdKn0Aqg_cxIrXfAn5CthDahAkNmne-g1D8BH9XiHrxBpZVzigJfVubUHozz42rzjCRWKO_u7F9sGbRNB3m4Z3OM8UqPau1A0_ZLJ7jcyzsp4ZALWeS-sTKmwKc5HC3Ty2DPqi3puhw9n0DhQ9Ys7jjy7QhY0mHNtam2OSdjljk7Q5U9ieAAQCuVX4HxJwAU4lsyqWutoWnOOiGn6TVUCNomvJRpjrXYItS7E1HYA4PKO4I_hn8O98M32keGD7X57D6fAKYmonJnuGspaxmAlGvzVVfKQmYINtaM',
            'ASP.NET_SessionId': f'{sessionID}',
            'fn': '',
        }

        headers = {
            'Accept': 'text/html, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # Requests sorts cookies= alphabetically
            # 'Cookie': '__RequestVerificationToken=2CVOfIo4TxTJ05ZpuoFpc43B7_np5prStM6q__qY1BR6j9Mxgk4UN174ZVBi6pX1S7AmhULkfewSy_dBAmtfnDfNGMHbn70R54a3K3T0ogs1; DGAUTH=AAD5758C7C2CD5718D4891ED7F60EB01FE68E853B684A82F05F48916898E06B49FA065F1A277D355C8840BA3A4047C2FC68B2A286EF8859862FD5D73A56CEA2A382828465D5C535C3C40AFEA93863B024F57E87198B599977AE23B078C4CC96A; .AspNet.ApplicationCookie=32lxAa3Irq2EHESlcC-O_Nf0jn-6XChZc6fGw9ABpNgSqlgayokjpo7FsxoA-dciDn5aD8bm7QLSmfoRGsIFd7tHQj2epsbvvIM5VvSIi1D5g3dwEDXrvEevramaES6pxdF8MFToXE7dIff4Xuq-mXI7qxGZcHJqPmTxQ5DXuHdCL-1dmiJ_4cXD0twygvam6C_Wx9ItdKn0Aqg_cxIrXfAn5CthDahAkNmne-g1D8BH9XiHrxBpZVzigJfVubUHozz42rzjCRWKO_u7F9sGbRNB3m4Z3OM8UqPau1A0_ZLJ7jcyzsp4ZALWeS-sTKmwKc5HC3Ty2DPqi3puhw9n0DhQ9Ys7jjy7QhY0mHNtam2OSdjljk7Q5U9ieAAQCuVX4HxJwAU4lsyqWutoWnOOiGn6TVUCNomvJRpjrXYItS7E1HYA4PKO4I_hn8O98M32keGD7X57D6fAKYmonJnuGspaxmAlGvzVVfKQmYINtaM; ASP.NET_SessionId=g5rhvlzxkmfnekzbekxu1uzd; fn=',
            'Origin': 'http://canmeal.ut.ac.ir',
            'Referer': 'http://canmeal.ut.ac.ir/Reserves',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
            'X-Requested-With': 'XMLHttpRequest',
        }

        data = {
            'personId': '0',
            'personGroupId': '1031',
            'restId': '1053',
        }

        response = requests.post('http://canmeal.ut.ac.ir/Reserves/GetReservePage',
                                 cookies=cookies, headers=headers, data=data, verify=False)
        print('reserve page = ' + str(response.status_code))

        soup = BeautifulSoup(response.text, 'html.parser')
        foods = soup.find_all(
            attrs={"style": "display: flex; flex-direction: row; flex-wrap: wrap; clear: both;"})
        lunch = foods[0].findAll(id='MealDiv')
        dinner = foods[1].findAll(id='MealDiv')

        class day:
            def __init__(self, date, lunch0, lunch1, dinner0, dinner1):
                self.date = date
                self.lunch0 = lunch0
                self.lunch1 = lunch1
                self.dinner0 = dinner0
                self.dinner1 = dinner1

        def create_day(day_index):

            date = lunch[day_index].find(id='DateDiv').contents[0]

            try:

                lunch0 = lunch[day_index].findAll(
                    "label", class_="reserveFoodCheckBox")[0].contents[0].strip()
            except:
                lunch0 = None

            try:
                lunch1 = lunch[day_index].findAll("label", class_="reserveFoodCheckBox")[
                    1].contents[0].strip()
            except:
                lunch1 = None

            try:
                dinner0 = dinner[day_index].findAll("label", class_="reserveFoodCheckBox")[
                    0].contents[0].strip()
            except:
                dinner0 = None

            try:
                dinner1 = dinner[day_index].findAll("label", class_="reserveFoodCheckBox")[
                    1].contents[0].strip()
            except:
                dinner1 = None
            return(day(date, lunch0, lunch1, dinner0, dinner1))

        datetime.datetime.today().weekday()
        curr_date = date.today()
        curr_day = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday'].index(calendar.day_name[curr_date.weekday()])

        Today = create_day(curr_day)

        # bot_token = '5324292612:AAEGKc3LvTY5bAmwR4OcYnRXIjhchWPQy8s'
        # channel_id = '-1001651126277'

        # food_emoji = random.choice(['🍪', '🍫', '🍉', '🥦', '🍧', '🍰', ])
        # post_emoji = random.choice(['🍪', '🍫', '🍉', '🥦', '🍧', '🍰', ])

        # has_lunch = True if Today.lunch0 or Today.lunch1 is not None else False
        # has_dinner = True if Today.dinner0 or Today.dinner1 is not None else False
        # has_food = has_lunch or has_dinner

        # morning_text = food_emoji + ' ' + f'صبح بخیر'
        # skip_line = '\n'
        # end_text = Today.date + skip_line + f'{post_emoji} لذت ببرید!'

        # lunch_text = ''
        # if Today.lunch0 is not None:
        #     lunch_text = '\n\n' + '*ناهار امروز:*' + \
        #         skip_line + f'- {Today.lunch0}'
        #     if Today.lunch1 is not None:
        #         lunch_text = lunch_text + skip_line + f'- {Today.lunch1}'

        # dinner_text = ''
        # if Today.dinner0 is not None:
        #     dinner_text = '\n\n' + '*شام امروز:*' + \
        #         skip_line + f'- {Today.dinner0}'
        #     if Today.dinner1 is not None:
        #         dinner_text = dinner_text + skip_line + f'- {Today.dinner1}'

        # text = morning_text + lunch_text + dinner_text + skip_line * 3 + end_text

        # no_food_text = morning_text + 2 * skip_line + \
        #     'امروز سلف غذا سرو نمی کند' + skip_line * 2 + Today.date

        # url = "https://api.telegram.org/bot" + \
        #     str(bot_token) + "/" + str('sendMessage')
        # payload = {'chat_id': channel_id,
        #            'text': (text.replace('-', '\-').replace('+', '\+').replace('!', '\!').replace(')', '\)').replace('(', '\(').replace('  ', ' ') if has_food else no_food_text.replace('-', '\-').replace('+', '\+').replace('!', '\!').replace(')', '\)').replace('(', '\(').replace('  ', ' ')), 'parse_mode': 'MarkdownV2'}

        # r = requests.get(url, params=payload)
        # print(r)
        self.wfile.write(
            str(str('غذا امروز ای هه: ' + Today.lunch0).encode()))
        return
