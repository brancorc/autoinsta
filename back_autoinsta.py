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

extensiones_imagen= [".jpg", ".png", ".gif", ".thiff", ".heif", ".webp", ".jpeg" ]
extensiones_video= [".ogm",  ".mwn", ".mpg", ".webm", ".ogv", ".mov", ".asx", ".mpeg", ".mp4", ".m4v", ".avi"]

def click_path(path):

	try:

	    element = WebDriverWait(driver, 100).until(
	        EC.presence_of_element_located((By.XPATH, path))
	    )

	finally:
		
		driver.find_element(By.XPATH, path).click()
		time.sleep(1)


def send_path(path, key):

	try:

	    element = WebDriverWait(driver, 100).until(                            
	        EC.presence_of_element_located((By.XPATH, path))
	    )

	finally:
		
		
		driver.find_element(By.XPATH, path).send_keys(key)
		time.sleep(1)


class autoinsta():

	def __init__(self, username, password):  #inicia sesión

		driver.get("https://business.facebook.com/latest/content_calendar?asset_id=105669625640630&nav_ref=bm_home_redirect")

		send_path('//*[@id="email"]', username)

		send_path('//*[@id="pass"]', password)

		click_path('//*[@id="loginbutton"]')

	def programar_publicacion(self, fecha, hora, minuto, sistema_horario, descripcion, archivo):

		click_path('/html/body/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div/span/div/div[2]/div/div') #flecha para publicar

		click_path('/html/body/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div') #crear publicacion

# DE ACA PARA ABAJO AJUSTA LA PROGRAMACION

		# click_path("/html/body/div[4]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div")

		# input_fecha = driver.find_elements(By.XPATH , "/html/body/div[4]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div/input")

		# input_fecha[0].send_keys(Keys.CONTROL + "a")
		# input_fecha[0].send_keys(Keys.DELETE)

		# send_path("/html/body/div[4]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div/input", fecha)

		# time.sleep(1)

		# send_path("/html/body/div[4]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div[1]/div/input", hora)

		# send_path("/html/body/div[4]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div/input", minuto)

		# send_path("/html/body/div[4]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div/input", sistema_horario)

		# click_path("/html/body/div[4]/div[1]/div[1]/div/div/div/div/div[3]/div/div[2]/div/span/div/div/div")

#DE ACA PARA  ARRIBA AJUSTA LA PROGRAMACION

		time.sleep(10) #cambiar esto por uno mejor, seguir intentando si puedo meter la imagen y, de no ser asi, probar entrando a programar publicaciones desde otro lado

		click_path("/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/label/div/div/div[1]/div[1]/div/div[1]/input") #activa instagram

		click_path("/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div/div/label/div/div/div[1]/div[1]/div/div[1]/input") #desactiva facebook

		send_path("/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div/div/div/div/div/div/div", descripcion) #pone la descripcion


		for i in extensiones_imagen:

			if i in archivo:

				print("ENTRO EN EL IF I IN ARCHIVO")

				send_path("/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[5]/div[1]/div/a", archivo)
				send_path("/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[5]/div[1]/div/a", archivo)




ejecutar_bot=autoinsta(nombre, contraseña)

ejecutar_bot.programar_publicacion("11/10/2022", 4, 20, "p", "imagen de prueba bro", "C:/Users/branc/OneDrive/Escritorio/autoinsta/meme.jpg")

