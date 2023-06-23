from sqlalchemy.orm import relationship, Session, declarative_base
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import Column, inspect
from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente_account"
    # atributos
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9), unique=True)
    endereco = Column(String(20), unique=True)

    # relationship
    conta = relationship("Conta", back_populates="contas")

    def __repr__(self):
        return f"User(id={self.id}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco})"


class Conta(Base):
    __tablename__ = "conta"

    # atributos
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(20))
    agencia = Column(String)
    num = Column(Integer, unique=True)
    id_cliente = Column(Integer, ForeignKey("cliente_account.id"), nullable=False)
    saldo = Column(Integer)

    # relationship
    contas = relationship("Cliente", back_populates="conta")

    def __repr__(self):
        return f"Address(id={self.id}, tipo={self.tipo}, agencia={self.num}, id_cliente={self.id_cliente}, saldo={self.saldo})"


# criando a conexão da engine no sqlite
engine = create_engine("sqlite://")

# criando as classe como tabela no banco de dados
Base.metadata.create_all(engine)

inspetor_engine = inspect(engine)

print(inspetor_engine.get_table_names())

# enviando para o DB

with Session(engine) as session:
    flayson = Cliente(
        id=1,
        nome="Flayson Junio Pereira Santos",
        cpf=(12345679),
        endereco="r.matogrosso, n 7589"
    )

    cassiane = Cliente(
        id=2,
        nome="Cassiane luiza",
        cpf=(12345678),
        endereco="r.bahia, n 12"
    )

    maria = Cliente(
        id=3,
        nome="Maria Pereira",
        cpf=(98765432),
        endereco="r.mato grosso, n 665"
    )

    # enviando para BD

    session.add_all([flayson, cassiane,maria])

    session.commit()

    # consultas ao BD - SqlAlchemy ORM
    stmt_id = select(Cliente).where(Cliente.id.in_([1,2]))
    print('\nRecuperando usuario aparti de filtragem de id...')
    for id in session.scalars(stmt_id):
        print(id)

    stmt_nome = select(Cliente).where(Cliente.nome.in_(["Cassiane luiza","Flayson Junio Pereira Santos"]))
    print('\nRecuperando usuario aparti de filtragem de nome...')
    for nome in session.scalars(stmt_nome):
        print(nome)

    stmt_cpf = select(Cliente).where(Cliente.cpf.in_([12345678]))
    print('\nRecuperando usuario aparti de filtragem de CPF...')
    for cpf in session.scalars(stmt_cpf):
        print(cpf)

    stmt_endereco = select(Cliente).where(Cliente.endereco.in_(["r.mato grosso, n 665"]))
    print('\nRecuperando usuario aparti de filtragem de Endereço...')
    for endereco in session.scalars(stmt_endereco):
        print(endereco)

