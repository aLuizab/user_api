import os
from flask import Flask, request
from flask_restful import Resource, Api
from models import Usuarios

app = Flask(__name__)
api = Api(app)


class Usuario(Resource):
    def get(self, cpf):
        usuario = Usuarios.query.filter_by(cpf=cpf).first()
        try:
            response = {
                'nome': usuario.nome,
                'sobrenome': usuario.sobrenome,
                'cpf': usuario.cpf,
                'email': usuario.email,
                'nascimento': usuario.nascimento,
                'id': usuario.id
            }
        except AttributeError:
            response = {
                'status': 'Error',
                'mensagem': 'Usuario nao cadastrado'
            }
        return response


class ListaUsuarios(Resource):
    def get(self):
        usuarios = Usuarios.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'sobrenome': i.sobrenome} for i in usuarios]
        return response

    def post(self):
        dados = request.json
        usuario = Usuarios(nome=dados['nome'], cpf=dados['cpf'])
        usuario.save()
        response = {
            'id': usuario.id,
            'nome': usuario.nome,
            'cpf': usuario.cpf
        }
        return response

@app.route('/test')
def test():
    return "Works!"


api.add_resource(Usuario, '/user/<int:cpf>/')
api.add_resource(ListaUsuarios, '/user/')

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == '__main__':
    app.run(debug=True)
    main()