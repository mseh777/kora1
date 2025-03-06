from django.db import models
from django.contrib.auth.models import User
from django.db.models import SET_NULL
from django_quill.fields import QuillField
from django.utils.timezone import now
from PIL import Image
import os
from django.urls import reverse
from django.utils.text import slugify
import re
class Posts(models.Model):
    CARD_CHOICES = [
    ('1', 'Card left small'),
    ('2', 'Card center'),
    ('3', 'Card right small'),
    ('4', 'Card one'),
    ('5', 'Card two'),
    ('6', 'Card three'),
    ('7', 'Card Boss'),
    ('8', 'Card four'),
    ('9', 'Card five'),
    ('10', 'Card sex'),
    ('11', 'Card seven'),
    ('12', 'Card eight'),
    ('13', 'Card nine'),

    ('news', 'News'),
    
    ('gust_post', 'Gust_post'),

    ('champ', 'Championships'),

    ('analytics', 'Analytics'),

    ('trans', 'Transfers'),

    ('social', 'Social_Media'),

    ('prof', 'Professionals'),

    ('another_sports', 'Another_Sports'),


]
    user = models.ForeignKey(User, on_delete=SET_NULL , null=True)
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100, blank=True)
    content = QuillField()
    img = models.ImageField(upload_to='imgposts/', blank=True, null=True)
    img_name = models.CharField(max_length=50, null=True, blank=True)
    keywords = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=False)
    publish_date = models.DateTimeField(default=now, help_text="حدد وقت النشر")

    slug = models.SlugField(max_length=200, allow_unicode=True, unique=True, blank=True, null=True)

    card_location = models.CharField(
        max_length=30,
        choices=CARD_CHOICES,
        default='news',
        help_text="حدد مكان عرض البوست"
    )

    def get_absolute_url(self):
        return reverse("post", kwargs={"id": self.id, "slug": self.slug})

        # return reverse("post_detail_slug", kwargs={"id": self.id, "slug": self.slug})


    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super().save(*args, **kwargs)

        if self.img:
            img_path = self.img.path
            webp_path = os.path.splitext(img_path)[0] + ".webp"

            with Image.open(img_path) as img:
                img.save(webp_path, "WEBP", quality=80)


            self.img.name = self.img.name.rsplit(".", 1)[0] + ".webp"
            Posts.objects.filter(id=self.id).update(img=self.img.name)
            # super().save(*args, **kwargs)

    def is_published(self):
        """Checks if the post is ready to be published."""
        return self.publish_date <= now()

    def __str__(self):
        return self.title

def arabic_slugify(text):
    text = re.sub(r'[^\w\u0600-\u06FF\s-]', '', text)
    text = text.strip().replace(" ", "-")
    return slugify(text, allow_unicode=True) 


# def arabic_slugify(str):
#     str = str.replace(" ", "")
#     str = str.replace(",", "")
#     str = str.replace("(", "")
#     str = str.replace(")", "")
#     str = str.replace("؟", "")
#     str = str.replace(".", "")
#     str = str.replace(":", "")
#     str = str.replace("?", "")
#     str = str.replace("!", "")
#     str = str.replace("1", "")
#     str = str.replace("2", "")
#     str = str.replace("3", "")
#     str = str.replace("4", "")
#     str = str.replace("5", "")
#     str = str.replace("6", "")
#     str = str.replace("7", "")
#     str = str.replace("8", "")
#     str = str.replace("9", "")
#     str = str.replace("0", "")


#     return str
        


class MatchDay(models.Model):
    title = models.CharField(max_length=200, blank=True)
    content = QuillField(blank=True)
    img = models.ImageField(upload_to='imgposts/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.img:
            img_path = self.img.path
            webp_path = os.path.splitext(img_path)[0] + ".webp"

            with Image.open(img_path) as img:
                img.save(webp_path, "WEBP", quality=80)

            self.img.name = self.img.name.rsplit(".", 1)[0] + ".webp"
            # super().save(*args, **kwargs)
            MatchDay.objects.filter(id=self.id).update(img=self.img.name)

    def __str__(self):
        return self.title