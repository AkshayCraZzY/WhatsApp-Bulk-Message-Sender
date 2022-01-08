<p align="center">
 <a href="https://github.com/AkshayCraZzY/WhatsApp-Bulk-Message-Sender">
 <img width="250px" src="https://i.imgur.com/555Zl4p.png" align="center" alt="MargAuto" /></a>
 <h3 align="center"><a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://c.tenor.com/3MtdCRIPZUMAAAAi/whatsapp.gif" width="20px"></a> WhatsApp Bulk Message Sender - WBMS</h3></a>
</p>

$$\      $$\ $$\                  $$\
$$ | $\  $$ |$$ |                 $$ |
$$ |$$$\ $$ |$$$$$$$\   $$$$$$\ $$$$$$\    $$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$\
$$ $$ $$\$$ |$$  __$$\  \____$$\\_$$  _|  $$  _____| \____$$\ $$  __$$\ $$  __$$\
$$$$  _$$$$ |$$ |  $$ | $$$$$$$ | $$ |    \$$$$$$\   $$$$$$$ |$$ /  $$ |$$ /  $$ |
$$$  / \$$$ |$$ |  $$ |$$  __$$ | $$ |$$\  \____$$\ $$  __$$ |$$ |  $$ |$$ |  $$ |
$$  /   \$$ |$$ |  $$ |\$$$$$$$ | \$$$$  |$$$$$$$  |\$$$$$$$ |$$$$$$$  |$$$$$$$  |
\__/     \__|\__|  \__| \_______|  \____/ \_______/  \_______|$$  ____/ $$  ____/
                                                              $$ |      $$ |
                                                              $$ |      $$ |
                                                              \__|      \__|
<h3 align="center">WBMS automates sending of message to multiple numbers via WhatsApp Web. <br/> </h3>
<br/>
<p align="center">
<a href="https://github.com/AkshayCraZzY/WhatsApp-Bulk-Message-Sender">
      <img src="https://img.shields.io/badge/Login%20Info-saves-orange?style=for-the-badge"/>
 </a>
<a href="https://github.com/AkshayCraZzY/WhatsApp-Bulk-Message-Sender">
    <img src="https://img.shields.io/badge/Unsaved%20contacts-works-blue?style=for-the-badge">
</a>
<a href="https://github.com/AkshayCraZzY/WhatsApp-Bulk-Message-Sender">
    <img src="https://img.shields.io/github/last-commit/akshaycrazzy/WhatsApp-Bulk-Message-Sender?style=for-the-badge">
</a>
<br/>
<a href="https://github.com/AkshayCraZzY/WhatsApp-Bulk-Message-Sender">
      <img src="https://img.shields.io/badge/Selenium--ChromeDriver-8b1616?style=for-the-badge"/>
 </a>
<br/>
<a href="https://github.com/AkshayCraZzY/WhatsApp-Bulk-Message-Sender/issues/new/choose">Report Bug</a>
·
<a href="https://github.com/AkshayCraZzY/WhatsApp-Bulk-Message-Sender/issues/new/choose">Request Feature</a>
  </p>
</p>
<p align="center">Love the project? Please consider staring it!
<br/>
<br/>

## 👁‍🗨 Why choose WBMS over others?

- Scan QR code only once, It creates and uses separate user data for chrome to keep you logged in.

- It works even if you don't have the numbers saved in your contacts.

- Stores a screenshot right after sending a message for verification. 

- It skips invalid/number which doesn't have a WhatsApp account. 

- Works on a single browser window even when using multiple wa.me links.
 
- Stores failed / invalid numbers in a file for debugging later.
<br/>
<br/>   

# 🚀 Installation :

