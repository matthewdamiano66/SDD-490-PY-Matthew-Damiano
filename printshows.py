import requests
import secrets
def main():
    sourceFile = open('data.txt','w')
    showdata = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt7462410"
    reference= requests.get(loc)
    results = requests.get(showdata)
   #brings in the initial data to the data file
    data = results.json()
    disp = reference.json()

    print(disp,data,file=sourceFile)

    with open('data.txt') as f:
        #reads in the file and then, formats them horizontally
        lines = f.readlines()
        print(lines,file = sourceFile)
if __name__ == '__main__':
    main()