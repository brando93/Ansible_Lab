FROM python:3.11-slim

# Evita archivos .pyc y logs raros
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de caché de Hugging Face (persistente con volumen)
ENV HF_HOME=/app/.cache/huggingface
ENV TRANSFORMERS_CACHE=/app/.cache/huggingface

WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Crear directorio de caché
RUN mkdir -p /app/.cache/huggingface

# Copiar código de la aplicación
COPY app ./app

# Puerto interno
EXPOSE 8000

# Modo mock por defecto (rápido)
# Cambiar a MODEL_MODE=full para usar modelo real
ENV MODEL_MODE=mock

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')" || exit 1

# Comando de inicio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]