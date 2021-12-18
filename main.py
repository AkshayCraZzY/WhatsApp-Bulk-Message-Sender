import pyperclip
import time
import sys
import os
import os.path
import mmap
import warnings
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#from selenium.common.exceptions import NoSuchElementException
warnings.filterwarnings("ignore", category=DeprecationWarning)

scriptdir="C:\\Users\\aksha\\Documents\\WBMS\\"
link="https://web.whatsapp.com/send?phone=91"

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir="+scriptdir+"wbms\\User Data") 
#options.add_argument("user-data-dir=C:\\Users\\aksha\\AppData\\Local\\Google\\Chrome\\User Data") 
#options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
options.add_argument("window-size=1080x720")
options.add_argument('--log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('disable-gpu')
options.add_argument('disable-infobars')
options.add_argument('disable-extensions')
print("\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print(" - - - - - - WBMS - WhatsApp Bulk Message Sender - - - - - -")
print(" - - - - - - - - - Github.com/AkshayCraZzY - - - - - - - - -")
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

with open(os.path.join(sys.path[0], "msg.txt"),"r+") as file:
    msg = file.read()


def send():
    if os.stat(scriptdir+"num.txt").st_size == 0:
        print('\n - - - - - -0 numbers found in num.txt, Exiting - - - - - -')
        sys.exit()
    f = open(scriptdir+"num.txt", "r+")
    nums = f.readlines()
    nums=  lines = [line.rstrip() for line in nums]
    buf = mmap.mmap(f.fileno(), 0)
    lines = 0
    readline = buf.readline
    while readline():
        lines += 1
    print('\n - - - - - - '+str(lines)+' numbers found in num.txt, Starting- - - - - -')
    #print('\n - - - - - - - - Found '+str(lines)+' numbers in num.txt - - - - - - - -')
    print("\n - - - - - - - - - - - -Your Message - - - - - - - - - - - -")
    print('"'+msg+'"')
    print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    f = open(scriptdir+"failed.txt", "a")
    f.write('\n---Edited on '+datetime.fromtimestamp(datetime.timestamp(datetime.now())).strftime("%d %B %I:%M %p")+'---\n')
    f.close()
    count=0
    sent=0
    w = webdriver.Chrome(options=options)
    #w.minimize_window()

    while (count < lines): 
        tosend = nums[count]
        if len(tosend) != 10:
            count = count + 1
            f = open(scriptdir+"failed.txt", "a")
            f.write(tosend+'\n')
            f.close()
            time.sleep(15)
            print('\n - - Number '+tosend+' is not a 10 digit number, skipping - - ')
            linkk='about:blank'
            continue
        else:
          linkk=link+tosend
        
        w.get(linkk)
        search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
        WebDriverWait(w, 100).until(EC.presence_of_element_located((By.XPATH, search_xpath)))
        time.sleep(2)

        try:
            w.find_element_by_class_name('nne8e')
        except:
            msg_xpath = '//div[@contenteditable="true"][@data-tab="9"]'
            msg_box = WebDriverWait(w, 100).until(EC.presence_of_element_located((By.XPATH, msg_xpath)))
            msg_box.click()
            pyperclip.copy(msg)
            msg_box.send_keys(Keys.SHIFT, Keys.INSERT)
            msg_box.send_keys(Keys.ENTER)
            sent = sent + 1
            w.get_screenshot_as_file(scriptdir+"screencaptures\\"+tosend+"_.png")
            print('\n - - - - - ['+str(sent)+'] - - - - Message sent to '+tosend+' - - - - - ')
            w.execute_script("window.close();")
            time.sleep(2)
            count = count + 1
            #time.sleep(1)
        else:
            f = open(scriptdir+"failed.txt", "a")
            f.write(tosend+'\n')
            f.close()
            print('\n - - - Number '+tosend+' is not on WhatsApp, skipping - - - ')
            count = count + 1
            
    else:
        #w.close()
        
        print('\n - - - - - - - - - Report:  '+str(sent)+'/'+str(lines)+' successful - - - - - - - - ')
        print('\n - - - - - - - - - Bye :) - - - - - - - - ')
       #print('\nSent messages to '+str(sent)+' numbers from '+str(lines)+' given numbers.')
        w.quit()
        time.sleep(5)
        sys.exit()

send()
