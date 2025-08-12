from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import Config

if not Config.DB_LINK:
    raise ValueError("A variável de ambiente DB_LINK não foi definida no .env")

Base = declarative_base()
engine = create_engine(Config.DB_LINK, echo=Config.DEBUG, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    """Gera sessão do banco para uso em rotas."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
