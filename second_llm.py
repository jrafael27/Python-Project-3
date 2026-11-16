import json

import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"  # sesuaikan dengan hasil `ollama list`

try:
    res = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "user", "content": "Jelaskan apa itu API dalam 2 kalimat."}
            ],
            "stream": True,
            "options": {"num_predict": 150},  # batasi panjang jawaban
        },
        stream=True,
        timeout=300,
    )
    res.raise_for_status()

    for baris in res.iter_lines():
        if not baris:
            continue
        potongan = json.loads(baris)
        print(potongan.get("message", {}).get("content", ""), end="", flush=True)
        if potongan.get("done"):
            break
    print()

except requests.exceptions.ConnectionError:
    print("Ollama belum berjalan. Buka aplikasi Ollama atau jalankan: ollama serve")
except requests.exceptions.Timeout:
    print("Terlalu lama menunggu. Coba model yang lebih kecil.")