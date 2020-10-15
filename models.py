from sqlalchemy import create_engine, Column, Integer, ForeignKey, String
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///usuarios.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                            bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Usuarios(Base):
    __tablename__='usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    sobrenome = Column(String(40), index=True)
    cpf = Column(Integer)
    email = Column(String(40), index=True)
    nascimento = Column(Integer)

    def __repr__(self):
        return '<Usuario {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__== '__main__':
    init_db()
