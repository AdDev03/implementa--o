from medbusca import db
from datetime import datetime

class Disponibilidade_medico_view(db.Model):
        crm_medico = db.Column(db.String)
        dataHoraInicio = db.Column(db.String)
        dataHoraFim = db.Column(db.String)
        especialidade = db.Column(db.Interger)
        rua_unidade = db.Column(db.String)
        cep_unidade = db.Column(db.String)
        numero_unidade = db.Column(db.String)
        bairro_unidade = db.Column(db.String)
        cidade_unidade = db.Column(db.String)
        estado_unidade = db.Column(db.String)
        nome_unidade = db.Column(db.String)