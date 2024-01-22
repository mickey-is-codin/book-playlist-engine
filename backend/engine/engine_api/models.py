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


class BuildWork(models.Model):
    isbn = models.IntegerField(db_column='ISBN', blank=True, null=True)  # Field name made lowercase.
    isbn13 = models.IntegerField(db_column='ISBN13', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='TITLE', blank=True, null=True)  # Field name made lowercase.
    work_id = models.IntegerField(db_column='WORK_ID', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    book_id = models.IntegerField(db_column='BOOK_ID', blank=True, null=True)  # Field name made lowercase.
    book_average_rating = models.FloatField(db_column='BOOK_AVERAGE_RATING', blank=True, null=True)  # Field name made lowercase.
    book_text_reviews_count = models.IntegerField(db_column='BOOK_TEXT_REVIEWS_COUNT', blank=True, null=True)  # Field name made lowercase.
    book_ratings_count = models.IntegerField(db_column='BOOK_RATINGS_COUNT', blank=True, null=True)  # Field name made lowercase.
    num_pages = models.IntegerField(db_column='NUM_PAGES', blank=True, null=True)  # Field name made lowercase.
    publisher = models.TextField(db_column='PUBLISHER', blank=True, null=True)  # Field name made lowercase.
    publication_year = models.IntegerField(db_column='PUBLICATION_YEAR', blank=True, null=True)  # Field name made lowercase.
    publication_month = models.IntegerField(db_column='PUBLICATION_MONTH', blank=True, null=True)  # Field name made lowercase.
    publication_day = models.IntegerField(db_column='PUBLICATION_DAY', blank=True, null=True)  # Field name made lowercase.
    country_code = models.TextField(db_column='COUNTRY_CODE', blank=True, null=True)  # Field name made lowercase.
    language_code = models.TextField(db_column='LANGUAGE_CODE', blank=True, null=True)  # Field name made lowercase.
    series = models.TextField(db_column='SERIES', blank=True, null=True)  # Field name made lowercase.
    asin = models.TextField(db_column='ASIN', blank=True, null=True)  # Field name made lowercase.
    kindle_asin = models.TextField(db_column='KINDLE_ASIN', blank=True, null=True)  # Field name made lowercase.
    format = models.TextField(db_column='FORMAT', blank=True, null=True)  # Field name made lowercase.
    is_ebook = models.TextField(db_column='IS_EBOOK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    book_desc = models.TextField(db_column='BOOK_DESC', blank=True, null=True)  # Field name made lowercase.
    similar_books = models.TextField(db_column='SIMILAR_BOOKS', blank=True, null=True)  # Field name made lowercase.
    link = models.TextField(db_column='LINK', blank=True, null=True)  # Field name made lowercase.
    edition_information = models.TextField(db_column='EDITION_INFORMATION', blank=True, null=True)  # Field name made lowercase.
    book_url = models.TextField(db_column='BOOK_URL', blank=True, null=True)  # Field name made lowercase.
    image_url = models.TextField(db_column='IMAGE_URL', blank=True, null=True)  # Field name made lowercase.
    title_without_series = models.TextField(db_column='TITLE_WITHOUT_SERIES', blank=True, null=True)  # Field name made lowercase.
    author_id = models.IntegerField(db_column='AUTHOR_ID', blank=True, null=True)  # Field name made lowercase.
    author_role = models.TextField(db_column='AUTHOR_ROLE', blank=True, null=True)  # Field name made lowercase.
    author_name = models.TextField(db_column='AUTHOR_NAME', blank=True, null=True)  # Field name made lowercase.
    author_average_rating = models.FloatField(db_column='AUTHOR_AVERAGE_RATING', blank=True, null=True)  # Field name made lowercase.
    author_text_reviews_count = models.IntegerField(db_column='AUTHOR_TEXT_REVIEWS_COUNT', blank=True, null=True)  # Field name made lowercase.
    author_ratings_count = models.IntegerField(db_column='AUTHOR_RATINGS_COUNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BUILD_WORK'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EngineApiAuthor(models.Model):
    author_id = models.IntegerField()
    name = models.CharField(max_length=255)
    text_reviews_count = models.IntegerField()
    ratings_count = models.IntegerField()
    average_rating = models.FloatField()

    class Meta:
        managed = False
        db_table = 'engine_api_author'


class EngineApiBook(models.Model):
    title = models.CharField(max_length=255)
    title_without_series = models.CharField(max_length=255)
    book_id = models.IntegerField()
    work_id = models.IntegerField()
    description = models.CharField(max_length=255)
    text_reviews_count = models.IntegerField()
    ratings_count = models.IntegerField()
    country_code = models.CharField(max_length=255)
    language_code = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    num_pages = models.IntegerField()
    link = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    publication_day = models.IntegerField()
    publication_month = models.IntegerField()
    publication_year = models.IntegerField()
    similar_books = models.CharField(max_length=255)
    edition_information = models.CharField(max_length=255)
    series = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    isbn13 = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    asin = models.CharField(max_length=255)
    kindle_asin = models.CharField(max_length=255)
    is_ebook = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'engine_api_book'


class ImportAuthors(models.Model):
    author_id = models.TextField(blank=True, null=False, primary_key=True)
    role = models.TextField(blank=True, null=True)
    book_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_authors'


class ImportBookAuthors(models.Model):
    average_rating = models.FloatField(blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=False, primary_key=True)
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
