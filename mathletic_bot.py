from os import system
from colorama.ansi import Style
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from colorama import init, Fore, Style


browser  = webdriver.Chrome(ChromeDriverManager().install(), service_log_path="NUL")
browser.get('http://www.mathletics.com/')
base_div = "//*[@id=\"livemathletics\"]/body/div[1]/ui-view/div/div[1]/div[2]/div[2]/aligned-question/div/form/div"

def get_answer(xpath):        
    x1, x2 = browser.find_element_by_xpath(f"{xpath}").text[:-2].split(" + ")
    return [int(x1), int(x2)]

def input_answer(xpath, answer):
    browser.find_element_by_xpath(f"{xpath}/input").send_keys(answer[0]+answer[1])
    browser.find_element_by_xpath(f"{xpath}/input").send_keys(Keys.ENTER)
    print(f"Answer Submit: {Fore.GREEN}{answer[0]} + {answer[1]} = {answer}{Style.RESET_ALL}")

init(convert=True)
system("cls" or "clear")
while (True):
    try:
        input_answer(base_div, get_answer(base_div))
        
    except NoSuchElementException:
        input(f"{Fore.RED}[x]{Fore.WHITE} Game Not Found or Game Ended!\n" + 
              f"\nPress {Fore.CYAN}[Enter]{Style.RESET_ALL} once loaded into a game...\n"
        )
