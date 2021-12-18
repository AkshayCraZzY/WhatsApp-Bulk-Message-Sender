from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import pyperclip
import time
import sys
import os
import os.path
import mmap
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\aksha\\AppData\\Local\\Google\\Chrome\\User Data") 
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
#options.add_argument("window-size=1920x1080")
#options.add_argument('--log-level=3')
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.add_argument('start-maximized')
#options.add_argument("headless") # Runs Chrome in headless mode.
#options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('disable-gpu')  # applicable to windows os only
#options.add_argument('start-minimized') # 
options.add_argument('disable-infobars')
options.add_argument('disable-extensions')
#options.add_argument("--disable-web-security")
#options.add_argument("--allow-running-insecure-content")
#options.add_argument("--test-type")

link="https://web.whatsapp.com/send?phone=91"
with open(os.path.join(sys.path[0], "msg.txt"),"r+") as file:
    msg = file.read()
#msg="test."

def send():
    f = open("C:\\Users\\aksha\\Documents\\whatsapppy\\num.txt", "r+")
    nums = f.readlines()
    nums=  lines = [line.rstrip() for line in nums]
    buf = mmap.mmap(f.fileno(), 0)
    lines = 0
    readline = buf.readline
    while readline():
        lines += 1
    count=0
    sent=0
    w = webdriver.Chrome(options=options)
    while (count < lines): 
        tosend = nums[count]
        if len(tosend) != 10:
            count = count + 1
            
            print('\nNumber '+tosend+' is not a valid number (Number lenght '+str(len(tosend))+' not allowed).')
            linkk='about:blank'
            continue
        else:
          linkk=link+tosend
        w.get(linkk)
        #w.get('chrome://version')
        
       
        search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
        search_box = WebDriverWait(w, 100).until(EC.presence_of_element_located((By.XPATH, search_xpath)))
        #print('found')

        time.sleep(2)
        try:
            invbt = w.find_element_by_class_name('nne8e')

        except:
            #print("------- WhatsApp Number "+tosend+" is VALID -------")
            msg_xpath = '//div[@contenteditable="true"][@data-tab="9"]'
            msg_box = WebDriverWait(w, 100).until(EC.presence_of_element_located((By.XPATH, msg_xpath)))
          #  print("Msg Found")
            msg_box.click()
            pyperclip.copy(msg)

            msg_box.send_keys(Keys.SHIFT, Keys.INSERT)
            msg_box.send_keys(Keys.ENTER)
            sent = sent+1
            w.get_screenshot_as_file("C:\\Users\\aksha\\Documents\\whatsapppy\\screencaptures\\"+tosend+"_ss.png")
            print('\nMessage sent to '+tosend+'.')
            w.execute_script("window.close();")
            time.sleep(2)
                #w.execute_script("window.open('about:blank','secondtab');")
                #w.switch_to.window("secondtab")
                #p= w.window_handles[0]
                #obtain browser tab window
                #c = w.window_handles[1]
            # w.switch_to.window(p)
            # w.close()
            #w.switch_to.window(c)
            count = count + 1
            time.sleep(1)
        else:
            print('\nNumber '+tosend+' is not on WhatsApp.')
            count = count + 1
            
    else:
        w.close()
        w.quit()
        print('\nReport:  '+str(sent)+'/'+str(lines)+' successfull.')
       # print('\nSent messages to '+str(sent)+' numbers from '+str(lines)+' given numbers.')
        sys.exit()


    
    
 

    


send()


#sys.exit()