from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=200, null=True, blank=False)
#     slug = models.SlugField(max_length=200, null=True, blank=False)
    
#     def __str__(self):
#         return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, null=True, blank=False)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    url = models.URLField(blank=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def save(self):
        self.slug = self.slug or slugify(self.title)
        super().save()

    def __str__(self):
        return self.title