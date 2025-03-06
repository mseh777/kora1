from django.shortcuts import render
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts
from django.http import JsonResponse
from django.utils.timezone import now
from datetime import timedelta
from .models import Posts, MatchDay
# Create your views here.
def all_posts(request):
    myposts = Posts.objects.filter(active=True, publish_date__lte=now()).order_by('-publish_date')      
    
    Card_left_small = Posts.objects.filter(card_location='1', active=True, publish_date__lte=now()).order_by('-publish_date').first()
    Card_center = Posts.objects.filter(card_location='2', active=True, publish_date__lte=now()).order_by('-publish_date').first()
    Card_right_small = Posts.objects.filter(card_location='3', active=True, publish_date__lte=now()).order_by('-publish_date').first()

    Card_one = Posts.objects.filter(card_location='4', active=True, publish_date__lte=now()).order_by('-publish_date').first()
    Card_two = Posts.objects.filter(card_location='5', active=True, publish_date__lte=now()).order_by('-publish_date').first()
    Card_three = Posts.objects.filter(card_location='6', active=True, publish_date__lte=now()).order_by('-publish_date').first()
    Card_Boss = Posts.objects.filter(card_location='7', active=True, publish_date__lte=now()).order_by('-publish_date').first()
    Card_four = Posts.objects.filter(card_location='8', active=True, publish_date__lte=now()).order_by('-publish_date').first()
    Card_five = Posts.objects.filter(card_location='9', active=True, publish_date__lte=now()).order_by('-publish_date').first()
    Card_sex = Posts.objects.filter(card_location='10', active=True, publish_date__lte=now()).order_by('-publish_date').first()
    Card_seven = Posts.objects.filter(card_location='11', active=True, publish_date__lte=now()).order_by('-publish_date').first()
    Card_eight = Posts.objects.filter(card_location='12', active=True, publish_date__lte=now()).order_by('-publish_date').first()
    Card_nine = Posts.objects.filter(card_location='13', active=True, publish_date__lte=now()).order_by('-publish_date').first()




    other_posts = Posts.objects.filter(card_location='news', active=True, publish_date__lte=now())


    gust_post = Posts.objects.filter(card_location='gust_post', active=True, publish_date__lte=now())

    champ = Posts.objects.filter(card_location='Championships', active=True, publish_date__lte=now())

    trans = Posts.objects.filter(card_location='Transfers', active=True, publish_date__lte=now())

    analy = Posts.objects.filter(card_location='analytics', active=True, publish_date__lte=now())

    social = Posts.objects.filter(card_location='Social_Media', active=True, publish_date__lte=now())

    prof = Posts.objects.filter(card_location='Professionals', active=True, publish_date__lte=now())

    another_sports = Posts.objects.filter(card_location='Another_Sports', active=True, publish_date__lte=now())

    # return render(request, 'home.html', {'myposts': myposts})
    return render(request, 'home.html', {
        'myposts': myposts,
        'Card_left_small': Card_left_small,
        'Card_center': Card_center,
        'Card_right_small': Card_right_small,
        'Card_one': Card_one,
        'Card_two': Card_two,
        'Card_three': Card_three,
        'Card_Boss': Card_Boss,
        'Card_four': Card_four,
        'Card_five': Card_five,
        'Card_sex': Card_sex,
        'Card_seven': Card_seven,
        'Card_eight': Card_eight,
        'Card_nine': Card_nine,
        'other_posts': other_posts,
        'gust_post':gust_post,
        'champ':champ,
        'trans':trans,
        'analytics':analy,
        'social':social,
        'prof':prof,
        'another_sports':another_sports,
        })


def championships(request):
    champ = Posts.objects.filter(active=True, card_location='champ').order_by('-publish_date')[:25]
    return render(request, 'pages/Championships.html', {'champ':champ,})

def transfers(request):

    trans = Posts.objects.filter(active=True, card_location='trans').order_by('-publish_date')[:25]
    return render(request, 'pages/Transfers.html',{'trans':trans,})

