import requests
from bs4 import BeautifulSoup
import csv

link_do_usuario = input("Por favor, insira o link: ")

if link_do_usuario.strip():
    print(f"O link inserido foi: {link_do_usuario}")
else:
    print("Nenhum link foi inserido.")

def fetch_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Levanta uma exceção para códigos de status 4xx/5xx
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return None

def parse_html(html):
    if not html:
        return []
    soup = BeautifulSoup(html, 'html.parser')
    soup = BeautifulSoup(html, 'lxml')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links


def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Link'])  # Cabeçalho do CSV
        for item in data:
            writer.writerow([item])

def main():
    url = link_do_usuario
    html = fetch_page(url)
    if html:
        links = parse_html(html)
        if links:
            save_to_csv(links, '../data/logs/links.csv')
            print("Links salvos com sucesso em 'link.csv'")
        else:
            print("Nenhum link encontrado.")
    else:
        print("Não foi possível obter o HTML da página.")

if __name__ == "__main__":
    main()