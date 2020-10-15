from models import Usuarios

#insere dados na tabela pessoa
def insere_usuarios():
    usuario = Usuarios(nome='Nonato', sobrenome='Galiza')
    print(usuario)
    usuario.save()

#realiza consulta na tabela pessoa
def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)
    usuario = Usuarios.query.filter_by(nome='Ana').first()
    print(usuario.sobrenome)

if __name__=='__main__':
    #insere_usuarios()
    consulta_usuarios()