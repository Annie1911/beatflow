from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    nom_profile = models.CharField(max_length=255)
    nombre_abonner = models.IntegerField(default=0)

    def __str__(self):
        return self.nom_profile




class Post(models.Model):
    IMAGE_TYPES = [
        ('image/jpeg', 'Image JPEG'),
        ('image/png', 'Image PNG'),
        ('', 'Aucune')
    ]

    VIDEO_TYPES = [
        ('video/mp4', 'Vidéo MP4'),
        ('', 'Aucune')
    ]

    POST_TYPES = [
        ('text', 'Texte'),
        ('image', 'Image'),
        ('video', 'Vidéo')
    ]

    date_publication = models.DateTimeField(auto_now_add=True)
    date_modifier = models.DateTimeField(auto_now=True)
    nbre_like = models.PositiveIntegerField(default=0)
    type = models.CharField(max_length=10, choices=POST_TYPES, default='text')
    contenu = models.TextField()
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    video = models.FileField(upload_to='post_videos/', null=True, blank=True)




class Comment(models.Model):
    contenu_comment = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True)
    utili_comment = models.ForeignKey('User', on_delete=models.CASCADE) # Assurez-vous que le modèle d'utilisateur personnalisé est bien défini
    video_Associéé = models.ForeignKey('Post', on_delete=models.CASCADE) # Assurez-vous que le modèle Post est bien défini

    def __str__(self):
        return f"Commentaire par {self.utili_comment} sur {self.video_Associéé}"

