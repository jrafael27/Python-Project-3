import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"  # sesuaikan dengan yang kamu pull

try:
    res = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "user", "content": "Jelaskan apa itu API dalam 2 kalimat."}
            ],
            "stream": False,
        },
        timeout=120,
    )
    res.raise_for_status()
except requests.exceptions.ConnectionError:
    print("Ollama belum berjalan. Buka aplikasi Ollama atau jalankan: ollama serve")
    raise SystemExit(1)

data = res.json()
print(data["message"]["content"])
print("Token masuk:", data["prompt_eval_count"])
print("Token keluar:", data["eval_count"])