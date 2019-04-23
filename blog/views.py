from django.db.models import Q
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import generic

from .models import Post,StablePage
from .forms import CommentCreateForm


class IndexView(generic.ListView):
    model = Post
    paginate_by = 9
    
    
    def get_queryset(self):
        queryset = Post.objects.order_by('-create_at')
        keyword = self.request.GET.get("keyword")
        if keyword:
            queryset = queryset.filter(
                    Q(title__icontains=keyword)|Q(pre_text__icontains=keyword)|Q(text__icontains=keyword)
                    )
        return queryset


class DetailAndCreate(ModelFormMixin,generic.DetailView):
    model = Post
    form_class = CommentCreateForm
    template_name = "blog/post_detail.html"
    
    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=post_pk)
        comment.save()
        return redirect('blog:detail', pk=post_pk)
    
    def post(self, request, *args,**kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            self.object = self.get_object()
            return self.form_invalid(form)
    
    
class CategoryView(generic.ListView):
    model = Post
    paginate_by = 10
    
    def get_queryset(self):
        category_pk = self.kwargs['pk']
        queryset = Post.objects.order_by('-create_at').filter(category__pk=category_pk)
        return queryset
    
class StablePageView(generic.DetailView):
    model = StablePage
    
