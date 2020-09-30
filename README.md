# Come replicare la graduatoria di Medicina

***Si avvisa che non è consentito riprodurre in qualsiasi forma e trasmettere a terzi, pubblicare nel web, nei social forum, blog e analoghi strumenti informatizzati a immediata diffusione, la graduatoria nazionale visionabile, sia per intero che per parti di essa.
Le pubblicazioni su siti internet o altri mezzi di divulgazione di tali dati sono soggette a informativa alle autorità competenti per individuare eventuali illeciti relativi a tali diffusioni e punire gli autori ai sensi dell'art. 167 del codice della privacy***

***Le informazioni in questa guida sono esclusivamente a scopo puramente illustrativo***

È necessario avere l'accesso al sito Universitaly ed essere iscritto al test di cui si vuole replicare la graduatoria.

Si può utilizzare python per scaricare tutte le schede della graduatoria e poi tramite beautifulsoup ricostruire la graduatoria. Il modo più semplice è quello di estrarre le singole tabelle da ogni pagina e concatenarle su un'unica pagina html. Un modo più efficente ma più difficile da eseguire è estrarre tutte le singole righe e inserirle in un dataframe.

# A cosa serve?
La graduatoria nazionale è difficile da scorrere essendo divisa in circa 400 pagine, ed è difficile tramite il sito cercare dei nomi.
La graduatoria riprodotta è ad unica pagina e per questo è possibile trovare qualsiasi nome facilmente.

# Installare Python
<https://www.python.org/downloads/>

Consigliati:

<https://www.anaconda.com/products/individual>

<https://www.jetbrains.com/pycharm/>

# Indice
1. [Download delle schede](Download-delle-schede)
2. [Estrazione della graduatoria](Estrazione-della-graduatoria)

# SCRIPTS
1. [SCRIPT 1](SCRIPT-1)
2. [SCRIPT 2](SCRIPT-2)


# Download delle schede

1. Recarsi sul sito di Universitaly.it
2. Entrare nella pagina di login
3. Prima di inserire i dati, premere F12 (ispeziona elemento) e posizionarsi nella scheda rete
4. Cancellare i contenuti della scheda rete se presenti
![](/first_login.png)
5. Inserire le credenziali e premere "Entra"
6. A lato cliccare col tasto destro su "login", "Copia", "Copia come cURL (Bash)"
![](/login_data.png)
7. Recarsi sul sito <https://curl.trillworks.com/>, incollare nel box "curl command"
8. Copiare il testo nel box "Python requests" in uno script python. Il codice dovrebbe essere qualcosa di simile a:
```python
import requests
cookies = {
    '__utma': '...',
    '__utmc': '...',
    ...
}
headers = {
    'Connection': '...',
    ...
}
data = {
  'email-log': 'YOUR EMAIL',
  'password': 'YOUR PASSWORD',
  'query_string': '...',
  'login': '1^',
  'azione': 'Entra'
}
s = requests.Session()
s.post('https://www.universitaly.it/index.php/login', headers=headers, cookies=cookies, data=data)
```
Non dovete modificare nessun campo dei vari dizionari.
Tuttavia pare che il sito faccia un doppio login quindi dovremo aggiungere ancora qualche riga
9. Comportiamoci come dei veri umani e visitiamo la dashboard dopo il login
```python
s.get('https://www.universitaly.it/index.php/dashboard')
```
10. In alto a destra nel sito di Universitaly clicchiamo sulla freccetta di fianco al nostro nome e entriamo nell'area riservata
11. Prima di cliccare su "Vai alla tua Area Riservata...", premere F12 (ispeziona elemento) e posizionarsi nella scheda rete
12. Cancellare i contenuti della scheda rete se presenti
13. Cliccare su "Vai alla tua Area Riservata..."
![](/reserved.png)
14. A lato cliccare col tasto destro su "autenticazione.php?SESSION=...", "Copia", "Copia come cURL (Bash)"
![](/second_login.png)
15. Recarsi sul sito <https://curl.trillworks.com/>, incollare nel box "curl command"
16. Copiare il testo nel box "Python requests" nello script python che abbiamo creato prima. Il codice dovrebbe essere qualcosa di simile a:
```python
import requests
cookies = {
    '...': '...',
}
headers = {
    'Connection': '...',
    ...
}
params = (
    ('SESSION', '...'),
    ('user', '...'),
)
response = requests.get('https://accessoprogrammato.cineca.it/2020/studenti/autenticazione.php', headers=headers, params=params, cookies=cookies)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('...', headers=headers, cookies=cookies)
```
17. Rimuoviamo l'import che è stato già effettuato in precedenza e chiamiamo il get sulla sessione che abbiamo utilizzato per effettuare il primo login:
```python
cookies = {
    '...': '...',
}
headers = {
    'Connection': '...',
    ...
}
params = (
    ('SESSION', '...'),
    ('user', '...'),
)
response = s.get('https://accessoprogrammato.cineca.it/2020/studenti/autenticazione.php', headers=headers, params=params, cookies=cookies)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('...', headers=headers, cookies=cookies)
```
18. Una volta fatto ciò dovremmo essere pronti a scaricare tutte le pagine html della graduatoria. Vediamo dal browser quante sono le pagine della graduatoria.
19. Utilizziamo questo codice per scaricare tutte le pagine della graduatoria. Modificare il numero di pagine in base all'esigenza.
```python
num_pages = 398
for i in range(1,num_pages + 1):
      response = s.get('https://accessoprogrammato.cineca.it/2020/studenti/graduatoria.php?&statica=1&pagina=' + str(i) + '&user=...')
      f = open(str(i) + '.html', 'w', encoding='ISO-8859-1')

      f.write(response.text)

      f.close()
      print('downloaded page' + str(i) + ', waiting...')
      time.sleep(2)
```
20. Si può modificare il numero di secondi da attendere tra il download di una pagina e l'altra modificando la riga **time.sleep(NUMERO_SECONDI)**. Non è consigliato settarlo ad un numero troppo basso o si potrebbe incorrere in timeout.

