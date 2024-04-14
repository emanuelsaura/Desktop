from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)
@app.route('/')
def principal():
    website = 'https://www.bna.com.ar/Personas'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('table', class_='cotizacion')
    return render_template('mercado.html', box=box)
if __name__ == '__main__':
    app.run(debug=True)