import pandas as pd
import sqlite3 as sql
import gzip

def main():
    con = sql.connect('data/library.db')
    file_name = 'data/goodreads_book_authors.json.gz'

    with gzip.open(file_name) as fin:
        # encoding for some author names is off
        full = pd.read_json(
            fin,
            lines=True)
        
        # write to sql
        full.to_sql(
            'import_book_authors', 
            con, 
            index = False, 
            if_exists = 'replace')

if __name__ == '__main__':
    main()
