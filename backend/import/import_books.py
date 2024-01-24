import pandas as pd
import sqlite3 as sql
import gzip

def main():
    con = sql.connect('data/library.db')
    file_name = 'data/goodreads_books.json.gz'

    with gzip.open(file_name) as fin:
        full = pd.read_json(fin, lines=True, chunksize = 10000)

        seen_works = set()
        counter = 0

        for temp in full:

            # print(temp.dtypes)

            authors = pd.DataFrame()
            tags = pd.DataFrame()

            # row by row... annoying
            for index, row in temp.iterrows():
                work_id = row['work_id']
                book_id = row['book_id']

                # get authors for this book
                for author in row['authors']:
                    temp_author = pd.DataFrame(author, index = [0]).assign(book_id = book_id)
                    authors = pd.concat([authors, temp_author])

                # get tags (for new works)
                if work_id not in seen_works:
                    temp_tag = pd.DataFrame(row['popular_shelves']).assign(work_id = work_id)
                    tags = pd.concat([tags, temp_tag])

                    seen_works.add(work_id)

            temp.drop(
                ['popular_shelves', 'authors'], 
                axis = 1
            ).map(
                str
            ).to_sql(
                'import_books', 
                con, 
                index = False, 
                if_exists = 'append'
            )

            authors.to_sql(
                'import_authors', 
                con, 
                index = False, 
                if_exists = 'append'
            )

            tags.to_sql(
                'import_shelves', 
                con, 
                index = False, 
                if_exists = 'append'
            )
            
            print(f'chunk {counter}/236 complete')
            counter += 1


if __name__ == '__main__':
    main()
