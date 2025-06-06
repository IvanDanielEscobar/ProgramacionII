from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')    

@app.route('/datos_personales')
def datos_personales():
    return render_template('datos_personales.html')    

@app.route('/datos_de_contacto')
def contacto():
    return render_template('contacto.html')    

@app.route('/redes_sociales')
def redes_sociales():
    return render_template('redes_sociales.html')    

@app.route('/idiomas')
def idiomas():
    return render_template('idiomas.html')    

@app.route('/intereses')
def intereses():
    return render_template('intereses.html')    

@app.route('/sobre_mi')
def sobre_mi():
    return render_template('sobre_mi.html')    

@app.route('/experiencia')
def experiencia():
    return render_template('experiencia.html')    

@app.route('/educacion')
def educacion():
    return render_template('educacion.html')    

@app.route('/habilidades')
def habilidades():
    return render_template('habilidades.html')    

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')    

@app.route('/referencias')
def referencias():
    return render_template('referencias.html')    

if __name__ == '__main__':
    app.run(debug=True)
    