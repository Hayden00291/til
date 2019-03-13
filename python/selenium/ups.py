from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

# 発送元
from_dict = {}
# 国についてはセレクタで選ばせる
from_dict['country'] = "JP"
from_dict['postal_code'] = "2850845"
from_dict['city'] = "千葉"

# 発送先
to_dict = {}
# 国についてはセレクタで選ばせる
to_dict['country'] = "AU"
to_dict['postal_code'] = "2600"
to_dict['city'] = "Canberra A.C.T."

# 貨物情報
package_dict = {}
package_dict['weight'] = '10'
package_dict['type'] = '02'
package_dict['total_price'] = '10000'

options = ChromeOptions()
# options.add_argument('--headless')
# driver = Chrome(options=options,
# executable_path='./chromedriver37.exe')

driver = Chrome(executable_path='./chromedriver37.exe')
driver.get('https://www.ups.com/mobile/ratetnthome?loc=ja_JP')

# 発送元情報セット
# 発送元国
from_country = driver.find_element_by_id('orig_Country')
Select(from_country).select_by_value(from_dict['country'])
# 発送元郵便番号
from_postalcode = driver.find_element_by_id('orig_PostalCode')
from_postalcode.send_keys(from_dict['postal_code'])
# 発送元都市
from_city = driver.find_element_by_id('orig_City')
from_city.send_keys(from_dict['city'])

# 宛先情報セット
# 宛先国
to_country = driver.find_element_by_id('dest_Country')
Select(to_country).select_by_value(to_dict['country'])
# 宛先郵便番号
to_postalcode = driver.find_element_by_id('dest_PostalCode')
to_postalcode.send_keys(to_dict['postal_code'])
# 宛先都市
to_city = driver.find_element_by_id('dest_City')
to_city.send_keys(to_dict['city'])

# 貨物情報セット
# 梱包タイプ
package_type = driver.find_element_by_id('packageType')
Select(package_type).select_by_value('02')
# 重量
package_weight = driver.find_element_by_id('packageWeight')
package_weight.send_keys(package_dict['weight'])
# 関税評価額
customs_value = driver.find_element_by_id('customs-value')
customs_value.send_keys(package_dict['total_price'])

# スクレイピングお作法
sleep(1)

# 見積もり実行
submit_btn = driver.find_element_by_id('quote_country_btn')
submit_btn.click()

# 結果を取得、コンソールに表示
results = driver.find_elements_by_class_name('list-group-item')

for item in results:
    print(item.text)
    print('')

driver.quit()
