from django.urls import path, register_converter
from .views import all_posts, get_one_post, post_list_view, load_more_posts, about, rules, contact,match_day, analytics,transfers, championships , social_media, professionals, another_sports, post_redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ArticleSitemap, StaticViewSitemap
from django.http import HttpResponse
import re
from django.views.generic import TemplateView

# def robots_txt(request):
#     content = "User-agent: *\nDisallow: \nSitemap: https://yourdomain.com/sitemap.xml"
#     return HttpResponse(content, content_type="text/plain")

def robots_txt(request):
    domain = request.build_absolute_uri('/')[:-1]  # استخراج الدومين تلقائيًا
    content = f"User-agent: *\nDisallow:\nSitemap: {domain}/sitemap.xml"
    return HttpResponse(content, content_type="text/plain")

sitemaps = {
    'articles': ArticleSitemap(),
    'static': StaticViewSitemap(),
}



class UnicodeSlugConverter:
    regex = r'[-\w\u0600-\u06FF]+'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value

register_converter(UnicodeSlugConverter, 'unislug')




urlpatterns = [

    path('', all_posts, name='home'),
    path('news/', post_list_view, name='news'),
    path('matchday/', match_day, name='matchday'),

    path('load-more-posts/', load_more_posts, name='load_more_posts'),
    # path('load-more-posts-analytics/', load_more_posts_analytics, name='load_more_posts_analytics'),
    # path('load-more-posts-champ/', load_more_posts_champ, name='load_more_posts_champ'),


    path('about/', about, name='about'),
    path('rules/', rules, name='rules'),
    path('contact/', contact, name='contact'),

    path('championships/', championships, name='Championships'),
    path('transfers/', transfers, name='Transfers'),
    path('analytics/', analytics, name='Analytics'),

    path('socialmedia/', social_media, name='Social_Media'),

    path('professionals/', professionals, name='Professionals'),

    path('anothersports/', another_sports, name='Another_Sports'),


    path('<int:id>/<unislug:slug>/', get_one_post, name='post'),
    path('<int:id>/', post_redirect, name='post_redirect'),
    # path('<int:id>/<unislug:slug>/', get_one_post, name='post_detail_slug'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt),
    # path('google08c232de79890e37.html', TemplateView.as_view(template_name="google08c232de79890e37.html"), name='google-verification'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
















# from django.urls import path, register_converter
# from .views import all_posts, get_one_post, post_list_view, load_more_posts, about, rules, contact, match_day, analytics, transfers, championships, social_media, professionals, another_sports
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.sitemaps.views import sitemap
# from .sitemaps import ArticleSitemap, StaticViewSitemap
# from django.http import HttpResponse
# import re

# دالة إنشاء ملف robots.txt تلقائيًا
# def robots_txt(request):
#     domain = request.build_absolute_uri('/')[:-1]  # استخراج الدومين تلقائيًا
#     content = f"User-agent: *\nDisallow:\nSitemap: {domain}/sitemap.xml"
#     return HttpResponse(content, content_type="text/plain")

# # تعريف السيت ماب
# sitemaps = {
#     'articles': ArticleSitemap(),
#     'static': StaticViewSitemap(),
# }

# ✅ إنشاء محول مخصص لدعم الحروف العربية في slug
# class UnicodeSlugConverter:
#     regex = r'[-\w\u0600-\u06FF]+'

#     def to_python(self, value):
#         return value  # إرجاع القيمة كما هي

#     def to_url(self, value):
#         return value  # استخدام نفس القيمة في الرابط

# تسجيل الـ Converter الجديد في Django
# register_converter(UnicodeSlugConverter, 'unislug')

# قائمة المسارات
# urlpatterns = [
#     path('', all_posts, name='home'),
#     path('news/', post_list_view, name='news'),
#     path('matchday/', match_day, name='matchday'),
#     path('load-more-posts/', load_more_posts, name='load_more_posts'),
#     path('about/', about, name='about'),
#     path('rules/', rules, name='rules'),
#     path('contact/', contact, name='contact'),
#     path('championships/', championships, name='Championships'),
#     path('transfers/', transfers, name='Transfers'),
#     path('analytics/', analytics, name='Analytics'),
#     path('socialmedia/', social_media, name='Social_Media'),
#     path('professionals/', professionals, name='Professionals'),
#     path('anothersports/', another_sports, name='Another_Sports'),


#     path('<int:id>/<unislug:slug>/', get_one_post, name='post_detail_slug'),
#     path('<int:id>/', get_one_post, name='post'),

#     path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
#     path('robots.txt', robots_txt),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
