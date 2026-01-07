# model.py
import os
from transformers import pipeline

class AIModel:
    def __init__(self):
        # Usa variable de entorno para elegir modo
        self.mode = os.getenv("MODEL_MODE", "mock")
        
        if self.mode == "full":
            # Modo completo con modelo real (más lento, más pesado)
            print("🚀 Loading full AI model (distilgpt2)...")
            self.generator = pipeline(
                "text-generation",
                model="distilgpt2",
                device=-1  # CPU (usa 0 para GPU si está disponible)
            )
            print("✅ Model loaded successfully")
        else:
            # Modo mock (rápido, ligero, para desarrollo)
            print("⚡ Using mock model (fast mode)")
            self.generator = None

    def predict(self, text: str) -> str:
        if self.mode == "full" and self.generator:
            # Genera texto con máximo 50 tokens
            output = self.generator(text, max_length=50, do_sample=True)[0]['generated_text']
            return output
        else:
            # Mock response - respuestas predefinidas rápidas
            responses = {
                "hello": "Hello! I'm a FastAPI mock model. How can I help you today?",
                "how are you": "I'm doing great! This is a mock response for fast testing.",
                "what is your name": "I'm a FastAPI AI assistant running in mock mode for quick development.",
            }
            
            # Busca coincidencia parcial
            text_lower = text.lower()
            for key, response in responses.items():
                if key in text_lower:
                    return f"{text} {response}"
            
            # Respuesta por defecto
            return f"{text} [Mock AI Response: This is a fast mock model for development. Set MODEL_MODE=full for real AI.]"

# Instancia global
model = AIModel()
