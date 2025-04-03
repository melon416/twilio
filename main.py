import os, sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import pyautogui

from time import sleep
import random

class Bot:
    def __init__(self):
        self.driver = ""
        self.path_to_chromedriver = "C:/Users/Administrator/Documents/coinbase_automation/chromedriver.exe"
        self.coinbase_url = "https://commerce.coinbase.com/dashboard/payments"
        self.target_url = "https://firekirin.xyz:8888/"
        self.loggedin_url = "https://firekirin.xyz:8888/Store.aspx"
        self.profile_port = 9433
        self.name = ""
        self.amount = 1

    def driver_startup(self, port):
        chrome_options = Options()
        self.browser_url = f"127.0.0.1:{port}"
        chrome_options.add_experimental_option("debuggerAddress", self.browser_url)
        self.driver = webdriver.Chrome(self.path_to_chromedriver)

    def main(self, name):
        try:
            self.driver_startup(self.profile_port)
            sleep(random.randint(6,8))
            sleep(4)
            self.login()
            sleep(7)

            self.driver.switch_to.frame(self.driver.find_element_by_xpath('//iframe[@id="frm_main_content"]'))

            create_account_btn = self.driver.find_element_by_xpath('(//div[@class="SearchBg"]//a)[1]')
            create_account_btn.click()
            sleep(2)

            # self.driver.switch_to.default_content()
            # print("45454545")

            # self.driver.switch_to.frame(self.driver.find_element_by_xpath('//div[@id="DialogBySHF"]//iframe'))
            account = self.driver.find_element_by_xpath('//input[@name="txtAccount"]')
            account.send_keys(str(name))
            sleep(1)

            password = self.driver.find_element_by_xpath('//input[@name="txtLogonPass"]')
            password.send_keys('123123')
            sleep(1)

            confirm_password = self.driver.find_element_by_xpath('//input[@name="txtLogonPass2"]')
            confirm_password.send_keys('123123')
            sleep(1)

            save_btn = self.driver.find_element_by_xpath('//input[@name="btnSave1"]')
            save_btn.click()
            sleep(2)

            self.driver.switch_to.default_content()

            #check if it is successful or not
            msg = self.driver.find_element_by_xpath('//div[@id="mb_con"]//div[@id="mb_msg"]//p')
            if msg.text == "Added successfully":
                print('Account Creation Successful!')
                ok_btn = self.driver.find_element_by_xpath('//input[@id="mb_btn_ok"]')
                ok_btn.click()
                sleep(2)
                self.driver.close()
                return "success"
            elif msg.text == "The account number already exists, please re-enter it!":
                self.driver.close()
                return "exist"
            else:
                print('Account Creation not successful!')
                self.driver.close()
                return "fail"

            return "success"

        except:
            print("failed")
            return "fail"

    def redeem(self, idx):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//iframe[@id="frm_main_content"]'))
        sleep(1)

        #click update btn
        update_btn = self.driver.find_element_by_xpath('(//input[@value="Update"])['+str(idx)+']')
        print("update btn", update_btn)
        update_btn.click()
        sleep(2)

        redeem_btn = self.driver.find_element_by_xpath('(//div[@id="content"]//div[@class="SearchBg"]//a)[7]')
        redeem_btn.click()
        sleep(3)

        self.driver.switch_to.default_content()

        ###################
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//div[@id="DialogBySHF"]//iframe'))

        amount_input = self.driver.find_element_by_xpath('//input[@name="txtAddGold"]')
        amount_input.clear()
        sleep(0.5)
        amount_input.send_keys(self.amount)
        sleep(1)
        redeem_click = self.driver.find_element_by_xpath('//input[@name="Button1"]').click()
        sleep(2)

        self.driver.switch_to.default_content()

        #check if it is successful or not
        msg = self.driver.find_element_by_xpath('//div[@id="mb_con"]//div[@id="mb_msg"]//p')
        print("msg", msg.text)
        if msg.text == "Confirmed successful":
            print('Redeem Successful!')
            ok_btn = self.driver.find_element_by_xpath('//input[@id="mb_btn_ok"]')
            ok_btn.click()
            sleep(2)
        else:
            print('Redeem not successful!')

    def recharge(self, idx):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//iframe[@id="frm_main_content"]'))
        sleep(1)

        #click update btn
        update_btn = self.driver.find_element_by_xpath('(//input[@value="Update"])['+str(idx)+']')
        print("update btn", update_btn)
        update_btn.click()
        sleep(2)

        recharge_btn = self.driver.find_element_by_xpath('(//div[@id="content"]//div[@class="SearchBg"]//a)[6]')
        recharge_btn.click()
        sleep(3)

        self.driver.switch_to.default_content()

        ###################
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//div[@id="DialogBySHF"]//iframe'))

        amount_input = self.driver.find_element_by_xpath('//input[@name="txtAddGold"]')
        sleep(0.5)
        amount_input.send_keys(self.amount)
        sleep(1)
        recharge_click = self.driver.find_element_by_xpath('//input[@name="Button1"]').click()
        sleep(2)

        self.driver.switch_to.default_content()

        #check if it is successful or not
        msg = self.driver.find_element_by_xpath('//div[@id="mb_con"]//div[@id="mb_msg"]//p')
        print("msg", msg.text)
        if msg.text == "Confirmed successful":
            print('Recharge Successful!')
            ok_btn = self.driver.find_element_by_xpath('//input[@id="mb_btn_ok"]')
            ok_btn.click()
            sleep(2)
        else:
            print('Recharge not successful!')

    def login(self):
        print("Login:::::")
        self.driver.get(self.target_url)

        username_input = self.driver.find_element_by_xpath('//input[@id="txtLoginName"]')
        username_input.send_keys("Mainfirekirin")
        sleep(1)
        password_input = self.driver.find_element_by_xpath('//input[@id="txtLoginPass"]')
        password_input.send_keys("Teststore2")
        sleep(1)

        login_btn = self.driver.find_element_by_xpath('//input[@name="btnLogin"]')
        login_btn.click()

        

# if __name__ == '__main__':
#     bot = Bot()
#     bot.main("Ffrog887")
