import sqlite3
#import sys
import requests
import secrets
connection = sqlite3.connect('imdb.db')
# comment to test workflow
def main():
    sourceFile = open('data.txt', 'w')
    showdata = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt7462410"
    reference = requests.get(loc)
    results = requests.get(showdata)
    # brings in the initial data to the data file
    data = results.json()
    disp = reference.json()

    print(disp, data, file=sourceFile)
    with open('data.txt') as f:
        # reads in the file and then, formats them horizontally
        lines = f.readlines()
        print(lines, file=sourceFile)
def makedb():
    # connection = sqlite3.connect('imdb.db')
    cursor = connection.cursor()
    # makes our tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS "top250" (
    	"id"	TEXT,
    	"title"	TEXT,
    	"full_title"	TEXT,
    	"year"	INTEGER,
    	"crew"	TEXT,
    	"rating"	INTEGER,
    	"rating_count"	INTEGER,
    	PRIMARY KEY("id")
    )''')
    connection.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS "ratings" (
    	"imdbID"	TEXT,
    	"total_score"	INTEGER,
    	"total_votes"	INTEGER,
    	"ten_rating_percent"	INTEGER,
    	"ten_ratings"	INTEGER,
    	"nine_rating_percent"	INTEGER,
    	"nine_ratings"	INTEGER,
    	"eight_rating_percent"	INTEGER,
    	"eight_ratings"	INTEGER,
    	"seven_rating_percent"	INTEGER,
    	"seven_ratings"	INTEGER,
    	"six_rating_percent"	INTEGER,
    	"six_ratings"	INTEGER,
    	"five_rating_percent"	INTEGER,
    	"five_ratings"	INTEGER,
    	"four_rating_percent"	INTEGER,
    	"four_ratings"	INTEGER,
    	"three_rating_percent"	INTEGER,
    	"three_ratings"	INTEGER,
    	"two_rating_percent"	INTEGER,
    	"two_ratings"	INTEGER,
    	"one_rating_percent"	INTEGER,
    	"one_ratings"	INTEGER,
    	PRIMARY KEY("total_votes"),
    	FOREIGN KEY("imdbID") REFERENCES "top250"("id")
    )''')
    connection.commit()
    # now lets take our dictionary and fill it in here
    connection.close()
if __name__ == '__main__':
    main()
    makedb()