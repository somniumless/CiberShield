from flask import Flask, render_template, request
from datetime import datetime
import re 
import os

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('pagina.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        print(f'Login de {correo} con contraseña {contrasena}')
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        print(f'Registro de {correo} con contraseña {contrasena}')
    return render_template('registro.html')

@app.route('/contrasena', methods=['GET', 'POST'])
def olvidar_contrasena():
    if request.method == 'POST':
        correo = request.form['correo']
        print(f'Solicitud de recuperación de contraseña para: {correo}')
    return render_template('contrasena.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

@app.route('/preguntas')
def preguntas():
    return render_template('preguntas.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/ayuda')
def ayuda():
    return render_template('ayuda.html')

@app.route('/modulo1')
def modulo1():
    return render_template('modulo1.html')

@app.route('/Planes')
def planes():
    return render_template('Planes.html')

@app.route('/introduccion_ciberseguridad')
def introduccion_ciberseguridad():
    return render_template('introduccion_ciberseguridad.html')