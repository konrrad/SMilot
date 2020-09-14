# SMILOT
#EN

### Aim
SMilot is a pilot for smart-home based on mqtt broker.

### Functionality

- [Usage example](https://drive.google.com/file/d/1aFaUPXSzoOxpYg3ZnmBuC_lZq8iicHMc/view?usp=sharingno do)

- SMilot publishes commands, that can be received by devices or other SMilots.
- Each working pilot is aware of real-time state of its devices.
- Pilot, that sent a command updates its state due to the message it sent to broker, i.e. its state is based on broker's state.
- When pilot X is terminated, it saves its state to file. That enables it to load the real state of its devices when started again.
- When pilot X is offline and other pilots publish commands, then pilot X will load the commands published when offline.


### Usage

Install mosquitto

`sudo apt install mosquitto`

`sudo apt install mosquitto-clients`

Start mosquitto

`mosquitto`

In a new terminalu:

`mosquitto_sub -v -t '#`

Start pilot with example config

`pip3 install pyqt5`

`python3 Window.py [plik_configu]`

On first start it is advised to calibrate the pilot.
One should set all devices to 0 both in the SMilot and in reality.
From now on, the devices will respond to the commands.

One can control the devices from SMilot and observe their real state in terminal with mosquitto_sub client.

Example command:

`mosquitto_pub -t 'home/Lazienka/Kranik' -m 11 --qos 2`



To start multiple instances of application, one should change the [client_name]( ./config.json ) in config file.

Two configs are provided so one can test concurrent workflow of application.


#PL

Projekt na Programowanie w języku Python.

### Cel

Celem projektu było stworzenie pilota do inteligentnego domu, którego działanie miało opierać
się na brokerze mqtt.

### Działanie

- [Przykładowe uruchomienie](https://drive.google.com/file/d/1aFaUPXSzoOxpYg3ZnmBuC_lZq8iicHMc/view?usp=sharingno do)

- Pilot publikuje polecenia, które mogą być odbierane przez urządzenia oraz inne piloty.
- Każdy uruchomiony w danym momencie pilot posiada faktyczny stan urządzeń.
- Pilot, z którego zostało wysłane polecenie aktualizuje swoje wskazania na podstawie wysłanej przez siebie wiadomości
do brokera, tzn. na podstawie subskrybcji danego tematu.
- Kiedy pilot X jest zamykany zapisuje swój stan w pliku, co pozwala przy ponownym uruchomieniu
wczytać realny stan urządzeń. 
- Kiedy pilot X jest offline a inne piloty publikują polecenia, wtedy pilot X
po uruchomieniu wczyta polecenia opublikowanie w czasie, gdy był offline.

### Budowa


#### [Klasa Device](Device/Device.py)
Struktura danych - reprezentuje urządzenie w programie.

#### [Klasa DeviceQWidget](GUI/DeviceQWidget.py)
Widok dla danego urządzenia.

#### [Klasa DeviceController](Device/DeviceController.py)
Zarządza urządzeniem oraz jego widokiem(aktualizuje wartości).

#### [Klasa NetworkClient](Network/NetworkClient.py)
Zarządza połączeniem z brokerem. Odbiera i wysyła polecenia.

#### [Klasa ConfigProvider](ConfigUtils/ConfigProvider.py)
Odczytuje config.

#### [Klasa ConfigTranslator](ConfigUtils/ConfigTranslator.py)
Przebudowuje strukturę zawartą w configu na obiekty programu.

#### [Klasa ControllerCreator](Builders/ControllerCreator.py)
Budowniczy dla DeviceController.

#### [Klasa ErrorHandler](GUI/ErrorHandler.py)
Wyświetla okno z komunikatem błędu.

#### [Klasa DeviceBuilder](Builders/DeviceBuilder.py)
Budowniczy dla Device.

#### [Klasa IdentifiedSlider](GUI/IdentifiedSlider.py)
Slider,który wie o swoim DeviceController.

#### [Klasa Window](./Window.py)
Główna klasa programu.


#### Pliki konfiguracyjne
Zawierają:
- nazwa klienta - musi być unikalna
- address - ip brokera
- port
- hasło do brokera
- tablica pokoi

Każdy pokój składa się z:
- nazwa pokoju - musi być unikalna
- tablica urządzeń

Struktura urzadzenia składa się z:
- nazwa urządzenia - musi być unikalna
- pole range 
    - true dla urządzeń mogących przyjmować stany od 0 do 100
    - false dla urządzeń przyjmujących stan włączony/wyłączony
- pole value - ostatnia znany stan urządzenia
- pole coordinates - topic w brokerze przypisany danemu urządzeniu


### Jak użyć

Instalacja mosquitto

`sudo apt install mosquitto`

`sudo apt install mosquitto-clients`

Uruchomienie mosquitto

`mosquitto`

W osobnym terminalu:

`mosquitto_sub -v -t '#`

Uruchomienie pilota z przykładowym configiem:

`pip3 install pyqt5`

`python3 Window.py [plik_configu]`

Przy pierwszym uruchomieniu warto zadbać, aby dane z configa były zgodne z realnymi.
Można np ustawić wszystkie urządzenia na 0 w pliku i w rzeczywistości. Od tej pory urządzenia będą poprawnie reagować na polecenia.

Teraz można wydawać polecenia za pomocą pilota i obserwować ich skutek w terminalu z klientem mosquitto_sub.

Przykładowe polecenie:

`mosquitto_pub -t 'home/Lazienka/Kranik' -m 11 --qos 2`


Aby uruchomić kilka pilotów należy uruchomić je z innym [client_name]( ./config.json ) w pliku konfiguracyjnym.

Dwa pliki konfiguracyjne są zapewnione po to,aby można było sprawdzić synchroniczne działanie dwóch różnych pilotów( dwóch instancji aplikacji ).
