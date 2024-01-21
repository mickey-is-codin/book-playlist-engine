# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class BuildShelves(models.Model):
    count = models.FloatField(db_column='COUNT', blank=True, null=True)  # Field name made lowercase.
    work_id = models.IntegerField(db_column='WORK_ID', blank=True, null=True)  # Field name made lowercase.
    tag_name = models.TextField(db_column='TAG_NAME', blank=True, null=True)  # Field name made lowercase.
    tag_count = models.TextField(db_column='TAG_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tag_count_squared = models.TextField(db_column='TAG_COUNT_SQUARED', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tag_work = models.TextField(db_column='TAG_WORK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    work_count = models.TextField(db_column='WORK_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    work_count_squared = models.TextField(db_column='WORK_COUNT_SQUARED', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'BUILD_SHELVES'


class BuildWorks(models.Model):
    isbn = models.TextField(blank=True, null=True)
    text_reviews_count = models.TextField(blank=True, null=True)
    series = models.TextField(blank=True, null=True)
    country_code = models.TextField(blank=True, null=True)
    language_code = models.TextField(blank=True, null=True)
    asin = models.TextField(blank=True, null=True)
    is_ebook = models.TextField(blank=True, null=True)
    average_rating = models.TextField(blank=True, null=True)
    kindle_asin = models.TextField(blank=True, null=True)
    similar_books = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    format = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    num_pages = models.TextField(blank=True, null=True)
    publication_day = models.TextField(blank=True, null=True)
    isbn13 = models.TextField(blank=True, null=True)
    publication_month = models.TextField(blank=True, null=True)
    edition_information = models.TextField(blank=True, null=True)
    publication_year = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    book_id = models.TextField(blank=True, null=True)
    ratings_count = models.TextField(blank=True, null=True)
    work_id = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    title_without_series = models.TextField(blank=True, null=True)
    author_id = models.IntegerField(db_column='AUTHOR_ID', blank=True, null=True)  # Field name made lowercase.
    author_role = models.TextField(db_column='AUTHOR_ROLE', blank=True, null=True)  # Field name made lowercase.
    average_rating_1 = models.FloatField(db_column='average_rating:1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    text_reviews_count_1 = models.IntegerField(db_column='text_reviews_count:1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    name = models.TextField(blank=True, null=True)
    ratings_count_1 = models.IntegerField(db_column='ratings_count:1', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'BUILD_WORKS'


class ImportAuthors(models.Model):
    author_id = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)
    book_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_authors'


class ImportBookAuthors(models.Model):
    average_rating = models.FloatField(blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)
    text_reviews_count = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    ratings_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_book_authors'


class ImportBookInteractions(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    book_id = models.IntegerField(blank=True, null=True)
    is_read = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    is_reviewed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_book_interactions'


class ImportBooks(models.Model):
    isbn = models.TextField(blank=True, null=True)
    text_reviews_count = models.TextField(blank=True, null=True)
    series = models.TextField(blank=True, null=True)
    country_code = models.TextField(blank=True, null=True)
    language_code = models.TextField(blank=True, null=True)
    asin = models.TextField(blank=True, null=True)
    is_ebook = models.TextField(blank=True, null=True)
    average_rating = models.TextField(blank=True, null=True)
    kindle_asin = models.TextField(blank=True, null=True)
    similar_books = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    format = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    num_pages = models.TextField(blank=True, null=True)
    publication_day = models.TextField(blank=True, null=True)
    isbn13 = models.TextField(blank=True, null=True)
    publication_month = models.TextField(blank=True, null=True)
    edition_information = models.TextField(blank=True, null=True)
    publication_year = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    book_id = models.TextField(blank=True, null=True)
    ratings_count = models.TextField(blank=True, null=True)
    work_id = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    title_without_series = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_books'


class ImportShelves(models.Model):
    count = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    work_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_shelves'
