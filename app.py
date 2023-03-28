from flask import Flask, request, render_template, redirect, abort
import requests

app = Flask(__name__)

uri = 'https://videogames-api-ip7s.onrender.com/api/videogames'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        items = requests.get(uri).json()
        videogames = []
        for item in items:
            videogames.append(item)

        response = {"videogames": videogames}
        
        return render_template('index.html', response = response)
    else:
        name = request.form['name']
        nameLower = name.lower()
        if(name != "" and not name.isspace()):
            items = requests.get(uri).json()
            videogames = []
            for item in items:
                itemLower = item['name'].lower()
                index = itemLower.find(nameLower)
                if(index != -1):
                    videogames.append(item)

            response = {"videogames": videogames}
            
            return render_template('index.html', response = response)
        else:
            return redirect('/')
    
@app.route('/view/<int:id>', methods = ['GET'])
def view(id):
    if request.method == 'GET':
        items = requests.get(uri).json()
        videogames = []
        for item in items:
            if item['id'] == id:
                videogames.append(item)
        response = {"videogames": videogames}

        return render_template('videogameview.html', response = response)
    else:
        return abort(500)
    

if __name__ == '__main__':
    app.run(debug = True)