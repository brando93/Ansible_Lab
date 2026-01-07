# FastAPI AI Application

## 🚀 Características

- **Modo Mock (Rápido)**: Respuestas instantáneas para desarrollo
- **Modo Full (IA Real)**: Modelo distilgpt2 de Hugging Face
- **Caché Persistente**: Los modelos se guardan en volúmenes Docker
- **Health Check**: Endpoint `/health` para monitoreo

## 🎯 Modos de Operación

### Modo Mock (Por defecto en DEV)
- ⚡ Inicio instantáneo (~5 segundos)
- 💾 Imagen ligera (~500MB)
- 🔄 Respuestas predefinidas rápidas
- ✅ Ideal para desarrollo y testing

### Modo Full (Por defecto en PROD)
- 🤖 Modelo real de IA (distilgpt2)
- 📦 Primera descarga: ~250MB
- ⏱️ Primer inicio: 1-2 minutos
- 🔄 Siguientes inicios: ~30 segundos (usa caché)
- ✅ Ideal para producción

## 📡 Endpoints

### Health Check
```bash
curl http://localhost:8001/health
```

Respuesta:
```json
{
  "status": "ok",
  "environment": "dev"
}
```

### Predicción (Mock Mode)
```bash
curl -X POST http://localhost:8001/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "hello"}'
```

Respuesta:
```json
{
  "result": "hello Hello! I'm a FastAPI mock model. How can I help you today?"
}
```

### Predicción (Full Mode)
```bash
curl -X POST http://localhost:8002/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "The future of AI is"}'
```

Respuesta (generada por IA):
```json
{
  "result": "The future of AI is bright and full of possibilities..."
}
```

## 🔧 Configuración

### Cambiar modo en DEV a Full
Edita `ansible-lab/ansible/group_vars/dev.yml`:
```yaml
model_mode: full  # Cambiar de 'mock' a 'full'
```

### Cambiar modo en PROD a Mock
Edita `ansible-lab/ansible/group_vars/prod.yml`:
```yaml
model_mode: mock  # Cambiar de 'full' a 'mock'
```

## 💾 Persistencia

Los modelos de IA se guardan en volúmenes Docker:
- `fastapi-cache-dev`: Caché para entorno dev
- `fastapi-cache-prod`: Caché para entorno prod

**Ventaja**: Cuando bajas y subes el ambiente, el modelo ya está descargado y el inicio es rápido.

## 🐳 Puertos

- **DEV**: `http://localhost:8001`
- **PROD**: `http://localhost:8002`

## 📊 Recursos

### Modo Mock
- RAM: ~200MB
- Disco: ~500MB
- CPU: Bajo

### Modo Full
- RAM: ~1-2GB
- Disco: ~2GB (primera vez), ~500MB (con caché)
- CPU: Medio-Alto durante inferencia

## 🧪 Testing Rápido

```bash
# Health check
curl http://localhost:8001/health

# Predicción simple
curl -X POST http://localhost:8001/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "hello"}'

# Predicción con pregunta
curl -X POST http://localhost:8001/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "how are you"}'
```

## 🔄 Workflow Recomendado

1. **Desarrollo**: Usa modo `mock` en DEV para iteración rápida
2. **Testing**: Cambia a modo `full` en DEV para probar el modelo real
3. **Producción**: Usa modo `full` en PROD con caché persistente
4. **CI/CD**: Jenkins despliega automáticamente según configuración

## 📝 Variables de Entorno

- `ENV`: Entorno (dev/prod)
- `MODEL_MODE`: Modo del modelo (mock/full)
- `HF_HOME`: Directorio de caché de Hugging Face
- `TRANSFORMERS_CACHE`: Caché de transformers

## 🎓 Ejemplos de Prompts (Modo Full)

```bash
# Generación de texto
curl -X POST http://localhost:8002/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Once upon a time"}'

# Continuación de historia
curl -X POST http://localhost:8002/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "In a world where AI"}'

# Pregunta abierta
curl -X POST http://localhost:8002/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "What is the meaning of"}'