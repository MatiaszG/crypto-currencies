# crypto-currencies

Projekt jest napisany w języku Python przy pomocy frameworka django.
Realizuje on stronę internetową, przedstawiającą dane na temat kryptowalut, pobrane przez API strony https://www.coingecko.com/.
Dane o kryptowalutach są aktualizowane na bieżąco, przy pomocy protokołu websocket.
Dzięki cyklicznie odczytywanym danym z serwisu coingecko, strona buduje dla użytkownika w czasie rzeczywistym wykresy cen kryptowalut.
Strona zawiera także funkcjonalnośc odpowiadającą za konwersję kryptowalut. Funkcjonalność ta również bazuje na API serwisu https://www.coingecko.com/.
Przed uruchomieniem projektu należy zainstalować moduły takie jak django, requests oraz channels.

Aby uruchomić projekt, należy uruchomić serwer korzystając z polecenia
```
python manage.py runserver
```
będąc w folderze project w którym znajduje się plik manage.py.
Następnie nalezy połączyć się z poziomu przeglądarki z adresem wyświetlonym w konsoli.

