import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres://kparykko:euHJqLkE9npPS9wD6V2bxu0snUsZvf96@drona.db.elephantsql.com:5432/kparykko")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open ("books.csv")
    reader = csv.reader(f)
    
    
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO libros (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",{"isbn": isbn, "title": title, "author": author, "year": year})
        print(f"isbn: {isbn} - title: {title} - author:{author} - year: {year} ")
        db.commit()

if __name__ == "__main__":
    main()
    
    
