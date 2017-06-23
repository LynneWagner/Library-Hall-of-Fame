from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=250, unique=True)
    creator = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

#class CheckOut(models.Model):
 #   user = models.ForeignKey(User)
  #  date = models.DateField()
   # item = models.ForeignKey(Item)


class Book(models.Model):
    item = models.OneToOneField(Item, blank=True, null=True)
    topic = models.CharField(max_length=250)
    isbn = models.CharField(max_length=250)


    @property
    def author(self):
        return self.item.creator
    
    @property
    def name(self):
        return self.item.name

    @property
    def book_cover(self):
        return self.item.description

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Book, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Books"

    def __str__(self):
        return self.name

class DVD(models.Model):
    item = models.OneToOneField(Item, blank=True, null=True)
    @property
    def dvd_name(self):
        return self.item.name

    @property
    def dvd_cover(self):
        return self.item.description

    def save(self, *args, **kwargs):
        self.slug = slugify(self.dvd_name)
        super(DVD, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "DVD's"

    def __str__(self):
        return self.dvd_name


class Mags(models.Model):
    item = models.OneToOneField(Item, blank=True, null=True)
    
    @property
    def mag_name(self):
        return self.item.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.mag_name)
        super(Mags, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Magazines"

    def __str__(self):
        return self.mag_name

class Newspaper(models.Model):
    item = models.OneToOneField(Item, blank=True, null=True)
    
    @property
    def newspaper_name(self):
        return self.item.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.newspaper_name)
        super(Newspaper, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Newspapers"

    def __str__(self):
        return self.newspaper_name

class Music(models.Model):
    item = models.OneToOneField(Item, blank=True, null=True)
    
    @property
    def album(self):
        return self.item.name
    
    @property
    def artist(self):
        return self.item.creator


    def save(self, *args, **kwargs):
        self.slug = slugify(self.album)
        super(Music, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Music"

    def __str__(self):
        return self.album