## Install Selenium 
 
  Using [pip](https://pypi.org/project/selenium/)
  ```
  pip install selenium
  ```

## Download and setup Chrome Webdriver
 
For checking chrome version :
```
chrome://version
```

- Download according to your chrome version from [HERE](https://sites.google.com/chromium.org/driver/downloads?authuser=0)
 
 - Add ChromeDriver to your PATH (System variable)  [HERE](https://zwbetz.com/download-chromedriver-binary-and-add-to-your-path-for-automated-functional-testing/#windows-gui)

To verify chromedriver installation run on CMD : 
```
chromedriver.exe -v
```
## Changes in the Code
In a new folder, place ```main.py``` and create ```num.txt```, ```msg.txt``` <br/>
Find this line and replace with path of your newly created folder.<br/>
```python
scriptdir='C:\\Users\\aksha\\Documents\\WBMS\\'
```

For example : ```scriptdir='C:\\coding\\WBMS\\'```

# ⚡ Usage :
- In ```msg.txt``` add the message you wish to send.
- In ```num.txt``` add 10 digit phone numbers line wise (Don't include country code)
For Example : 
```
9876543210
9123456789
```
Run main.py
```
python main.py
```
*At first run you will get whatsapp QR code Login window. After logging in succesfully restart the script. It should now be already loged in.*<br/>

All important messages will be shown on the console window.

# 📸 Screenshots / Working with Example:
* <h3 align="left">Contents of num.txt :</h3>

  - 1st number is a 8 digit number ***(Invalid)*** <br/>
  - 2nd number is a ***(Valid)*** number<br/>
  - 3rd number is not on whatsapp ***(Invalid)***

<p align="center"><a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img width="70%" height="auto" src="https://raw.githubusercontent.com/AkshayCraZzY/WhatsApp-Bulk-Message-Sender/main/screenshots/nums.JPG" height="175px"/></a></p>

* <h3 align="left">Contents of msg.txt :</h3>

<p align="center"><a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img width="70%" height="auto" src="https://raw.githubusercontent.com/AkshayCraZzY/WhatsApp-Bulk-Message-Sender/main/screenshots/msg.JPG" height="175px"/></a></p> 

* <h3 align="left">After Running main.py</h3>

<p align="center"><a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img width="70%" height="auto" src="https://raw.githubusercontent.com/AkshayCraZzY/WhatsApp-Bulk-Message-Sender/main/screenshots/1.jpg" height="175px"/></a></p> 

* <h3 align="left">Output</h3>

<p align="center"><a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img width="70%" height="auto" src="https://raw.githubusercontent.com/AkshayCraZzY/WhatsApp-Bulk-Message-Sender/main/screenshots/2.JPG" height="175px"/></a></p> 




# 💬 Connect with me
<p align="left">
<a href = "mailto:akshayparakh98@gmail.com"><img src="https://img.icons8.com/fluent/48/000000/mail.png"/></a>
<a href = "https://www.linkedin.com/in/akshayparakh98/"><img src="https://img.icons8.com/fluent/48/000000/linkedin.png"/></a>
<a href = "https://twitter.com/akshayparakh98"><img src="https://img.icons8.com/fluent/48/000000/twitter.png"/></a>
<a href = "https://www.instagram.com/akki_parakh/"><img src="https://img.icons8.com/fluent/48/000000/instagram-new.png"/></a>
<a href = "https://www.youtube.com/crazzyak"><img src="https://img.icons8.com/color/48/000000/youtube-play.png"/></a>

</p>

# 👁‍🗨 My Views and Followers
<a href="https://github.com/akshaycrazzy/">
    <img src="https://komarev.com/ghpvc/?username=antonkomarev&color=brightgreen&style=flat-square">
</a>
<a href="https://github.com/akshaycrazzy?tab=followers"><img src="https://img.shields.io/github/followers/akshaycrazzy?label=Followers&style=social" alt="GitHub Badge"></a>

<br/>
<br/>

# 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [repositories page](https://github.com/akshaycrazzy?tab=repositories).
<br/>
<br/>

# ⭐️ Show your support

Give a ⭐️ if this project helped you!
<br/>
<br/>

# 📝 License

Copyright © 2022 [Akshay Parakh](https://github.com/AkshayCraZzY).<br />
This project is [Apache License 2.0](https://github.com/AkshayCraZzY/WhatsApp-Bulk-Message-Sender/blob/main/LICENSE) licensed.
