#!/usr/bin/env python3
import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

# Cargar variables locales (.env)
load_dotenv()

logger = logging.getLogger(__name__)

# Intentar importar streamlit (solo existe en deploy)
try:
    import streamlit as st
except Exception:
    st = None


def get_config(key, default=None):
    """
    Busca primero en st.secrets (Streamlit Cloud),
    si no existe usa variables del sistema (.env).
    """
    if st is not None:
        try:
            return st.secrets[key]
        except Exception:
            pass

    return os.getenv(key, default)


DB_HOST = get_config("DB_HOST", "127.0.0.1")
DB_PORT = get_config("DB_PORT", "5432")
DB_USER = get_config("DB_USER", "postgres")
DB_PASSWORD = get_config("DB_PASSWORD")
DB_NAME = get_config("DB_NAME", "data_dogs")

if not DB_PASSWORD:
    raise ValueError("DB_PASSWORD no está definido ni en secrets ni en .env")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True
)

Base = declarative_base()

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_connection() -> bool:
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        logger.info("✅ Conexión a PostgreSQL exitosa")
        return True
    except Exception as e:
        logger.error(f"❌ Error conectando a PostgreSQL: {e}")
        return False
