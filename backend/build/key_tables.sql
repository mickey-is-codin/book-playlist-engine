-- Do we need to drop these tables now?
CREATE TABLE IF NOT EXISTS import_book_authors_keyed (
    author_id INTEGER PRIMARY KEY,
    author_name TEXT,
    author_average_rating REAL,
    author_text_reviews_count INTEGER,
    author_ratings_count INTEGER
) WITHOUT ROWID;

INSERT INTO import_book_authors_keyed
    SELECT 
        author_id,
        name author_name,
        average_rating author_average_rating,
        text_reviews_count author_text_reviews_count,
        ratings_count author_ratings_count
    FROM import_book_authors;

CREATE TABLE IF NOT EXISTS import_authors_keyed (
    author_id INTEGER,
    book_id INTEGER,
    role TEXT,
    PRIMARY KEY(author_id, book_id)
) WITHOUT ROWID;

-- unsure if the ignore is what we want here
INSERT OR IGNORE INTO import_authors_keyed 
    SELECT DISTINCT
        CAST(author_id AS INT) author_id,
        book_id,
        role
    FROM import_authors;

CREATE TABLE IF NOT EXISTS import_shelves_keyed (
    work_id INTEGER,
    tag_name TEXT,
    count INTEGER,
    PRIMARY KEY(work_id, tag_name)
) WITHOUT ROWID;

-- unsure if the ignore is what we want here
INSERT OR IGNORE INTO import_shelves_keyed
    SELECT
        name tag_name,
        CAST(work_id AS INT) work_id,
        CAST(count AS INT) count
    FROM import_shelves;

CREATE TABLE IF NOT EXISTS import_book_interactions_keyed (
    user_id INTEGER,
    book_id INTEGER,
    is_read INTEGER,
    rating INTEGER,
    is_reviewed INTEGER,
    PRIMARY KEY(user_id, book_id)
) WITHOUT ROWID;

INSERT INTO import_book_interactions_keyed
    SELECT *
    FROM import_book_interactions;

CREATE TABLE IF NOT EXISTS import_books_keyed (
    isbn INTEGER,
    text_reviews_count INTEGER,
    series TEXT,
    country_code TEXT,
    language_code TEXT,
    asin TEXT,
    is_ebook INTEGER,
    average_rating REAL,
    kindle_asin TEXT,
    similar_books TEXT,
    description TEXT,
    format TEXT,
    link TEXT,
    publisher TEXT,
    num_pages INTEGER,
    publication_day INTEGER,
    isbn13 INTEGER,
    publication_month INTEGER,
    edition_information TEXT,
    publication_year INTEGER,
    url TEXT,
    image_url TEXT,
    book_id INTEGER PRIMARY KEY,
    ratings_count INTEGER,
    work_id INTEGER,
    title TEXT,
    title_without_series TEXT
) WITHOUT ROWID;

INSERT INTO import_books_keyed
    SELECT
        CAST(isbn AS INTEGER) isbn,
        CAST(text_reviews_count AS INTEGER) text_reviews_count,
        series TEXT,
        country_code TEXT,
        language_code TEXT,
        asin TEXT,
        CAST(is_ebook AS INTEGER) is_ebook,
        CAST(average_rating AS REAL) average_rating,
        kindle_asin TEXT,
        similar_books TEXT,
        description TEXT,
        format TEXT,
        link TEXT,
        publisher TEXT,
        CAST(num_pages AS INTEGER) num_pages,
        CAST(publication_day AS INTEGER) publication_day,
        CAST(isbn13 AS INTEGER) isbn13,
        CAST(publication_month AS INTEGER) publication_month,
        edition_information TEXT,
        CAST(publication_year AS INTEGER) publication_year,
        url TEXT,
        image_url TEXT,
        CAST(book_id AS INTEGER) book_id,
        CAST(ratings_count AS INTEGER) ratings_count,
        CAST(work_id AS INTEGER) work_id,
        title TEXT,
        title_without_series TEXT
    FROM import_books;