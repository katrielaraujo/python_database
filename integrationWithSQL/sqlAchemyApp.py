import sqlalchemy
from sqlalchemy import Column, Integer, String, Float, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()

class Client(Base):
    __tablename__ = "client"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    cpf = Column(String(11))
    address = Column(String(15))

    accounts = relationship("Account", back_populates="client", cascade="all, delete-orphan")

    def __repr__(self):
        return f'id: {self.id} name: {self.name} cpf: {self.cpf}'

class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    tipo = Column(String(20))
    agency = Column(String(20), nullable=False)
    number = Column(Integer, nullable=False)
    balance = Column(Float)

    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship("Client", back_populates="accounts")

    def __repr__(self):
        return f'tipo: {self.tipo} number: {self.number} saldo: {self.balance}'

print(Client.__tablename__, Account.__tablename__)

engine = create_engine("sqlite://")
Base.metadata.create_all(engine)

with Session(engine) as session:
    juliana = Client(
        name="Juliana Mascarenhas",
        cpf="12345678901",
        address="123 Main St",
        accounts=[Account(tipo="Conta Corrente", agency="001", number=1001, balance=1000.00)]
    )
    sandy = Client(
        name="Sandy Cardoso",
        cpf="98765432101",
        address="456 Elm St",
        accounts=[Account(tipo="Conta Poupança", agency="002", number=2001, balance=2500.00)]
    )
    patrick = Client(
        name="Patrick Cardoso",
        cpf="11122233344",
        address="789 Oak St",
        accounts=[Account(tipo="Conta Corrente", agency="003", number=3001, balance=1500.00)]
    )

    session.add_all([juliana, sandy, patrick])
    session.commit()

    print("Dados da tabela 'Cliente': ")
    clients = session.query(Client).all()
    for client in clients:
        print(client)

    print("Dados da tabela 'Account': ")
    accounts = session.query(Account).all()
    for account in accounts:
        print(account)
