import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.relative_locator import locate_with




options = Options()
options.binary_location = '/Users/asethi22/Library/Printers/Firefox.app/Contents/MacOS/firefox-bin'
service = Service(executable_path="/Users/asethi22/Library/Printers/drivers/geckodriver")


driver = webdriver.Firefox(service=service, options=options)

driver.get('https://www.instagram.com/')

driver.implicitly_wait(3)


username = driver.find_element(By.NAME, 'username')
username.send_keys('alulbalul15')

username = driver.find_element(By.NAME, 'password')
username.send_keys('akul06152003')

button_locator = locate_with(By.TAG_NAME, 'button').below({By.NAME: 'password'})

driver.find_element(button_locator).click()

try:
    time.sleep(2)
    driver.find_element(By.ID, 'advancedButton').click()
    time.sleep(2)
    driver.find_element(By.ID, 'exceptionDialogButton').click()
except:
    print('no warning')

driver.implicitly_wait(4)

search_locator = locate_with(By.TAG_NAME, 'input').above({By.CLASS_NAME: 'coreSpriteKeyhole'})
bar = driver.find_element(search_locator)
bar.send_keys('yoohoo_soohoo' + Keys.ENTER)


# driver.implicitly_wait(1)
driver.find_element(By.CLASS_NAME, '-qQT3').click()
# driver.implicitly_wait(5)


counter = 0
links = []
for i in range(125):
    
    for j in range(i):
        driver.execute_script("window.scrollTo(0, " + str(counter) + ");")
        counter += 900
        time.sleep(5)
 
    article = driver.find_element(By.TAG_NAME, 'article')
    links = article.find_element(By.TAG_NAME, 'div').find_element(By.TAG_NAME, 'div').find_elements(By.TAG_NAME, 'a')
    
    posts = []
    for link in links:
        posts.append(link.get_attribute('href'))

    
    for post in posts:
        driver.get(post)
        time.sleep(1)
        try:
            text = driver.find_element(By.CLASS_NAME, "MOdxS ").find_element(By.TAG_NAME, 'span').text

            with open('data1.txt', 'a') as f:
                f.write(text)
                f.write('\n')
        except:
            print('no caption')
     
    driver.get("https://www.instagram.com/yoohoo_soohoo")






       



# driver.quit()

# username = driver.find_element(By.)




