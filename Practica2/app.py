from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('inscripcion.html')

@app.route('/inscripcion', methods=['GET', 'POST'])
def inscripcion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        curso = request.form['curso']
        return f"Inscripción recibida: {nombre} {apellido}, Curso: {curso}"
    return render_template('inscripcion.html')

@app.route('/registro_usuarios', methods=['GET', 'POST'])
def registro_usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        return f"Registro de usuario: {nombre} {apellido}, Email: {email}"
    return render_template('registro_usuarios.html')

@app.route('/registro_productos', methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        precio = request.form['precio']
        return f"Producto registrado: {producto}, Categoría: {categoria}, Precio: {precio}"
    return render_template('registro_productos.html')

@app.route('/registro_libros', methods=['GET', 'POST'])
def registro_libros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        return f"Libro registrado: {titulo}, Autor: {autor}, Resumen: {resumen}"
    return render_template('registro_libros.html')

if __name__ == '__main__':
    app.run(debug=True)

