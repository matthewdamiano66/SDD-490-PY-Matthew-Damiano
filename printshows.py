import requests
import secrets
def main():
    showdata = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    results = requests.get(showdata)
    data = results.json()
    print(data)
if __name__ == '__main__':
    main()

