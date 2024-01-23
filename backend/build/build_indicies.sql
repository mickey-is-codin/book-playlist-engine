CREATE INDEX idx_author_names
ON import_book_authors_keyed (author_name);

CREATE INDEX work_names
ON build_work_keyed (title);