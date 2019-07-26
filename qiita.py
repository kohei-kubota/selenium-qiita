from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://qiita.com/')

driver.find_element_by_css_selector('a.nl-SocialSignup.nl-SocialSignup-github').click()

driver.find_element_by_id('login_field').send_keys('{}')

driver.find_element_by_id('password').send_keys('{}')

driver.find_element_by_css_selector('input.btn-block').click()

# sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[3]/div[6]/div/div[2]/div/div[1]/div[2]/a').click()

sleep(1)

tag = {}

for i in range(3):
    sleep(1)
    elements = driver.find_elements_by_css_selector('a.tsf-ArticleBody_tag')

    for element in elements:
        # print(element.text)
        if element.text in tag:
            tag[element.text] += 1
        else:
            tag[element.text] = 1

    sleep(1)
    driver.find_element_by_css_selector('li.st-Pager_next>a.st-Pager_link').click()
    # driver.refresh()

# print(tag)
with open('result.csv', 'w') as f:
    for key, val in tag.items():
        f.write('"'+key+'",'+str(val)+"\n")
