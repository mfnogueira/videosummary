import os
import json
from pytubefix import YouTube

# Caminho para o arquivo JSON com os links dos vídeos
json_file_path = "data/links_video.json"

# Diretório de saída para os áudios baixados
output_path = "audios_ydownload"

# Verificar se o diretório de saída existe, se não, criar
if not os.path.exists(output_path):
    os.makedirs(output_path)
    print(f"Diretório de saída criado: {output_path}")

# Ler os links dos vídeos do arquivo JSON
with open(json_file_path, "r", encoding="utf-8") as json_file:
    data = json.load(json_file)
    video_urls = data.get("links", [])

# Iterar sobre cada URL e baixar o áudio
for url in video_urls:
    try:
        # Cria um objeto YouTube
        yt = YouTube(url)

        # Obter o fluxo de áudio
        stream = yt.streams.filter(only_audio=True).first()

        # Obter o título do vídeo e substituir caracteres inválidos para nomes de arquivo
        video_title = yt.title
        safe_title = "".join(c for c in video_title if c.isalnum() or c.isspace()).rstrip()

        # Definir o nome do arquivo de saída
        filename = f"{safe_title}.mp3"

        # Baixar o áudio
        stream.download(output_path=output_path, filename=filename)

        print(f"Download concluído com sucesso: {filename}")

    except Exception as e:
        print(f"Ocorreu um erro ao baixar o vídeo {url}: {str(e)}")

print("Todos os downloads foram concluídos.")
