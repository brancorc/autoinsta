from xml.etree.ElementTree import QName
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

service = Service(executable_path="chromedriver.exe")

opciones=Options()

opciones.add_experimental_option("prefs", {
	"profile.default_content_setting_values.notifications" : 2
	})

driver = webdriver.Chrome(chrome_options=opciones, service=service)

nombre="momoskratos"
contraseña="1622378459rcxd"

def click_path(path):

	try:

	    element = WebDriverWait(driver, 100).until(
	        EC.presence_of_element_located((By.XPATH, path))
	    )

	finally:
		time.sleep(1)
		driver.find_element(By.XPATH, path).click()


def send_path(path, key):

	try:

	    element = WebDriverWait(driver, 100).until(                            
	        EC.presence_of_element_located((By.XPATH, path))
	    )

	finally:
		
		time.sleep(1)
		driver.find_element(By.XPATH, path).send_keys(key)


class autoinsta():

	def __init__(self, username, password):  #inicia sesión

		driver.get("https://business.facebook.com/latest/content_calendar?asset_id=105669625640630&nav_ref=bm_home_redirect")

		send_path('//*[@id="email"]', username)

		send_path('//*[@id="pass"]', password)

		click_path('//*[@id="loginbutton"]')

	def programar_publicacion(self, fecha, hora):

		click_path('/html/body/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div') 

		click_path('/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div') 
	
		send_path("/html/body/div[4]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div/input", fecha)
creo que seleccionar el input desde otro xpath seria buena opcion para el clear

		# click_path("/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/label/div/div/div[1]/div[1]/div/div[1]/input")

		# click_path("/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div/div/label/div/div/div[1]/div[1]/div/div[1]/input")


ejecutar_bot=autoinsta(nombre, contraseña)

ejecutar_bot.programar_publicacion("6/10/2022", "13:30")

