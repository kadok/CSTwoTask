from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from app.data.database import Base

class Car(Base):
    """
        Classe que representa a tabela de carros e seus atributos
    """
    __tablename__ = "carros"

    id               = Column(Integer, primary_key=True, autoincrement=True)
    marca            = Column(String,  nullable=False)                    
    modelo           = Column(String,  nullable=False)                   
    ano              = Column(Integer, nullable=False)                     
    motor            = Column(String)                              
    combustivel      = Column(String)                         
    cor              = Column(String)                                      
    quilometragem    = Column(Float)                             
    portas           = Column(Integer)                           
    cambio           = Column(String)                                               
    preco            = Column(Float)                                     
    situacao         = Column(String)  

    def to_dict(self):
        return {
            "id": self.id,
            "marca": self.marca,
            "modelo": self.modelo,
            "ano": self.ano,
            "motor": self.motorizacao,
            "combustivel": self.combustivel,
            "cor": self.cor,
            "quilometragem": self.quilometragem,
            "portas": self.portas,
            "cambio": self.cambio,
            "preco": self.preco,
            "situacao": self.situacao,
        }