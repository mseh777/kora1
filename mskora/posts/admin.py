from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Posts, MatchDay
from django.utils.html import format_html
from django.urls import reverse
from django import forms
from django.utils.timezone import now



class UserPostCountFilter(admin.SimpleListFilter):
    title = "عدد الأخبار اليوم"
    parameter_name = "user_post_count"

    def lookups(self, request, model_admin):
        users = set(Posts.objects.filter(publish_date__date=now().date()).values_list("user__username", flat=True))
        return [(user, f"{user}") for user in users]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(user__username=self.value(), publish_date__date=now().date())
        return queryset

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'size': '80'}),
        }
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ['title', 'user','active','img_name','card_location', 'img_preview', 'publish_date','post_link']
    list_filter = ['user','card_location', UserPostCountFilter]
    search_fields = ['title', 'content']
    exclude = ('user',)
    ordering = ('-publish_date',)   
    change_form_template = 'admin/change_form.html'


    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)
    
    def img_preview(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;"/>', obj.img.url)
        return "No Image"


    img_preview.short_description = 'الصورة'



    # def post_link(self, obj):
        
    #     url = reverse('post', kwargs={'id': obj.id})
    #     return format_html('<a href="{}" target="_blank">مشاهدة الخبر</a>', url)

    # post_link.short_description = 'رابط الخبر'
    def post_link(self, obj):
        if not obj.slug:  # تأكد من أن slug موجود قبل محاولة إنشاء الرابط
            return "لا يوجد رابط"

        url = reverse('post', kwargs={'id': obj.id, 'slug': obj.slug})
        return format_html('<a href="{}" target="_blank">مشاهدة الخبر</a>', url)

    post_link.short_description = 'رابط الخبر'



admin.site.register(Posts, PostAdmin)

admin.site.register(MatchDay)

admin.site.unregister(Group)


admin.site.site_header = "إدارة AhlanKora"
admin.site.site_title = "لوحة تحكم AhlanKora"
admin.site.index_title = "مرحبًا بك في لوحة الإدارة"
