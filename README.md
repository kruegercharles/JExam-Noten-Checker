## JExam Noten Checker
Dieses Programm ist für JExam von der TU Dresden. 
Gebaut mit Selenium und Python. 

Leider ist JExam unnötig kompliziert. Man muss sich erst einloggen und dann zu den Prüfungsergebnissen navigieren. 
Und da es keine automatische Benachrichtigung für neue Prüfungsergebnisse gibt, muss man das immer und immer wieder machen.

Dieses Tool loggt den Nutzer automatisch bei JExam ein, navigiert zu den Prüfungsergebnissen, wartet 10 Sekunden (das kann natürlich geändert werden), loggt den Nutzer wieder aus und schließt dann das Fenster.
So kann man schnell überprüfen, ob es neue Noten gibt. 

Zudem wurde der Zoom standardmäßig auf 80% gesetzt, um eine bessere Übersicht zu ermöglichen. 


## Installation
### Schritt 1
Selenium installieren - `pip install selenium`

### Schritt 2
Chromedriver runterladen: https://chromedriver.chromium.org/downloads

Achtung: 

Die Version vom Chromedriver muss zur Version von Chrome passen, die man installiert hat. 

D.h. vorher checken, welche Chrome-Version man hat und den entsprechenden Chrome-Driver herunterladen. 

Alternativ könnte man auch den Driver für Firefox, Brave, Safari etc. nutzen, aber damit wurde das Skript nicht getestet. 

Außerdem müsste man dann die Zeile `driver = webdriver.Chrome(PATH)` anpassen. 

### Schritt 3
Chromedriver irgendwo speichern, wo man ihn später leicht wiederfindet, da man den Pfad später braucht

### Schritt 4
Python-Skript herunterladen und Settings ausfüllen, d.h. Username, Password und Pfad zum Chromedriver eintragen. 

Und dann einfach das Skript ausführen.

## Nützlich
- Selenium Dokumenation: https://www.selenium.dev/documentation/overview/
- Selenium IDE für Chrome: https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd

## Bekannte Fehler
Wenn man das Skript mehrfach innerhalb einer gewissen Zeitspanne (z.B. 10 Minuten) ausführt, dann bekommt man einen Fehler beim Login, dass man schon eingeloggt sei - obwohl man am Ende von dem Skript eigentlich ausgeloggt wird.

Mir ist noch nicht ganz klar, warum das passiert.

Einzige Lösung bis jetzt: kurz abwarten. 

## Mögliche Verbesserungen
- Keys in eine .env-Datei auslagern
- Statt pip Poetry oder Pipenv nutzen
- Herunterladen vom Chromedriver automatisieren
