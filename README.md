#SMILOT

Projekt na Programowanie w języku Python.

###Cel

Celem projektu było stworzenie pilota do inteligentnego domu, którego działanie miało opierać
się na brokerze mqtt.

###Działanie

Pilot publikuje polecenia, które mogą być odbierane przez urządzenia oraz inne piloty,
co sprawia, że każdy uruchomiony w danym momencie pilot posiada faktyczny stan urządzeń.
Ponadto kiedy pilot X jest zamykany zapisuje swój stan w pliku, co pozwala przy ponownym uruchomieniu
wczytać realny stan urządzeń. Kiedy pilot X jest offline a inne piloty publikują polecenia, wtedy pilot X
po uruchomieniu wczyta polecenia opublikowanie w czasie, gdy był offline.

###Budowa


####[Klasa Device](./Device.py)
Struktura danych - reprezentuje urządzenie w programie.

####[Klasa DeviceQWidget](./DeviceQWidget.py)
Widok dla danego urządzenia.

####[Klasa DeviceController](./DeviceController.py)
Zarządza urządzeniem oraz jego widokiem(aktualizuje wartości).

####[Klasa NetworkClient](./NetworkClient.py)
Zarządza połączeniem z brokerem. Odbiera i wysyła polecenia.

####[Klasa ConfigProvider](./ConfigProvider.py)
Odczytuje config.

####[Klasa ConfigTranslator](./ConfigTranslator.py)
Przebudowuje strukturę zawartą w configu na obiekty programu.

####[Klasa ControllerCreator](./ControllerCreator.py)
Budowniczy dla DeviceController.

####[Klasa ErrorHandler](./ErrorHandler.py)
Wyświetla okno z komunikatem błędu.

####[Klasa DeviceBuilder](./DeviceBuilder.py)
Budowniczy dla Device.

####[Klasa IdentifiedSlider](./IdentifiedSlider.py)
Slider,który wie o swoim DeviceController.

####[Klasa Window](./Window.py)
Główna klasa programu.


###Jak użyć

Instalacja mosquitto

`sudo apt install mosquitto`

`sudo apt install mosquitto-clients`

Uruchomienie mosquitto

`mosquitto`

W osobnym terminalu:

`mosquitto_sub -v -t '#`

Uruchomienie pilota z przykładowym configiem:

`python3 Window.py [plik_configu]`

Przy pierwszym uruchomieniu warto zadbać, aby dane z configa były zgodne z realnymi.
Można np ustawić wszystkie urządzenia na 0 w pliku i w rzeczywistości. Od tej pory urządzenia będą poprawnie reagować na polecenia.

Teraz można wydawać polecenia za pomocą pilota i obserwować ich skutek w terminalu z klientem mosquitto_sub.

Aby uruchomić kilka pilotów należy uruchomić je z innym [client_name]( ./config.json ) w pliku konfiguracyjnym.

Dwa pliki konfiguracyjne są zapewnione po to,aby można było sprawdzić synchroniczne działanie dwóch różnych pilotów( dwóch instancji aplikacji ).
