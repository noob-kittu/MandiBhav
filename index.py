from flask import Flask, render_template
from bs4 import BeautifulSoup
import cloudscraper
import asyncio

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


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/neemuch')
def nimach():
    mandirate = Mandirate("https://ekisan.net/neemuch-mandi-bhav/", "Neemuch")
    table = mandirate.scrape()
    mandirate.save_to_file(table)
    return render_template('Neemuch.html')


@app.route('/mandsore')
def mandsor():
    mandirate = Mandirate("https://ekisan.net/mandsaur-mandi-bhav/", "Mandsore")
    table = mandirate.scrape()
    mandirate.save_to_file(table)
    return render_template('Mandsore.html')

@app.route('/badnagar')
def badnagar():
    mandirate = Mandirate("https://ekisan.net/badnagar-mandi-bhav/", "Badnagar")
    table = mandirate.scrape()
    mandirate.save_to_file(table)
    return render_template('Badnagar.html')


@app.route('/indore')
def indor():
    mandirate = Mandirate("https://ekisan.net/indore-mandi-bhav/", "Indore")
    table = mandirate.scrape()
    mandirate.save_to_file(table)
    return render_template('Indore.html')


if __name__ == "__main__":
    app.run(debug=True)
