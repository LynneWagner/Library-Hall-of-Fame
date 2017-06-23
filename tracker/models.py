from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

#class CheckOut(models.Model):
 #   user = models.ForeignKey(User)
  #  date = models.DateField()
   # item = models.ForeignKey(Item)


class Book(models.Model):
    item = models.OneToOneField(Item, blank=True, null=True)
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    isbn = models.CharField(max_length=250)
    topic = models.CharField(max_length=250)
    book_cover = models.CharField(max_length=1000)


    @property
    def name(self):
        return self.item.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Book, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Books"

    def __str__(self):
        return self.name

class DVD(models.Model):
    item = models.OneToOneField(Item, blank=True, null=True)
    dvd_name = models.CharField(max_length=250)
    dvd_cover = models.CharField(max_length=250)

    @property
    def dvd_name(self):
        return self.item.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.dvd_name)
        super(DVD, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "DVD's"

    def __str__(self):
        return self.dvd_name


class Mags(models.Model):
    item = models.OneToOneField(Item, blank=True, null=True)
    mag_name = models.CharField(max_length=250)
    mag_cover = models.CharField(max_length=250)
    
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
    newspaper_name = models.CharField(max_length=250)
    newspaper_cover = models.CharField(max_length=250)
    
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


