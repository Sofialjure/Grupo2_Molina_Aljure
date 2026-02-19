#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import logging

# -------------------------
# Crear carpetas necesarias
# -------------------------
os.makedirs("logs", exist_ok=True)
os.makedirs("data", exist_ok=True)

# -------------------------
# Configurar logging
# -------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/etl.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

logger.info("📊 Iniciando visualización de datos")

# -------------------------
# Cargar datos
# -------------------------
df = pd.read_csv("data/dogs.csv")

if df.empty:
    raise ValueError("❌ dogs.csv está vacío")

logger.info(f"📄 Registros cargados: {len(df)}")

# -------------------------
# Crear figura
# -------------------------
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle("Análisis de Razas de Perros", fontsize=16, fontweight="bold")

# Gráfica 1: Peso macho
axes[0, 0].bar(df["raza"], df["peso_macho_max"])
axes[0, 0].set_title("Peso Máximo Machos (kg)")
axes[0, 0].tick_params(axis="x", rotation=45)
axes[0, 0].grid(axis="y", alpha=0.3)

# Gráfica 2: Peso hembra
axes[0, 1].bar(df["raza"], df["peso_hembra_max"])
axes[0, 1].set_title("Peso Máximo Hembras (kg)")
axes[0, 1].tick_params(axis="x", rotation=45)
axes[0, 1].grid(axis="y", alpha=0.3)

# Gráfica 3: Esperanza de vida
axes[1, 0].scatter(df["raza"], df["vida_max"], s=200)
axes[1, 0].set_title("Esperanza de Vida Máxima (años)")
axes[1, 0].tick_params(axis="x", rotation=45)
axes[1, 0].grid(alpha=0.3)

# Gráfica 4: Comparación peso
x = np.arange(len(df))
width = 0.35
axes[1, 1].bar(x - width/2, df["peso_macho_max"], width, label="Macho")
axes[1, 1].bar(x + width/2, df["peso_hembra_max"], width, label="Hembra")
axes[1, 1].set_title("Peso Macho vs Hembra")
axes[1, 1].set_xticks(x)
axes[1, 1].set_xticklabels(df["raza"], rotation=45)
axes[1, 1].legend()
axes[1, 1].grid(axis="y", alpha=0.3)

# -------------------------
# Guardar imagen
# -------------------------
plt.tight_layout()
plt.savefig("data/dogs_analysis.png", dpi=300, bbox_inches="tight")
plt.close()

logger.info("✅ Imagen dogs_analysis.png creada correctamente")