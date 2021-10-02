from selenium import webdriver
from selenium.webdriver.chrome.options import Options

user_input = "gmm"
options = Options()
options.headless = True
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver_path = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=driver_path)
driver.get(f'https://www.youtube.com/results?search_query={user_input}')

channel_name = driver.find_element_by_id("channel-title").click()
url = f"{driver.current_url}/videos"

print(url)