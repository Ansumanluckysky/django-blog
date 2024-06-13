from django import forms

from blogs.models import Blog, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=Blog
        # fields='__all__'     -- Here we shouldn't give all becoz it allows the editor to select the author and he can select anyone where as he is the editor. Same for slug field as well.
        fields=('title','category','featured_image','short_description','blog_body','status','is_featured')
        