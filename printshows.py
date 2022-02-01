import requests
import secrets
def main():
    sourceFile = open('data.txt','w')
    sourceFile2 = open('new.txt','w')
    showdata = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    results = requests.get(showdata)
   #brings in the initial data to the data file
    data = results.json()
    print(data,file = sourceFile)
    with open('data.txt') as f:
        #reads in the file and then, formats them horizontally
        lines = f.readlines()
        print(lines,file = sourceFile2)
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        print (punc)

        def remove_punc(string):
            punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
            for ele in data:
                if ele in punc:
                    string = string.replace(ele, "")
            return data.txt


if __name__ == '__main__':
    main()

