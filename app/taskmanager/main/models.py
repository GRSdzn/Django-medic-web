from django.db import models


# Симптомы
class Symptoms(models.Model):
    title = models.CharField('Название', max_length=50)
    info = models.TextField('Описание')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'симптом'
        verbose_name_plural = 'симптомы'


class Causes(models.Model):
    title = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Причина болезни'
        verbose_name_plural = 'Причины болезней'


# Болезни
class Diseases(models.Model):
    title = models.CharField('Название', max_length=50)
    info = models.TextField('Описание')
    symptoms = models.ManyToManyField(Symptoms, verbose_name='Симптомы', related_name='diseases', blank=True)
    causes = models.ManyToManyField(Causes, verbose_name='Причины болезни', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'болезнь'
        verbose_name_plural = 'болезни'


class Questions(models.Model):
    title = models.CharField('Название', max_length=50)
    question = models.TextField('Вопрос')
    email = models.CharField('Почта', max_length=50)
    datetime = models.DateTimeField('Дата', auto_now_add=True)

    def __str__(self):
        return f"{self.email} {self.title}: {self.datetime}"

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
        ordering = ['-datetime']