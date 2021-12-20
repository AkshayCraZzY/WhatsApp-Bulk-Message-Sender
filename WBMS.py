#import pyperclip

import time
import sys
import os
import os.path
import mmap
import warnings
import glob
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import urllib.parse
warnings.filterwarnings("ignore", category=DeprecationWarning)
start = time.time()
#scriptdir="M:\\WBMS\\"
link1="https://web.whatsapp.com/send?phone=91"
link2="&text="
img=[]
clear = lambda: os.system('cls')

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir="+os.path.join(sys.path[0])+"\\wbms\\User Data") 
options.add_argument("window-size=1080x720")
options.add_argument('log-level=3')
options.add_argument('disable-gpu')
options.add_argument('disable-infobars')
options.add_argument('disable-extensions')
options.add_argument('disable-dev-shm-usage')
#options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

msg_path=os.path.join(sys.path[0])+"\\PUT EVERYTHING HERE\\msg.txt"
num_path=os.path.join(sys.path[0])+"\\PUT EVERYTHING HERE\\num.txt"
log_path=os.path.join(sys.path[0])+"\\failed.log"
img_path=os.path.join(sys.path[0])+"\\PUT EVERYTHING HERE\\Images"
clear()
print("\n - - - - - - - - - - - - -STARTING - - - - - - - - - - - - -")
print(" - - - -Reading Numbers, Message and Images to send - - - - ")



for root, subdirs, files in os.walk(img_path):
    for file in files:
        if os.path.splitext(file)[1].lower() in ('.jpg', '.png'):
             img.append(file)
#print(img)


#sys.exit()
with open(msg_path,"r+") as file:
    msg = file.read()

send_msg=urllib.parse.quote_plus(msg)
#send_msg = msg.replace('\n', '%0A').replace('\r', '%0A')

if os.stat(num_path).st_size == 0 or os.stat(msg_path).st_size == 0:
    print('\n - - - - - -num.txt or msg.txt is empty, Exiting - - - - - -')
    sys.exit()

if len(img) > 3:
    print('\n - - - - - - Maximum 3 images allowed, Exiting - - - - - - -')
    sys.exit()
elif len(img) == 0:
    print('\n - - - - - - - - - - -No images found - - - - - - - - - - - ')
elif len(img):
    print(' - - - - - - - - - - - '+str(len(img))+' Images found - - - - - - - - - - - ')

f = open(num_path, "r+")
nums = f.readlines()
nums=  lines = [line.rstrip() for line in nums]
buf = mmap.mmap(f.fileno(), 0)
lines = 0
readline = buf.readline
while readline():
    lines += 1
print('\n - - - - - - '+str(lines)+' numbers found in num.txt, Starting- - - - - -')
print("\n - - - - - - - - - - - -Your Message - - - - - - - - - - - -")
print('"'+msg+'"')
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
'''
f = open(log_path, "a")
f.write('\n - - - - - - - Edited on '+datetime.fromtimestamp(datetime.timestamp(datetime.now())).strftime("%d %B %I:%M %p")+' - - - - - - - \n')
f.close()
'''

