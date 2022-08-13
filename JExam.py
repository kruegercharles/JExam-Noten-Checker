from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# ========== Settings eintragen ==========
PATH = " Pfad " # Pfad für Chromedriver eintragen, z.B. "C:/Program Files (x86)/chromedriver.exe" oder "/Users/MaxMustermann/chromedriver"
USER = " Username " # Nutzernamen eintragen
PASS = " Password " # Passwort eintragen


driver = webdriver.Chrome(PATH)
driver.implicitly_wait(10) # Wartet, bis Elemente geladen sind; muss nur einmal gesetzt werden

# Window size
driver.set_window_position(0,0)
driver.maximize_window()

driver.get("https://jexam.inf.tu-dresden.de/de.jexam.web.v5/spring/welcome")

try:

    # Login
    login = driver.find_element(By.ID, "username").send_keys(USER) # Gibt Usernamen ein
    password = driver.find_element(By.ID, "password")
    password.send_keys(PASS) # Gibt Passwort ein
    password.send_keys(Keys.RETURN)



    # Navigiert durch Menüs zu Klausurergebnissen
    driver.find_element(By.XPATH, "//div[@id=\'wrapper\']/div/div/div[2]/a[3]/span").click()
    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".fill-primary:nth-child(2)").click()

    driver.execute_script("document.body.style.zoom = '80%';") # zoomt auf 80% heraus

    time.sleep(10) # wartet 10 Sekunden

    driver.execute_script("window.scrollTo(0, 0)") # scrollt nach oben für logout

    # Logout

    driver.find_element(By.LINK_TEXT, "Abmelden").click()

finally:
    driver.delete_all_cookies()
    driver.quit() # Schließt Browserfenster