def analytics(request):

    analy = Posts.objects.filter(active=True, card_location='analytics').order_by('-publish_date')[:25]
    return render(request, 'pages/Analytics.html', {'analy':analy,})


def social_media(request):

    social = Posts.objects.filter(active=True, card_location='social').order_by('-publish_date')[:25]
    return render(request, 'pages/Social_Media.html',{'social':social,})


def professionals(request):

    prof = Posts.objects.filter(active=True, card_location='prof').order_by('-publish_date')[:25]
    return render(request, 'pages/Professionals.html',{'prof':prof,})


def another_sports(request):

    another_spo = Posts.objects.filter(active=True, card_location='another_sports').order_by('-publish_date')[:25]
    return render(request, 'pages/another_sports.html',{'another_spo':another_spo,})


def post_redirect(request, id):

    post = get_object_or_404(Posts, id=id)

    if not post.slug:
        from django.utils.text import slugify
        post.slug = slugify(post.title)
        post.save()
    return redirect('post', id=post.id, slug=post.slug)

def get_one_post(request, id, slug=None):

    onepost = get_object_or_404(Posts, id=id)

        # if not slug or slug != onepost.slug:
    #     return redirect('post', id=id, slug=onepost.slug, permanent=True)

    related_posts = Posts.objects.exclude(id=onepost.id).order_by('-publish_date')[:6]

    context = {
        'onepost': onepost,
        'related_posts': related_posts,
    }
    return render(request, 'onepost.html', context)

def post_list_view(request):
    return render(request, 'pages/news.html')


def match_day(request):
    # matchd = MatchDay.objects.all()
    matchd = MatchDay.objects.order_by('-id').first()
    return render(request, 'pages/matchday.html', {'matchd': matchd})


def load_more_posts(request):
    page = int(request.GET.get('page', 1))
    posts_per_page = 10
    start = (page - 1) * posts_per_page
    end = start + posts_per_page
    posts = Posts.objects.filter(card_location='news', active=True).order_by("-publish_date")[start:end]
    data = [
        {
            "id": post.id, 
            "slug": post.slug,
            "title": post.title,
            "writer": post.writer,
            "publish_date": post.publish_date.strftime('%d/%m/%Y') if post.publish_date else None,
            "img": post.img.url if post.img else None,
        }
        for post in posts
    ]
    return JsonResponse({"posts": data})

# def load_more_posts_analytics(request):
#     page = int(request.GET.get('page', 1))
#     posts_per_page = 10
#     start = (page - 1) * posts_per_page
#     end = start + posts_per_page
#     posts = Posts.objects.filter(card_location='analytics', active=True).order_by("-publish_date")[start:end]
#     data = [
#         {
#             "id": post.id, 
#             "slug": post.slug,
#             "title": post.title,
#             "writer": post.writer,
#             "publish_date": post.publish_date.strftime('%d/%m/%Y') if post.publish_date else None,
#             "img": post.img.url if post.img else None,
#         }
#         for post in posts
#     ]
#     return JsonResponse({"posts": data})

# def load_more_posts_champ(request):
#     page = int(request.GET.get('page', 1))
#     posts_per_page = 10
#     start = (page - 1) * posts_per_page
#     end = start + posts_per_page
#     posts = Posts.objects.filter(card_location='champ', active=True).order_by("-publish_date")[start:end]
#     data = [
#         {
#             "id": post.id, 
#             "slug": post.slug,
#             "title": post.title,
#             "writer": post.writer,
#             "publish_date": post.publish_date.strftime('%d/%m/%Y') if post.publish_date else None,
#             "img": post.img.url if post.img else None,
#         }
#         for post in posts
#     ]
#     return JsonResponse({"posts": data})







def about(request):
    return render(request, 'pages/about.html')

def rules(request):
    return render(request, 'pages/rules.html')

def contact(request):
    return render(request, 'pages/contact.html')