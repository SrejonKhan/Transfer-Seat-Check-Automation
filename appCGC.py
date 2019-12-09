from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from seleniumrequests import Chrome
import time

class TC: 
    def __init__(self,regNumber,groupIndex,clgEIIN):
        self.regNumber = regNumber 
        self.groupIndex = groupIndex
        self.clgEIIN = clgEIIN 
        self.bot = Chrome()

    def  fillupCGC(self):
        bot = self.bot
        bot.get('https://xi.onlinetc.comillaboard.gov.bd/')
        time.sleep(2)
        regN = bot.find_element_by_name('roll')
        grp = Select(bot.find_element_by_name('current_group'))
        clg = Select(bot.find_element_by_name('tc_college'))
        regN.send_keys(self.regNumber)
        clg.select_by_value(self.clgEIIN)
        grp.select_by_value(self.groupIndex)
        bot.find_element_by_css_selector(".btn-primary").click()
        time.sleep(2)
        log = "<html><head></head><body>You are not eligiable. No Seat Available. Thank You!</body></html>"
        if bot.page_source == log:
            print("No Seat Available! CGC") 
            time.sleep(600)
            transfer.fillupCGC()                                   
        else:
            bot.get('http://api.greenweb.com.bd/api.php?token=3f0eae289407f8909d89e7624a4062d1&to=01647434617,01627129715&message=Transfer+has+started+dude+CGC')         
            time.sleep(600)
            transfer.fillupCGC()   
              
transfer = TC('1611229780', 'Science', '105824')
transfer.fillupCGC()