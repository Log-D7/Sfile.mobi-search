#Log-D7
#https://t.me/Decode7Channel
import requests
from bs4 import BeautifulSoup

def search_url(query, page):
    return 'https://sfile.mobi/search.php', {
        'q': query,
        'search': 'Search',
        'page': page
    }

def fetch_html(url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    files = []

    for item in soup.find_all('div', class_='list'):
        link_tag = item.find('a')
        if link_tag:
            file_name = link_tag.text
            file_link = link_tag['href']
            file_size = get_size(item.get_text(strip=True))
            
            files.append({
                'name': file_name,
                'link': file_link,
                'size': file_size
            })
    
    return files

def get_size(info):
    if '(' in info and ')' in info:
        return info.split('(')[-1].split(')')[0]
    return "Unknown size"

def display(files, page):
    print(f"\n{'=' * 50}")
    print(f"{'Search Results':^50}")
    print(f"{'=' * 50}\n")
    
    if files:
        for idx, file in enumerate(files, 1):
            print(f"{(page - 1) * 10 + idx}. {file['name']}")
            print(f"   Size: {file['size']}")
            print(f"   Link: {file['link']}")
            print("-" * 50)
    else:
        print("No results found.")

def main():
    query = input("What are you looking for? ")
    page = 1

    while True:
        url, params = search_url(query, page)
        html = fetch_html(url, params)
        files = parse_html(html)
        
        display(files, page)
        
        next_page = input("Want to see the next page? (y/n): ")
        if next_page.lower() != 'y':
            break
        page += 1

if __name__ == "__main__":
    main()￼Enter
