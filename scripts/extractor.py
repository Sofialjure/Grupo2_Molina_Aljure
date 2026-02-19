#!/usr/bin/env python3
import os
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import logging

# ======================
# Cargar variables
# ======================
load_dotenv()

DOG_API_BASE_URL = os.getenv('DOG_API_BASE_URL')
DOG_PAGE_LIMIT = int(os.getenv('DOG_PAGE_LIMIT', 1))
DOG_MAX_RECORDS = int(os.getenv('DOG_MAX_RECORDS', 50))

# ======================
# Logging
# ======================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ======================
# Extractor
# ======================
class DogAPIExtractor:
    def __init__(self):
        self.base_url = DOG_API_BASE_URL
        self.page_limit = DOG_PAGE_LIMIT
        self.max_records = DOG_MAX_RECORDS

    def extraer_razas(self):
        datos = []
        page = 1

        while page <= self.page_limit and len(datos) < self.max_records:
            logger.info(f"📥 Extrayendo página {page}")

            url = f"{self.base_url}/breeds"
            params = {
                "page[number]": page
            }

            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            json_data = response.json()
            page_data = json_data.get("data", [])

            if not page_data:
                break

            datos.extend(page_data)
            page += 1

        # 🔴 Corte final exacto
        return datos[:self.max_records]

    def procesar_respuesta(self, breed):
        attr = breed.get("attributes", {})

        male = attr.get("male_weight", {})
        female = attr.get("female_weight", {})
        life = attr.get("life", {})

        return {
            "raza": attr.get("name"),
            "vida_min": life.get("min"),
            "vida_max": life.get("max"),
            "peso_macho_max": male.get("max"),
            "peso_hembra_max": female.get("max"),
            "hipoalergenico": attr.get("hypoallergenic"),
            "fecha_extraccion": datetime.now().isoformat()
        }

    def ejecutar(self):
        crudos = self.extraer_razas()
        logger.info(f"📄 Registros obtenidos: {len(crudos)}")

        procesados = [self.procesar_respuesta(b) for b in crudos]
        return procesados

# ======================
# Main
# ======================
if __name__ == "__main__":
    extractor = DogAPIExtractor()
    datos = extractor.ejecutar()

    df = pd.DataFrame(datos)

    os.makedirs("data", exist_ok=True)
    df.to_json("data/dogs_raw.json", orient="records", indent=2)
    df.to_csv("data/dogs.csv", index=False)

    logger.info("✅ Datos guardados correctamente")
    print(df)