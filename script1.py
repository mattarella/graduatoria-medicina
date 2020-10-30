import requests
"""
INCOLLA QUI IL CODICE PRESO SEGUENDO IL PUNTO 8 DELLA GUIDA

ASSOMIGLIA A QUESTO CODICE :

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

"""
s = requests.Session()
s.post('https://www.universitaly.it/index.php/login', headers=headers, cookies=cookies, data=data)
s.get('https://www.universitaly.it/index.php/dashboard')
"""
INCOLLA QUI IL CODICE PRESO SEGUENDO IL PUNTO 16 DELLA GUIDA

ASSOMIGLIA A QUESTO CODICE :

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
"""
response = s.get('https://accessoprogrammato.cineca.it/2020/studenti/autenticazione.php', headers=headers, params=params, cookies=cookies)
num_pages = 398
for i in range(1,num_pages + 1):
      response = s.get('https://accessoprogrammato.cineca.it/2020/studenti/graduatoria.php?&statica=1&pagina=' + str(i) + '&user=...')
      f = open(str(i) + '.html', 'w', encoding='ISO-8859-1')

      f.write(response.text)

      f.close()
      print('downloaded page' + str(i) + ', waiting...')
      time.sleep(2)
