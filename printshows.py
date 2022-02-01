import requests
import secrets
def main():
    sourceFile = open('data.txt','w')
    showdata = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    results = requests.get(showdata)
    data = results.json()
    print(data,file = sourceFile)
if __name__ == '__main__':
    main()

