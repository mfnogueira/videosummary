# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# # Carregar variáveis de ambiente
# load_dotenv()

# # Inicializar o cliente da OpenAI
# openai_api_key = os.getenv("OPENAI_API_KEY")
# client = OpenAI(api_key=openai_api_key)

# def gerar_resumo(texto, modelo="gpt-4o-mini"):
#     """Gera um resumo do texto usando o modelo da OpenAI."""
#     try:
#         resposta = client.chat.completions.create(
#             model=modelo,
#             messages=[
#                 {"role": "user", "content": f"Por favor, resuma o seguinte texto:\n\n{texto}"}
#             ],
#             temperature=0.7  # Controle de criatividade
#         )
#         # Acessar o conteúdo do primeiro 'choice'
#         return resposta.choices[0].message.content
#     except Exception as e:
#         return f"Erro ao gerar resumo: {e}"

# if __name__ == "__main__":
#     texto = """Aqui está um exemplo de texto longo que precisa ser resumido.
#     O objetivo é criar um resumo claro e direto ao ponto, que capture as informações principais."""
    
#     resumo = gerar_resumo(texto)
#     print("Resumo do texto:")
#     print(resumo)


import os
from dotenv import load_dotenv
from openai import OpenAI

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar o cliente da OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

# Pastas
PASTA_TRANSCRICOES = "transcriptions"
PASTA_RESUMOS = "summaries"

# Garantir que a pasta de resumos exista
os.makedirs(PASTA_RESUMOS, exist_ok=True)

def gerar_resumo(texto, modelo="gpt-4o-mini"):
    """Gera um resumo do texto usando o modelo da OpenAI."""
    try:
        resposta = client.chat.completions.create(
            model=modelo,
            messages=[
                {"role": "user", "content": f"Por favor, resuma o seguinte texto:\n\n{texto}"}
            ],
            temperature=0.7
        )
        return resposta.choices[0].message.content
    except Exception as e:
        return f"Erro ao gerar resumo: {e}"

def processar_transcricoes():
    """Processa todos os arquivos de transcrição."""
    for arquivo in os.listdir(PASTA_TRANSCRICOES):
        if arquivo.endswith(".txt"):
            caminho_arquivo = os.path.join(PASTA_TRANSCRICOES, arquivo)
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                texto = f.read()

            print(f"Gerando resumo para: {arquivo}")
            resumo = gerar_resumo(texto)

            # Salvar o resumo na pasta 'summaries' com o mesmo nome
            caminho_resumo = os.path.join(PASTA_RESUMOS, arquivo)
            with open(caminho_resumo, "w", encoding="utf-8") as f:
                f.write(resumo)

            print(f"Resumo salvo em: {caminho_resumo}")

if __name__ == "__main__":
    processar_transcricoes()
