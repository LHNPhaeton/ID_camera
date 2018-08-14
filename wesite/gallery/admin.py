from django.contrib import admin
from .models import Gallery, Text
# Register your models here.

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id','img','img_name','author','last_updated_time','created_time')

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            '/static/js/editor/kindeditor/kindeditor-all-min.js',
            '/static/js/editor/kindeditor/lang/zh_CN.js',
            '/static/js/editor/kindeditor/config.js',
        )

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','last_updated_time','created_time')

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            '/static/js/editor/kindeditor/kindeditor-all-min.js',
            '/static/js/editor/kindeditor/lang/zh_CN.js',
            '/static/js/editor/kindeditor/config.js',
        )
