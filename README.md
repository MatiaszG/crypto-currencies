# crypto-currencies

Projekt jest napisany w języku Python przy pomocy frameworka django.
Realizuje on stronę internetową, przedstawiającą dane na temat kryptowalut, pobrane przez API strony https://www.coingecko.com/.
Dane o kryptowalutach są bieżąco aktualizowane przy pomocy protokołu websocket.
Dzięcki cyklicznie odczytywanym danym z serwisu coingecko, strona buduje dla użytkownika w czasie rzeczywistym wykresy zmian cen kryptowalut.

Aby uruchomić projekt, należy uruchomić serwer korzystając z polecenia
'''
python manage.py runserver
'''
w folderze project w którym znajduje się plik manage.py.
Następnie nalezy połączyć się z poziomu przeglądarki z adresem wyświetlonym w konsoli.

