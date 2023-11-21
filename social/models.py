from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.views import PasswordResetConfirmView


# Create your models here.
class Profile(models.Model):
    SECURITY_QUESTION_CHOICES = [
        ('1', '¿Cuál es el nombre de tu primera mascota?'),
        ('2', '¿Cuál es tu ciudad de nacimiento?'),
        ('3', '¿Cuál es tu libro favorito?'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='foto.png')
    favorites = models.ManyToManyField('Post', related_name='favorited_by')
    created_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    deleted_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    pregunta_seguridad = models.CharField(max_length=1, choices=SECURITY_QUESTION_CHOICES, null=True, default="")  
    respuesta_seguridad = models.CharField(max_length=100, null=True, default="")
    def __str__(self):
        return f'Perfil de {self.user.username}'
    def get_following(self):
        user_ids = Relationship.objects.filter(from_user=self.user) \
            .values_list('to_user__id', flat=True)
        return User.objects.filter(id__in=user_ids)

    def get_followers(self):
        user_ids = Relationship.objects.filter(to_user=self.user) \
            .values_list('from_user__id', flat=True)
        return User.objects.filter(id__in=user_ids)
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField(blank=True, null=True)
    post_title = models.CharField(max_length=200, blank=True, null=True)
    picture = models.ImageField(blank=True, null=True, upload_to='')
    deleted_date = models.DateTimeField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    key_result = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}:{self.content}'


class Relationship(models.Model):
    from_user=models.ForeignKey(User,related_name='relationships',on_delete=models.CASCADE)
    to_user=models.ForeignKey(User,related_name='related_to',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.from_user} to {self.to_user}'
    
    class Meta:
        indexes=[
            models.Index(fields=['from_user','to_user']),

        ]
class ExtendedData(models.Model):
    TYPE_CHOICES = [("A", "Artista"), ("S", "Sponsor")]

    SECURITY_QUESTION_CHOICES = [
        ('1', '¿Cuál es el nombre de tu primera mascota?'),
        ('2', '¿Cuál es tu ciudad de nacimiento?'),
        ('3', '¿Cuál es tu libro favorito?'),
    ]

    user_type = models.CharField(max_length=1, choices=TYPE_CHOICES, null=True,verbose_name="tipo de usuario")
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE,default="")
    pregunta_seguridad = models.CharField(max_length=1, choices=SECURITY_QUESTION_CHOICES, null=True, default="")
    respuesta_seguridad = models.CharField(max_length=100, null=True, default="")
    
    def __str__(self):
        return f'{self.user.username} - {self.user_type}'