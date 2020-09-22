# automated DMs

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import schedule
import random


global x
x = 0


def dmer(username,password,user,message):
    usrnames = [user]

    chrome_options = Options()
    chrome_options.add_argument(
        '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    browser = webdriver.Chrome("chromedriver.exe", options=chrome_options)
    browser.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)

    usrname_bar = browser.find_element_by_name('username')  # Find the username bar
    passwrd_bar = browser.find_element_by_name('password')  # Find the password bar

    username = username
    password = password

    usrname_bar.send_keys(username)
    passwrd_bar.send_keys(password + Keys.ENTER)

    time.sleep(11)

    def send_msg(usrnames):
        browser.get('https://www.instagram.com/direct/new/')

        time.sleep(5)

        to_btn = browser.find_element_by_name('queryBox')
        to_btn.send_keys(usrnames)

        time.sleep(8)

        chk_mrk = browser.find_element_by_class_name('dCJp8')
        chk_mrk.click()

        time.sleep(3)

        nxt_btn = browser.find_element_by_xpath('//div[@class="mXkkY KDuQp"]')
        nxt_btn.click()

        time.sleep(6)

        for tex in message:
            txt_box = browser.find_element_by_tag_name('textarea')
            txt_box.send_keys(tex)  # Customize your message

            value = random.randrange(2,4)
            time.sleep(value)

            snd_btn = browser.find_elements_by_tag_name('button')
            snd_btnn = snd_btn.__getitem__(3)
            snd_btnn.click()

            value = random.randrange(4, 7)
            time.sleep(value)


    count = 0
    try:
        for usrnamee in usrnames:
            send_msg(usrnamee)
            count += 1

    except TypeError:
        print('Failed!')

    browser.quit()

    x += 1


textall = []

for i in range(100):
    text = ""

    for z in range(i):
        text += "o"

    text = "o" + text + " ley"

    textall.append(text)


for i in textall:
    print(i)

dmer("user","pass","targetuser",textall)


""""
timee = "17:14"  # Specific Time When The message will be send

try:
    schedule.every().day.at(timee).do(dmer)
except TypeError:
    pass

try:
    while True and x != 1:
        schedule.run_pending()
        time.sleep(1)
except UnboundLocalError:
    print('')
"""