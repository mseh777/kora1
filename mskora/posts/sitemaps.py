from django.contrib.sitemaps import Sitemap
from django.urls import reverse, get_resolver
from .models import Posts

class ArticleSitemap(Sitemap):
    changefreq = "daily"  
    priority = 0.8  
    protocol = "https"  

    def items(self):
        # return Posts.objects.all()
        return Posts.objects.filter(active=True)

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.publish_date

    def get_protocol(self, obj=None):
        return "https"

class StaticViewSitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"

    def items(self):
        return ['home', 'contact', 'about', 'rules', 'news', 'Championships', 'Transfers','Analytics','Social_Media','Professionals','Another_Sports']  


    def location(self, item):

        return reverse(item)
        
