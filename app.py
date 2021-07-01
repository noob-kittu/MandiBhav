from flask import Flask, render_template
from bs4 import BeautifulSoup
import cloudscraper

def neemuch():
     URL = "https://ekisan.net/neemuch-mandi-bhav/"
     scraper = cloudscraper.create_scraper()
     r = scraper.get(URL)
          
     soup = BeautifulSoup(r.text, "html.parser")
     #soup = BeautifulSoup(r.content, 'html5lib')
     
     jinjabhai = """{% extends 'index.html' %}
     {% block content %}
     """

     headline = '<br> <button class="btn btn-primary" onclick="history.back()">Go back!</button><h1>Neemuch Mandi Bhav!</h1> <br>'
     jinjabhai2 = "{% endblock %}"
     table = soup.find('table')  
                   
     with open('templates/neemuch.html', 'w+', encoding='utf-8') as f:
               f.write(jinjabhai+ headline +str(table) + jinjabhai2)

     return table
 
 
def mandsore():
     URL = "https://ekisan.net/mandsaur-mandi-bhav/"
     scraper = cloudscraper.create_scraper()
     r = scraper.get(URL)
          
     soup = BeautifulSoup(r.text, "html.parser")
     #soup = BeautifulSoup(r.content, 'html5lib')
     
     jinjabhai = """{% extends 'index.html' %}
     {% block content %}
     """
     headline = '<br> <button class="btn btn-primary" onclick="history.back()">Go back!</button><h1>Mandsore Mandi Bhav!</h1> <br>'

     jinjabhai2 = "{% endblock %}"
     table = soup.find('table')  
                   
     with open('templates/mandsore.html', 'w+', encoding='utf-8') as f:
               f.write(jinjabhai+ headline + str(table) + jinjabhai2)

     return table


 
def Badnagar():
     URL = "https://ekisan.net/badnagar-mandi-bhav/"
     scraper = cloudscraper.create_scraper()
     r = scraper.get(URL)
          
     soup = BeautifulSoup(r.text, "html.parser")
     #soup = BeautifulSoup(r.content, 'html5lib')
     
     jinjabhai = """{% extends 'index.html' %}
     {% block content %}
     """
     headline = '<br> <button class="btn btn-primary" onclick="history.back()">Go back!</button><h1>Badnagar Mandi Bhav!</h1> <br>'

     jinjabhai2 = "{% endblock %}"
     table = soup.find('table')  
                   
     with open('templates/badnagar.html', 'w+', encoding='utf-8') as f:
               f.write(jinjabhai+ headline + str(table) + jinjabhai2)

     return table




def indore():
     URL = "https://ekisan.net/indore-mandi-bhav/"
     scraper = cloudscraper.create_scraper()
     r = scraper.get(URL)
          
     soup = BeautifulSoup(r.text, "html.parser")
     #soup = BeautifulSoup(r.content, 'html5lib')
     
     jinjabhai = """{% extends 'index.html' %}
     {% block content %}
     """
     headline = '<br> <button class="btn btn-primary" onclick="history.back()">Go back!</button><h1>Indore Mandi Bhav!</h1> <br>'

     jinjabhai2 = "{% endblock %}"
     table = soup.find('table')  
                   
     with open('templates/indore.html', 'w+', encoding='utf-8') as f:
               f.write(jinjabhai+ headline + str(table) + jinjabhai2)

     return table


def mcx():
     URL = "https://mcxdata.in/"
     scraper = cloudscraper.create_scraper()
     r = scraper.get(URL)
          
     soup = BeautifulSoup(r.text, "html.parser")
     #soup = BeautifulSoup(r.content, 'html5lib')
     
     jinjabhai = """{% extends 'index.html' %}
     {% block content %}
     """
     headline = '<br> <button class="btn btn-primary" onclick="history.back()">Go back!</button><h1>MCX LIVE RATES</h1> <br>'

     jinjabhai2 = "{% endblock %}"
     table = soup.find_all('table', {'id':'fullMcxPriceTable'})  
                   
     with open('templates/mcx.html', 'w+', encoding='utf-8') as f:
               f.write(jinjabhai+ headline + str(table) + jinjabhai2)

     return table
        

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/neemuch')
def nim():
    nimach = neemuch()
    return render_template('neemuch.html')


@app.route('/mandsore')
def mands():
    mandsor = mandsore()
    return render_template('mandsore.html')

@app.route('/badnagar')
def badnag():
    badnag = Badnagar()
    return render_template('badnagar.html')


@app.route('/indore')
def ind():
    indo = indore()
    return render_template('indore.html')

@app.route('/mcx')
def mxc():
    m = mcx()
    return render_template('mcx.html')

if __name__ == "__main__":
    app.run(debug=False)