def send():
    count=0
    sent=0
    fail=0
    loadtime=0
    w = webdriver.Chrome(options=options)
    while (count < lines): 
        tosend = nums[count]
        if len(tosend) != 10:
            count = count + 1
            f = open(log_path, "a")
            f.write('\n'+tosend+' - '+str(len(tosend))+' digit number\n')
            f.close()
            fail=fail+1
            print('\n - - Number '+tosend+' is not a 10 digit number, skipping - - ')
            linkk='about:blank'
            continue
        else:
            linkk=link1+tosend+link2+send_msg#+'%F0%9F%98%80'
        w.get(linkk)
        try:
            w.find_element_by_class_name("_2UwZ_")#.click()
        except NoSuchElementException:
            print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        else:
            print(" - - -RE-LOGIN NEEDED, Scan QR code and restart script - - -")
        #print(" - - - - - - - - - -WhatsApp Web loaded - - - - - - - - - - ")
        search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
        WebDriverWait(w, 30).until(EC.presence_of_element_located((By.XPATH, search_xpath)))
        loadtime=loadtime+time.time()-start
        time.sleep(2)
        try:
            w.find_element_by_class_name('nne8e')
        except:
            msg_xpath = '//div[@contenteditable="true"][@data-tab="9"]'
            msg_box = WebDriverWait(w, 100).until(EC.presence_of_element_located((By.XPATH, msg_xpath)))
           # msg_box.click()
           # pyperclip.copy(msg)
           # msg_box.send_keys(Keys.SHIFT, Keys.INSERT)
            msg_box.send_keys(Keys.ENTER)
            sent = sent + 1
            w.get_screenshot_as_file(os.path.join(sys.path[0])+"\\ss\\"+tosend+"_msg.png")
            #print('\n - - - - - ['+str(sent)+'] - - - - Message sent to '+tosend+' - - - - - ')
            print('\n - - - - - - - - - Message sent to '+tosend+' - - - - - ['+str(sent)+']')
            for imgs in img:
                #print(imgs)
                tosend_img=img_path+'\\'+imgs
                #print(tosend_img)
                #sys.exit()
                attach_xpath='//div[@title="Attach"]'
                attach_btn = WebDriverWait(w, 2000).until(EC.presence_of_element_located((By.XPATH, attach_xpath)))
                #print("Attach Found")
                attach_btn.click()
                time.sleep(1)
                doc_xpath = '//span[@data-icon="attach-document"]'
                img_xpath = '//span[@data-icon="attach-image"]'
                send_xpath = '//span[@data-icon="send"]'
                #doc_btn = WebDriverWait(w, 2000).until(EC.presence_of_element_located((By.XPATH, doc_xpath)))
                #print("Doc Found")
                #doc_btn.click()
                #self.send_attachment()
                img_btn = WebDriverWait(w, 2000).until(EC.presence_of_element_located((By.XPATH, img_xpath)))
                #img_btn = w.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]')
                #img_btn.click()
                img_btn = w.find_element_by_tag_name('input')
                img_btn.send_keys(tosend_img)
                send_btn = WebDriverWait(w, 2000).until(EC.presence_of_element_located((By.XPATH, send_xpath)))
                send_btn.click()
                print(' - - - - - - - - - Image sent '+imgs+' - - - - - - - - - -')
                if imgs == img[-1]:
                    w.get_screenshot_as_file(os.path.join(sys.path[0])+"\\ss\\"+tosend+"_img.png")
                #time.sleep(2)

            w.execute_script("window.close();")
            time.sleep(2)
            count = count + 1
        else:
            f = open(log_path, "a")
            f.write('\n'+tosend+' - Not on whatsapp\n')
            f.close()
            time.sleep(1)
            w.get_screenshot_as_file(os.path.join(sys.path[0])+"\\ss\\"+tosend+"_fail.png")
            fail=fail+1
            print('\n - - - Number '+tosend+' is not on WhatsApp, skipping - - - ')
            count = count + 1
            
    else:
        #w.close()
        
        print('\n - - - - - - - - - Report:  '+str(sent)+'/'+str(lines)+' successful - - - - - - - - ')
        exectime="%0.2f" % (time.time()-start,)
        ldtime="%0.2f" % loadtime
        actual_exec=(time.time()-start)-loadtime
        act_exec = "%0.2f" % actual_exec
        #print(' - - - - - - - Task finished in '+exectime+' seconds - - - - - - - ')
        print(' - - - - - - - -WhatsApp Web load time: '+ldtime+' s- - - - - - - ')
        #print(' - - - - - - - - - - - - - - - - - - -  + ')
        print(' - - - - - - - -Actual execution time: '+act_exec+' s- - - - - - - -')
        print(' - - - - - - - -Total execution time: '+exectime+' s- - - - - - - -')
       #print('\n - - - - - - - - - - - - - Bye :) - - - - - - - - - - - - - ')
        w.quit()
        if fail==1:
            os.startfile(log_path)
        print("\n - - - - - - WBMS - WhatsApp Bulk Message Sender - - - - - -")
        print(" - - - - - - - - - Github.com/AkshayCraZzY - - - - - - - - -")
        time.sleep(10)
        sys.exit()


send()
