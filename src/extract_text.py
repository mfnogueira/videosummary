
# import os
# import requests
# from dotenv import load_dotenv

# # Carregar as variáveis de ambiente do arquivo .env
# load_dotenv()

# # Obter a chave da API do OpenAI
# api_key = os.getenv("OPENAI_API_KEY")

# # Diretórios de entrada e saída
# audio_dir = "D:/workspace/VidioSummary/ydownload"
# transcription_dir = "D:/workspace/VidioSummary/transcriptions"

# # Verificar se o diretório de transcrições existe, se não, criar
# if not os.path.exists(transcription_dir):
#     os.makedirs(transcription_dir)
#     print(f"Diretório de transcrições criado: {transcription_dir}")

# # URL da API
# url = "https://api.openai.com/v1/audio/transcriptions"

# # Definir os headers
# headers = {
#     "Authorization": f"Bearer {api_key}"
# }

# # Iterar sobre todos os arquivos de áudio na pasta ydownload
# for audio_file_name in os.listdir(audio_dir):
#     if audio_file_name.endswith(".mp3"):
#         audio_file_path = os.path.join(audio_dir, audio_file_name)
#         transcription_file_name = os.path.splitext(audio_file_name)[0] + ".txt"
#         transcription_file_path = os.path.join(transcription_dir, transcription_file_name)

#         print(f"Processando arquivo de áudio: {audio_file_name}")

#         # Verificar se a transcrição já existe
#         if os.path.exists(transcription_file_path):
#             print(f"Transcrição já existe para {audio_file_name}. Pulando...")
#             continue

#         # Abrir o arquivo de áudio e enviar a requisição
#         with open(audio_file_path, "rb") as audio_file:
#             files = {
#                 "file": audio_file
#             }
#             data = {
#                 "model": "whisper-1"  # Modelo da transcrição
#             }
#             # Enviar a requisição POST
#             print(f"Enviando requisição de transcrição para {audio_file_name}...")
#             response = requests.post(url, headers=headers, files=files, data=data)

#         # Verificar a resposta da API
#         if response.status_code == 200:
#             print(f"Transcrição realizada com sucesso para {audio_file_name}!")
#             transcription = response.json().get("text", "")

#             # Salvar a transcrição em um arquivo de texto
#             with open(transcription_file_path, "w", encoding="utf-8") as transcription_file:
#                 transcription_file.write(transcription)

#             print(f"Transcrição salva em {transcription_file_path}")
#         else:
#             print(f"Erro na requisição para {audio_file_name}: {response.status_code}")
#             print(response.text)  # Exibir o erro detalhado

# print("Processamento concluído.")


import os
import requests
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a chave da API do OpenAI
api_key = os.getenv("OPENAI_API_KEY")

# Diretórios de entrada e saída (caminhos relativos)
audio_dir = "audios_ydownload"
transcription_dir = "transcriptions"

# Verificar se o diretório de transcrições existe, se não, criar
if not os.path.exists(transcription_dir):
    os.makedirs(transcription_dir)
    print(f"Diretório de transcrições criado: {transcription_dir}")

# URL da API
url = "https://api.openai.com/v1/audio/transcriptions"

# Definir os headers
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Iterar sobre todos os arquivos de áudio na pasta audios_ydownload
for audio_file_name in os.listdir(audio_dir):
    if audio_file_name.endswith(".mp3"):
        audio_file_path = os.path.join(audio_dir, audio_file_name)
        transcription_file_name = os.path.splitext(audio_file_name)[0] + ".txt"
        transcription_file_path = os.path.join(transcription_dir, transcription_file_name)

        print(f"Processando arquivo de áudio: {audio_file_name}")

        # Verificar se a transcrição já existe
        if os.path.exists(transcription_file_path):
            print(f"Transcrição já existe para {audio_file_name}. Pulando...")
            continue

        # Abrir o arquivo de áudio e enviar a requisição
        with open(audio_file_path, "rb") as audio_file:
            files = {
                "file": audio_file
            }
            data = {
                "model": "whisper-1"  # Modelo da transcrição
            }
            # Enviar a requisição POST
            print(f"Enviando requisição de transcrição para {audio_file_name}...")
            response = requests.post(url, headers=headers, files=files, data=data)

        # Verificar a resposta da API
        if response.status_code == 200:
            print(f"Transcrição realizada com sucesso para {audio_file_name}!")
            transcription = response.json().get("text", "")

            # Salvar a transcrição em um arquivo de texto
            with open(transcription_file_path, "w", encoding="utf-8") as transcription_file:
                transcription_file.write(transcription)

            print(f"Transcrição salva em {transcription_file_path}")
        else:
            print(f"Erro na requisição para {audio_file_name}: {response.status_code}")
            print(response.text)  # Exibir o erro detalhado

print("Processamento concluído.")
