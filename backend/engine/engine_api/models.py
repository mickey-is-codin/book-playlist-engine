# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Playlist(models.Model):
    playlist_id = models.IntegerField()
    work_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)


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


class BuildWorkKeyed(models.Model):
    isbn = models.IntegerField(blank=True, null=True)
    text_reviews_count = models.IntegerField(blank=True, null=True)
    series = models.TextField(blank=True, null=True)
    country_code = models.TextField(blank=True, null=True)
    language_code = models.TextField(blank=True, null=True)
    asin = models.TextField(blank=True, null=True)
    is_ebook = models.IntegerField(blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    kindle_asin = models.TextField(blank=True, null=True)
    similar_books = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    format = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    num_pages = models.IntegerField(blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    publication_day = models.IntegerField(blank=True, null=True)
    isbn13 = models.IntegerField(blank=True, null=True)
    publication_month = models.IntegerField(blank=True, null=True)
    edition_information = models.TextField(blank=True, null=True)
    publication_year = models.IntegerField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    book_id = models.IntegerField(blank=True, null=True)
    ratings_count = models.IntegerField(blank=True, null=True)
    work_id = models.AutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    title_without_series = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'build_work_keyed'


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


class ImportAuthorsKeyed(models.Model):
    author_id = models.AutoField(primary_key=True)  # The composite primary key (author_id, book_id) found, that is not supported. The first column is selected.
    book_id = models.IntegerField()
    role = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_authors_keyed'


class ImportBookAuthorsKeyed(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.TextField(blank=True, null=True)
    author_average_rating = models.FloatField(blank=True, null=True)
    author_text_reviews_count = models.IntegerField(blank=True, null=True)
    author_ratings_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_book_authors_keyed'


class ImportBookInteractionsKeyed(models.Model):
    user_id = models.AutoField(primary_key=True)  # The composite primary key (user_id, book_id) found, that is not supported. The first column is selected.
    book_id = models.IntegerField()
    is_read = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    is_reviewed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_book_interactions_keyed'


class ImportBooksKeyed(models.Model):
    isbn = models.IntegerField(blank=True, null=True)
    text_reviews_count = models.IntegerField(blank=True, null=True)
    series = models.TextField(blank=True, null=True)
    country_code = models.TextField(blank=True, null=True)
    language_code = models.TextField(blank=True, null=True)
    asin = models.TextField(blank=True, null=True)
    is_ebook = models.IntegerField(blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    kindle_asin = models.TextField(blank=True, null=True)
    similar_books = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    format = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    num_pages = models.IntegerField(blank=True, null=True)
    publication_day = models.IntegerField(blank=True, null=True)
    isbn13 = models.IntegerField(blank=True, null=True)
    publication_month = models.IntegerField(blank=True, null=True)
    edition_information = models.TextField(blank=True, null=True)
    publication_year = models.IntegerField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    book_id = models.AutoField(primary_key=True)
    ratings_count = models.IntegerField(blank=True, null=True)
    work_id = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    title_without_series = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_books_keyed'


class ImportShelvesKeyed(models.Model):
    work_id = models.AutoField(primary_key=True)  # The composite primary key (work_id, tag_name) found, that is not supported. The first column is selected.
    tag_name = models.TextField()
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_shelves_keyed'
