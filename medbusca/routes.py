from medbusca import app, db
from flask import Flask, render_template, url_for, request, flash, redirect


# Rota para exibir o formulário de busca
@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/busca', methods=['POST','GET'])
def busca():
    form_busca = forms.Busca()
    if form_busca.validate_on_submit():
        # Exibe mensagem de operação bem sucedida - importa flash
        flash('Busca bem sucedida!', 'alert-success')
        return render_template('busca.html', form_busca=form_busca)

# Rota para processar a busca
@app.route('/resultados', methods=['POST'])
def resultados():
    estado = request.form['estado']
    cidade = request.form['cidade']
    especialidade = request.form['especialidade']

 