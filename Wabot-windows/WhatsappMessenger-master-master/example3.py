# -- coding: utf-8 --
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
from urllib.parse import quote
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("user-data-dir=/Users/vaibhavchopra/Library/Application Support/Google/Chrome/Default")

message = """
Greetings from ISTE-VIT!
%0d%0a
You have registered for our 48-hour hackathon, Techinca'22 on VTOP. 
%0d%0a%0d%0a
*Please make sure you join the discord server for further details regarding the hackathon and register yourself on Devpost before 3 pm today.*
%0d%0a%0d%0a
Discord: https://bit.ly/Horizon22_Discord
%0d%0a
Devpost: https://bit.ly/Technica_ISTE-VIT
%0d%0a%0d%0a
✨Happy Hacking!

"""






numbers = []
f = open("D:\Tirth\Wabot\Wabot-windows\WhatsappMessenger-master-master\main.txt", "r")
for line in f.read().splitlines():
    if line != "":
        numbers.append(line)
f.close()
# numbers.reverse()
TRIES = 30

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.get('https://web.whatsapp.com')
# input()
c=0
for number in numbers[0:]:
    c+=1
    print(c)
    if number == "":
        continue
    print("Number: " + number)
    try:
        url = "https://web.whatsapp.com/send?phone=91" + number + "&text=" + message
        #print(url)
        driver.get(url)
        sleep(10)
        # click_btn = driver.find_elements(By.CSS_SELECTOR,"footer > div.copyable-area  div:nth-child(3) > button").get(0)
        click_btn = WebDriverWait(driver, TRIES).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_1Ae7k"))
        )
        click_btn.click()
        sleep(3)
        print("Message sent to: " + number)
    except Exception:
        print("Failed to send message to " + number)
        # append these number to failed.txt
        f = open("failed.txt", "a")
        f.write(number + "\n")
        f.close()
driver.quit()