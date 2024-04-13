from flask import Flask, request, jsonify

app = Flask(__name__)

arreglo = [1,2,3,4]

@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({'respuesta':arreglo}),200

@app.route('/saludar/<nombre>', methods=['GET'])
def saludar(nombre):
    return f'Hola, {nombre}!'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
