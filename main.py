from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/r3s')
def r3s():
    return render_template('r3s.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    name = request.form['name']
    contactno = request.form['contactno']
    aspiration = request.form['aspiration']
    with open('data.txt','a') as file:
       file.write(name + ',' + contactno + ',' + aspiration + '\n')
    return render_template('thanks.html', name=name, contactno=contactno, aspiration=aspiration)

app.run(host='0.0.0.0', port=81)
