from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        tarros = int(request.form['tarros'])
        precio_por_tarro = 9000
        total_sin_descuento = tarros * precio_por_tarro

        if 18 <= age <= 30:
            descuento = 0.15
        elif age > 30:
            descuento = 0.25
        else:
            descuento = 0

        monto_descuento = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - monto_descuento

        return render_template('ejercicio1.html', name=name, total_sin_descuento=total_sin_descuento,
                               monto_descuento=monto_descuento, total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = {
            'juan': 'admin',
            'pepe': 'user'
        }

        if username in users and users[username] == password:
            if username == 'juan':
                message = "Bienvenido Administrador juan"
            else:
                message = "Bienvenido Usuario pepe"
            flash(message)
        else:
            flash('Usuario o contraseña incorrectos')

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)
