# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Authors(models.Model):
    authorid = models.AutoField(db_column='authorId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'authors'


class Difficulties(models.Model):
    difficultid = models.PositiveIntegerField(db_column='difficultId', primary_key=True)  # Field name made lowercase.
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'difficulties'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
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


class Historic(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=100)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId')  # Field name made lowercase.
    itemname = models.TextField(db_column='itemName')  # Field name made lowercase.
    operationid = models.SmallIntegerField(db_column='operationId', db_comment='1->create, 2->update, 3->check, 4->uncheck, 5->delete')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    firebasesent = models.IntegerField(db_column='firebaseSent', blank=True, null=True)  # Field name made lowercase.
    remoteaddr = models.CharField(db_column='remoteAddr', max_length=45, blank=True, null=True)  # Field name made lowercase.
    originaldata = models.TextField(db_column='originalData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'historic'


class Images(models.Model):
    imageid = models.AutoField(db_column='imageId', primary_key=True)  # Field name made lowercase.
    recipeid = models.ForeignKey('Recipes', models.CASCADE, db_column='recipeId')  # Field name made lowercase.
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'images'


class Ingredients(models.Model):
    ingredientid = models.AutoField(db_column='ingredientId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_collation='utf8mb4_general_ci', blank=True, null=True)
    isproduct = models.TextField(db_column='isProduct', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ischecked = models.CharField(db_column='isChecked', max_length=1, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    comment = models.TextField(db_collation='utf8mb4_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredients'


class Log(models.Model):
    message = models.CharField(max_length=200, primary_key=True)
    datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log'


class Mealingredients(models.Model):
    mealid = models.OneToOneField('Meals', models.CASCADE, db_column='mealId', primary_key=True)  # Field name made lowercase. The composite primary key (mealId, ingredientId) found, that is not supported. The first column is selected.
    ingredientid = models.ForeignKey(Ingredients, models.CASCADE, db_column='ingredientId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mealingredients'
        unique_together = (('mealid', 'ingredientid'),)


class Meals(models.Model):
    mealid = models.AutoField(db_column='mealId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_collation='utf8mb4_general_ci', blank=True, null=True)
    islunch = models.IntegerField(db_column='isLunch')  # Field name made lowercase.
    ischecked = models.IntegerField(db_column='isChecked')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'meals'


class Notes(models.Model):
    noteid = models.AutoField(db_column='noteId', primary_key=True)  # Field name made lowercase.
    recipeid = models.ForeignKey('Recipes', models.CASCADE, db_column='recipeId')  # Field name made lowercase.
    note = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'notes'


class Operations(models.Model):
    operationid = models.IntegerField(db_column='operationId', primary_key=True)  # Field name made lowercase.
    authorid = models.IntegerField(db_column='authorId', blank=True, null=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='productId', blank=True, null=True)  # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'operations'


class Otherschild(models.Model):
    id = models.AutoField(primary_key=True)
    parentid = models.ForeignKey('Othersparent', models.CASCADE, db_column='parentId')  # Field name made lowercase.
    name = models.CharField(max_length=100)
    ischecked = models.IntegerField(db_column='isChecked')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'otherschild'


class Othersparent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'othersparent'


class Recipeingredients(models.Model):
    ingredientid = models.OneToOneField(Ingredients, models.CASCADE, db_column='ingredientId', primary_key=True)  # Field name made lowercase. The composite primary key (ingredientId, recipeId) found, that is not supported. The first column is selected.
    recipeid = models.ForeignKey('Recipes', models.CASCADE, db_column='recipeId')  # Field name made lowercase.
    number = models.CharField(max_length=50, db_collation='latin1_swedish_ci', blank=True, null=True)
    ingredientnote = models.CharField(db_column='ingredientNote', max_length=200, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recipeingredients'
        unique_together = (('ingredientid', 'recipeid'),)


class Recipes(models.Model):
    recipeid = models.AutoField(db_column='recipeId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=200)
    authorid = models.IntegerField(db_column='authorId')  # Field name made lowercase.
    date = models.DateField()
    views = models.PositiveIntegerField()
    preparationminutes = models.PositiveIntegerField(db_column='preparationMinutes', blank=True, null=True)  # Field name made lowercase.
    difficultyid = models.PositiveIntegerField(db_column='difficultyId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recipes'


class Recipetags(models.Model):
    tagid = models.OneToOneField('Tags', models.CASCADE, db_column='tagId', primary_key=True)  # Field name made lowercase. The composite primary key (tagId, recipeId) found, that is not supported. The first column is selected.
    recipeid = models.ForeignKey(Recipes, models.CASCADE, db_column='recipeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recipetags'
        unique_together = (('tagid', 'recipeid'),)


class Steps(models.Model):
    stepid = models.AutoField(db_column='stepId', primary_key=True)  # Field name made lowercase.
    recipeid = models.ForeignKey(Recipes, models.CASCADE, db_column='recipeId')  # Field name made lowercase.
    step = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'steps'


class Tags(models.Model):
    tagid = models.AutoField(db_column='tagId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tags'
