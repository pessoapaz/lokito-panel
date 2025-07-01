
# Simulador de comentário IA (manual ou automático) - YouTube ou Reddit (modo básico)
import random
import time

comentarios = [
    "Eles não querem que você veja isso...",
    "⚠️ Algo foi descoberto no código-fonte...",
    "Chip secreto detectado em dispositivos comuns.",
    "Promoção fantasma ativada. Link: https://lokito-link.com",
    "Esse vídeo está escondendo algo. Leia os comentários..."
]

def comentar_simulado(destino="YouTube", loops=10):
    for _ in range(loops):
        comentario = random.choice(comentarios)
        print(f"[{destino}] IA comenta: {comentario}")
        time.sleep(random.uniform(2, 5))

if __name__ == "__main__":
    comentar_simulado("YouTube", 5)
