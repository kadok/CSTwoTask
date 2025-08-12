from faker import Faker
import random
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from app.data.database import SessionLocal, engine
from app.data.models import Car, Base

#Base = declarative_base()
fake = Faker("pt_BR")


# Marcas e modelos detalhados
MARCAS_MODELOS = {
    "Ford": ["Ka", "Fiesta", "Focus", "Fusion", "EcoSport", "Maverick", "Bronco"],
    "Chevrolet": ["Onix", "Prisma", "Corsa", "Cruze", "Tracker", "S10", "Spin", "Trailblazer"],
    "Toyota": ["Corolla", "Yaris", "Hilux", "Etios", "SW4", "Camry", "RAV4"],
    "Honda": ["Civic", "Fit", "City", "HR-V", "WR-V", "Accord"],
    "Fiat": ["Uno", "Palio", "Argo", "Cronos", "Toro", "Mobi", "Pulse", "Fastback"],
    "Volkswagen": ["Gol", "Polo", "Virtus", "T-Cross", "Jetta", "Nivus", "Taos"],
    "BYD": ["Han", "Seal", "Song Plus", "Tang", "Dolphin", "Yuan Plus", "Atto 3"],
    "Haval": ["H2", "H6", "Dargo", "Jolion"],
    "Nissan": ["March", "Versa", "Kicks", "Frontier", "Sentra", "X-Trail"],
    "Jeep": ["Renegade", "Compass", "Commander", "Wrangler", "Gladiator"],
    "Renault": ["Kwid", "Sandero", "Logan", "Duster", "Captur", "Oroch", "Megane E-Tech"],
    "Peugeot": ["208", "2008", "3008", "5008", "Partner", "Expert"],
    "Hyundai": ["HB20", "Creta", "Tucson", "Santa Fe", "Azera", "i30"],
    "Kia": ["Sportage", "Sorento", "Seltos", "Rio", "Cerato", "EV6"],
    "Chery": ["Tiggo 2", "Tiggo 3X", "Tiggo 5X", "Tiggo 7", "Tiggo 8"],
    "Mitsubishi": ["Lancer", "ASX", "Outlander", "Pajero", "Eclipse Cross"],
    "Suzuki": ["Jimny", "Vitara", "S-Cross", "Swift"],
    "Mazda": ["Mazda 2", "Mazda 3", "CX-3", "CX-30", "CX-5"],
    "Subaru": ["Impreza", "XV", "Forester", "Outback", "WRX"],
    "BMW": ["320i", "X1", "X5", "M3"],
    "Mercedes-Benz": ["C180", "GLA 200", "GLC 300"]
}

CORES = ["Preto", "Branco", "Prata", "Vermelho", "Azul", "Verde", "Cinza", "Amarelo", "Marrom", "Roxo", "Prata"]

TIPO_COMBUSTIVEL = ["Gasolina", "Álcool", "Diesel", "Híbrido", "Flex", "Elétrico"]
CAMBIO = ["Manual", "Automático"]
SITUACAO = ["Novo", "Usado", "Seminovo"]


def gerar_motor():
    """
        Função para gerar potência do motor
    """
    cilindradas = random.choice([1.0, 1.4, 1.6, 1.8, 2.0, 3.0])
    potencia_hp = random.randint(70, 400)
    return f"{cilindradas}L {potencia_hp}cv"

def create_database(engine):
    """
        Cria a tabela no banco (se não existir).
    """
    Base.metadata.create_all(bind=engine)

def populate_database(session, n=100):
    """
        Popula a tabela carros com dados fake.
    """
    for _ in range(n):
        marca = random.choice(list(MARCAS_MODELOS.keys()))
        modelo = random.choice(MARCAS_MODELOS[marca])
        cor = random.choice(CORES)
        portas = random.choice([2, 4])
        ano = random.randint(2000, 2025)
        motor = gerar_motor()
        combustivel = random.choice(TIPO_COMBUSTIVEL)
        quilometragem = random.randint(0, 100000)
        cambio = random.choice(CAMBIO)
        preco = round(random.uniform(30000, 500000), 2)
        situacao = "Novo" if ano >= 2023 else random.choice(SITUACAO)

        carro = Car(
            marca=marca,
            modelo=modelo,
            cor=cor,
            portas=portas,
            ano=ano,
            motor=motor,
            combustivel=combustivel,
            quilometragem=quilometragem,
            cambio=cambio,
            preco=preco,
            situacao=situacao
        )
        session.add(carro)

    session.commit()
    print(f"{n} registros inseridos com sucesso!")

if __name__ == "__main__":
    session = SessionLocal()
    create_database(engine)
    populate_database(session, n = 200)  # Insere 200 registros
    session.close()
