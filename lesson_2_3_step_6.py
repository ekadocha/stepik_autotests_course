from selenium import webdriver
import time
import math

# browser.switch_to.window(window_name) # переключение на новую вкладку
# new_window = browser.window_handles[1] # узнать имя новой (второй по счету из открытых) вкладки
# first_window = browser.window_handles[0] # запомнить имя текущей (первой по счету из открытых) вкладки, чтобы иметь возможность потом к ней вернуться

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element_by_id("input_value").text
answer = calc(int(x))

input = browser.find_element_by_id("answer")
input.send_keys(answer)

button = browser.find_element_by_css_selector("button.btn")
button.click()


time.sleep(15)
browser.close()
time.sleep(2)
browser.quit()