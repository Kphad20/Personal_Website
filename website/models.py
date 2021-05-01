from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, null=True, blank=False)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    url = models.URLField(blank=True)

    class Meta:
        ordering = ['-date']

    def save(self):
        self.slug = self.slug or slugify(self.title)
        super().save()

    def __str__(self):
        return self.title