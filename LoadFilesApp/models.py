from django.db import models

# Create your models here:
class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    author = models.CharField(max_length=100, verbose_name="Автор")
    pdf = models.FileField(upload_to='books/pdf/', verbose_name="PDF-документ")
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True, verbose_name="Обложка")
    
    class Meta:
        verbose_name = "Название книги"
        verbose_name_plural = "Названия книг"
    
    def __str__(self):
        return self.title
        
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)