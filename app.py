from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sistema'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT NOMBRE, CORREO, MENSAJE, PAGO, MOTIVO FROM consulta")
    empleados = cursor.fetchall()
    cursor.close()
    return render_template('empleados/index.html', empleados=empleados)

@app.route('/create')
def create():
    return render_template('empleados/create.html')

@app.route('/store', methods=['POST'])
def store():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        pago = request.form['pago']
        motivo = request.form['motivo']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO consulta (NOMBRE, CORREO, MENSAJE, PAGO, MOTIVO) VALUES (%s, %s, %s, %s, %s)", (nombre, correo, mensaje, pago, motivo))
        mysql.connection.commit()
        cursor.close()
        
        return redirect(url_for('index'))

@app.route('/delete/<correo>')
def delete(correo):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM consulta WHERE CORREO = %s", (correo,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
