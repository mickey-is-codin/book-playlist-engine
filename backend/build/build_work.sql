CREATE TABLE build_work_keyed (
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
    publication_date DATE,
    publication_day INTEGER,
    isbn13 INTEGER,
    publication_month INTEGER,
    edition_information TEXT,
    publication_year INTEGER,
    url TEXT,
    image_url TEXT,
    book_id INTEGER,
    ratings_count INTEGER,
    work_id INTEGER PRIMARY KEY,
    title TEXT,
    title_without_series TEXT
) WITHOUT ROWID;

INSERT INTO build_work_keyed
    SELECT
        isbn,
        SUM(text_reviews_count) total_text_reviews_count,
        series,
        country_code,
        language_code,
        asin,
        is_ebook,
        SUM(average_rating * ratings_count) / SUM(ratings_count) as average_rating,
        kindle_asin,
        similar_books,
        description,
        format,
        link,
        publisher,
        num_pages,
        DATE(publication_year || '-' || substr('00' || publication_month, -2)  || '-' || substr('00' || publication_day, -2)) publication_date,
        publication_day,
        isbn13,
        publication_month,
        edition_information,
        publication_year,
        url,
        image_url,
        SUM(ratings_count) total_ratings_count,
        work_id,
        book_id,
        title, -- we will want an index on this
        title_without_series
    FROM import_books_keyed
    WHERE language_code = ''
    OR language_code like 'en%'
    GROUP BY work_id
    HAVING ratings_count + text_reviews_count = MAX(ratings_count + text_reviews_count);