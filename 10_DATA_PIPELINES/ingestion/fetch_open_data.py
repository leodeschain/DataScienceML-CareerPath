# Exemplo de script para buscar dados de uma API de dados abertos.
import requests

def fetch_open_data(api_url, params):
    """
    Busca dados de uma API de dados abertos.
    """
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Lança uma exceção para códigos de erro HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados: {e}")
        return None

if __name__ == "__main__":
    # Exemplo com a API do IBGE (nomes mais comuns)
    url = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking"
    params = {"qtd": 10}
    data = fetch_open_data(url, params)
    if data:
        print("10 nomes mais comuns no Brasil (segundo o IBGE):")
        for item in data[0]['res']:
            print(f"- {item['nome']}: {item['frequencia']:,}".replace(",", "."))