Quindi il nostro script sarà qualcosa di questo tipo:

# SCRIPT 1
```python
import requests
cookies = {
    '__utma': '...',
    '__utmc': '...',
    ...
}
headers = {
    'Connection': '...',
    ...
}
data = {
  'email-log': 'YOUR EMAIL',
  'password': 'YOUR PASSWORD',
  'query_string': '...',
  'login': '1^',
  'azione': 'Entra'
}
s = requests.Session()
s.post('https://www.universitaly.it/index.php/login', headers=headers, cookies=cookies, data=data)
s.get('https://www.universitaly.it/index.php/dashboard')
cookies = {
    '...': '...',
}
headers = {
    'Connection': '...',
    ...
}
params = (
    ('SESSION', '...'),
    ('user', '...'),
)
response = s.get('https://accessoprogrammato.cineca.it/2020/studenti/autenticazione.php', headers=headers, params=params, cookies=cookies)
num_pages = 398
for i in range(1,num_pages + 1):
      response = s.get('https://accessoprogrammato.cineca.it/2020/studenti/graduatoria.php?&statica=1&pagina=' + str(i) + '&user=...')
      f = open(str(i) + '.html', 'w', encoding='ISO-8859-1')

      f.write(response.text)

      f.close()
      print('downloaded page' + str(i) + ', waiting...')
      time.sleep(2)
```

# Estrazione della graduatoria
Se proviamo ad aprire uno dei file html che abbiamo scaricato notiamo che le informazioni che ci servono sono inserite all'interno del tag **\<table class=\"graduatoria"\>\<\/table\>**. Se proviamo a copiare solamente questo tag all'interno di un file html vuoto e poi proviamo ad aprirlo, possiamo notare come sia completamente funzionante e leggibile. Per questo, il metodo più semplice consiste nel prendere tutte le tabelle è concatenarle in un singolo file html.

Utilizzeremo la libreria beautifulsoup.

Tramite questa funzione è possibile estrarre la tabella da un file html dato in input e riscriverla nello stesso file. Quindi essenzialmente si vanno a rimuovere tutte le informazioni superflue dal file html.

```Python
def get_table(file):
    f = open(file, 'r', encoding='ISO-8859-1')
    html = f.read()

    soup = BeautifulSoup(html)
    table = ''
    for found in soup.findAll():
        if found.name == 'table':
            table = str(found)
            break

    f = open(file, 'w', encoding='ISO-8859-1')
    f.write(table)
    f.close()
```

Per effettuare questa pulizia dei file html chiamiamo questa funzione su tutti i file html che abbiamo scaricato:
```Python
def clutter():
    num_pages = 398
    for i in range(1,num_pages + 1):
        get_table(str(i) + '.html')
```
Perchè queste funzioni facciano esattamente quello che vogliamo, dobbiamo aver nominato i vari file html con **NUMERO_PAGINA.html** (ex 1.html, 2.html, ...). Se abbiamo scaricato le pagine html seguendo la guida sopra, non avremo problemi. I file html sono già nominati in questo modo.

Fatto questo non ci resta che concatenare tutte le tabelle in un file e vedere cosa viene fuori.

Questa funzione ci permette di concatenare le tabelle:
```Python
def cat_html():
  num_pages = 398
    grad = open('grad.html', 'w', encoding='ISO-8859-1')
    for i in range(1,num_pages + 1):
        f = open(str(i) + '.html', 'r', encoding='ISO-8859-1')
        html = f.read()
        grad.write(html)
        f.close()
    grad.close()
```

Quindi il nostro main dovrebbe essere qualcosa del genere:
```Python
def main():
  clutter()
  cat_html()
```
Fatto ciò dovremmo avere una classifica più facile da consultare.

Lo script dovrebbe essere qualcosa del genere:

# SCRIPT 2
```Python
def clutter():
    num_pages = 398
    for i in range(1,num_pages + 1):
        get_table(str(i) + '.html')

def cat_html():
  num_pages = 398
    grad = open('grad.html', 'w', encoding='ISO-8859-1')
    for i in range(1,num_pages + 1):
        f = open(str(i) + '.html', 'r', encoding='ISO-8859-1')
        html = f.read()
        grad.write(html)
        f.close()
    grad.close()

if __name__ == '__main__':
  clutter()
  cat_html()
```
