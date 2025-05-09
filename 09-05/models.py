
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///listalivros.sqlite3')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Livros(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(40), nullable=False, index=True)
    autor = Column(String(40), nullable=False, index=True)
    descricao = Column(String(40), nullable=False, index=True)


    def __repr__(self):
        return '<Livros: Titulo: {} Autor: {}>'.format(self.titulo, self.autor)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_livros = {
            'id': self.id,
            'Titulo': self.titulo,
            'Autor': self.autor,
            'Descrição': self.descricao
        }

        return dados_livros

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
