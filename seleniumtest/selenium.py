from selenium import webdriver

chromedriver = "/Users/junyuliu/Downloads/chromedriver"
driver = webdriver.Chrome(chromedriver)
#driver.get("http://stackoverflow.com")

# driver = webdriver.PhantomJS()
driver.get('https://www.douban.com/')
driver.implicitly_wait(5)
# iframe = driver.find_elements_by_tag_name('iframe')[1]
driver.switch_to.frame(0)
driver.find_element_by_xpath('//ul[@class="tab-start"]/li[2]').click()
driver.find_element_by_xpath('//*[@id="username"]').clear()
driver.find_element_by_xpath('//*[@id="username"]').send_keys('645541948@qq.com')
driver.find_element_by_xpath('//*[@id="password"]').clear()
driver.find_element_by_xpath('//*[@id="password"]').send_keys('jy8186102oa')
driver.find_element_by_xpath('//*[@id="tmpl_phone"]/div[5]/a').click()
# print(driver.page_source)
# with open('hello.html', 'w', encoding='utf-8') as f:
#     f.write(driver.page_source)
