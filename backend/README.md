1. Download the fillowing files into a folder called data:
    - from: https://datarepo.eng.ucsd.edu/mcauley_group/gdrive/goodreads/
    - goodreads_book_authors.json.gz
    - goodreads_interactions.csv
    - goodreads_interactions.csv

2. Create a virtual environment in backend called .venv, installing the required packages:
    - python3.11 -m venv .venv
    - source .venv/bin/activate
    - pip install -r requirments.txt

3. Run the files in the import folder:
    - import/import_books.py (this one takes a while)
    - import/import_interactions.py
    - import/import_book_authors.py

4. Now there should be a library.db that exists in your data folder! Run the files in the build folder in the following order:
    - key_tables.sql
    - build_indicies.sql