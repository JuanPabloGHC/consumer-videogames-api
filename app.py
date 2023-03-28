from flask import Flask, request, render_template, redirect, abort
import requests

app = Flask(__name__)

uri = 'https://videogames-api-ip7s.onrender.com/api/videogames'

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        items = requests.get(uri).json()
        videogames = []
        for item in items:
            videogames.append(item)

        response = {"videogames": videogames}
        
        return render_template('index.html', response = response)
    else:
        return abort(500)
    

if __name__ == '__main__':
    app.run(debug = True)