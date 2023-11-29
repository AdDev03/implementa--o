from medbusca import app, db
from medbusca import models
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length



# Rota para exibir o formulário de busca
@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/busca', methods=['POST','GET'])
def busca():
        return render_template('busca.html')

# Rota para processar a busca
@app.route('/resultados', methods=['POST', 'GET'])
def resultados():
    resultados = models.Disponibilidade_medico_view.query.all()
    return render_template('resultados.html', resultados=resultados)
  

 