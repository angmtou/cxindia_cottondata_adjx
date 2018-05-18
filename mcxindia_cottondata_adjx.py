# coding:utf-8
from selenium import webdriver
import time
import pandas as pd

user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
)

# 进入浏览器设置
options = webdriver.ChromeOptions()
# 设置中文
# options.add_argument('lang=zh_CN.UTF-8')
options.add_argument("--headless")

# 更换头部
# options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
# feeds_crawler = webdriver.Chrome(chrome_options=options)

# feeds_crawler.set_window_size(1920, 1200)  # optional
driver = webdriver.Chrome(chrome_options=options)
driver.set_window_size(1920, 1200)  # optional
url_home = "https://www.mcxindia.com/market-data/market-watch"
driver.get(url_home)
# time.sleep(18)
driver.implicitly_wait(20)

driver.find_element_by_id('ctl00_cph_InnerContainerRight_C005_ddlSymbols1_Input').clear()
driver.find_element_by_id('ctl00_cph_InnerContainerRight_C005_ddlSymbols1_Input').send_keys('COTTON')
# 移动到show按钮
driver.find_element_by_id("btnShow").click()

ht1=driver.page_source
t1=pd.read_html(ht1)

res=t1[3].copy()
# print (res.dtypes)
print  (res.iloc[:,[1,2,5,8,10,11,12,13,14,15]])