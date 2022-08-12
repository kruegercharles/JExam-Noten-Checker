## JExam Noten Checker
Dieses Programm ist für JExam von der TU Dresden.

Leider ist JExam unnötig kompliziert. Man muss sich erst einloggen und dann zu den Prüfungsergebnissen navigieren. 
Und da es keine automatische Benachrichtigung für neue Prüfungsergebnisse gibt, muss man das immer und immer wieder machen.

Dieses Tool loggt den Nutzer automatisch bei JExam ein, navigiert zu den Prüfungsergebnissen, wartet 10 Sekunden (das kann natürlich geändert werden), loggt den Nutzer wieder aus und schließt dann das Fenster.
So kann man schnell überprüfen, ob es neue Noten gibt. 

Zudem wurde der Zoom standardmäßig auf 80% gesetzt, um eine bessere Übersicht zu haben. 


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

## Aber ich tippe meine Nutzerdaten doch nicht in irgendein Random-Skript auf Github!
Sehr vernünftig, würde ich auch nicht machen!

Das ist eine super Gelegenheit, um sich mit Selenium vertraut zu machen. 
Und da das Skript relativ einfach ist, kann man schnell verstehen, was jeder einzelne Befehl macht, sodass man mir nicht vertrauen muss. 

Ich empfehle dieses Einführungs-Tutorial für Selenium: https://www.youtube.com/watch?v=Xjv1sY630Uc

Achtung: Die Syntax hat sich geringfügig geändert, aber im Großen und Ganzen ist das Tutorial noch aktuell. 

Auch nützlich:
- die Selenium Dokumenation: https://www.selenium.dev/documentation/overview/
- Selenium IDE für Chrome: https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd

## Bekannte Fehler
Wenn man die standardmäßig 10 Sekunden nicht wartet, bis das Skript den Nutzer ausloggt (oder man aus irgendeinem anderen Grund nicht ausgeloggt wird), aber man das Skript direkt danach neustartet, dann kann es passieren, dass man folgende Fehlermeldung erhält "Du bist schon woanders angemeldet".

In dem Fall kann man nur überprüfen, ob man irgendwo noch ein Fenster offen hat, bei dem man angemeldet ist. 
Ansonsten kann man nur warten, bis man vom Server automatisch ausgeloggt wird, damit das Skript wieder ordnungsgemäß funktioniert. 

## TO DO
- Keys in eine .env-Datei auslagern
- Statt pip Poetry oder Pipenv nutzen
- Herunterladen vom Chromedriver automatisieren