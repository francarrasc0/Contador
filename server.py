from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'secreto' 

@app.route('/')
def index():
    if 'contador' in session:
        session['contador'] += 1
    else:
        session['contador'] = 1
    contador=session['contador']
    return render_template('index.html', contador=contador)

@app.route('/destroy/session', methods=['GET'])
def destroy_session():
    session.pop('contador', None)
    return redirect('/')

@app.route ('/aumentar', methods=['GET'])
def aumentar():
    if 'contador' in session:
        session['contador'] += 1
    else:
        session['contador'] = 1
    return redirect('/')

@app.route('/aumento/personalizado', methods=['POST'])
def aumento_pesonalizado():
    cantidad = int(request.form['aumento'])
    if 'contador' in session:
        session['contador'] += cantidad -1
    else:
        session['contador'] = cantidad -1
    return redirect('/') 

if __name__ == '__main__':
    app.run(debug=True)