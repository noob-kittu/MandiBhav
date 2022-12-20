from flask import Flask, render_template
from bs4 import BeautifulSoup
import cloudscraper

class Mandirate:
    def __init__(self, url, city_name):
        self.url = url
        self.city_name = city_name
        self.scraper = cloudscraper.create_scraper()
    
    def scrape(self):
        r = self.scraper.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find('table')
        return table
    
    def save_to_file(self, table):
        jinjabhai = """{% extends 'index.html' %}
        {% block content %}
        """
        headline = '<br> <button class="btn btn-primary" onclick="history.back()">Go back!</button><h1>{} Mandi Bhav!</h1> <br>'.format(self.city_name)
        jinjabhai2 = "{% endblock %}"
        
        with open('templates/{}.html'.format(self.city_name), 'w+', encoding='utf-8') as f:
            f.write(jinjabhai + headline + str(table) + jinjabhai2)


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
    neemuch = Mandirate("https://ekisan.net/neemuch-mandi-bhav/", "Neemuch")
    return render_template('Neemuch.html')


@app.route('/mandsore')
def mands():
    mandsore = Mandirate("https://ekisan.net/mandsaur-mandi-bhav/", "Mandsore")
    return render_template('Mandsore.html')

@app.route('/badnagar')
def badnag():
    Badnagar = Mandirate("https://ekisan.net/badnagar-mandi-bhav/", "Badnagar")
    return render_template('Badnagar.html')


@app.route('/indore')
def ind():
    indore = Mandirate("https://ekisan.net/indore-mandi-bhav/", "Indore")
    return render_template('Indore.html')

@app.route('/mcx')
def mxc():
    m = mcx()
    return render_template('mcx.html')

if __name__ == "__main__":
    app.run(debug=True)
