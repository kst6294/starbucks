from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=45)
    class Meta:
        db_table = 'menus'

class Category(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, null = True)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'

class Drink(models.Model):
    korean_name     = models.CharField(max_length=45)
    english_name    = models.CharField(max_length=45)
    description     = models.TextField()
    menu            = models.ForeignKey('Menu', on_delete = models.CASCADE, null = True)
    category        = models.ForeignKey('Category', on_delete = models.CASCADE, null = True)
    allergy         = models.ManyToManyField('Allergy', through = 'Allergy_Drink')
    class Meta:
        db_table = 'drinks'

class Allergy(models.Model):
    name = models.CharField(max_length=45)
    class Meta:
        db_table = 'allergies'

class Allergy_Drink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete = models.CASCADE, null = True)
    drink = models.ForeignKey('Drink', on_delete = models.CASCADE, null = True)
    class Meta:
        db_table = 'allergies_drinks'

class Url(models.Model):
    url = models.CharField(max_length=1000)
    drink = models.ForeignKey('Drink', on_delete = models.CASCADE, null = True)
    class Meta:
        db_table = 'urls'

class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey(Drink, on_delete = models.CASCADE)
    class Meta:
        db_table = 'images'

class Nutrition(models.Model):
    one_serving_kca = models.DecimalField(max_digits=10, decimal_places=2)
    sodium_mg       = models.DecimalField(max_digits=10, decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2)
    sugars_g        = models.DecimalField(max_digits=10, decimal_places=2)
    protein_g       = models.DecimalField(max_digits=10, decimal_places=2)
    caffeine_mg     = models.DecimalField(max_digits=10, decimal_places=2)
    drink           = models.ForeignKey(Drink, on_delete = models.CASCADE, null = True)
    class Meta:
        db_table = 'nutritions'

