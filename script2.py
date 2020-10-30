from bs4 import BeautifulSoup  
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
