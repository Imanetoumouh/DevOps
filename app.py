from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        age = request.form['age']
        return render_template('resultat.html', nom=nom, prenom=prenom, age=age)
    return render_template('formulaire.html')

if __name__ == '__main__':
    app.run(debug=True)
