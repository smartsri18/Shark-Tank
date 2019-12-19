from django.db import models

# Season model.
class Season(models.Model):
    season_number = models.IntegerField()

    def __str__(self):
        name = "Season "
        return name+str(self.season_number)

# Episode model.
class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='etb_season', null=True)
    episode_number = models.IntegerField()

    def __str__(self):
        l_name = " Episode "
        return str(self.season)+l_name+str(self.episode_number)

# Company model.
class Company(models.Model):
    showlist = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='showlist', null=True)
    company_name = models.CharField(max_length=500)
    deal = models.CharField(max_length=10)
    industry = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    amount = models.CharField(max_length=100)
    equity = models.CharField(max_length=20)
    valuation = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name

# Product model.
class Product(models.Model):
    showlist = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='prod_showlist', null=True)
    product_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=30)
    investors = models.CharField(max_length=255)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='product', null=True, blank=True)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.product_name
