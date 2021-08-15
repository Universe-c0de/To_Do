from django.db import models


class Venue(models.Model):
    name = models.CharField('Название места', max_length=120)
    address = models.CharField('Адрес', max_length=300)
    phone = models.CharField('Телефон', max_length=25)
    web = models.URLField('Веб-сайт')
    email_address = models.EmailField('Email')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Место проведения'
        verbose_name_plural = 'Места проведения'


class ToDoUser(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    Email = models.EmailField('Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Event(models.Model):
    name = models.CharField('Название события', max_length=120)
    event_date = models.DateTimeField('Дата проведения')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    # venue = models.CharField(max_length=120)
    manager = models.CharField('Задача', max_length=60)
    description = models.TextField('Описание', blank=True)
    attendees = models.ManyToManyField(ToDoUser, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

class Task(models.Model):
    title = models.CharField('название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'