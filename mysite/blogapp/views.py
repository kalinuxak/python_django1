from _csv import reader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from .models import BlogPost, Image
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .forms import BlogPostForm, UploadPostForm, ImageForm




class PostsListView(ListView):
    template_name = 'blogapp/posts-list.html'
    queryset = BlogPost.objects.all()
    context_object_name = 'blogpost'

    class Meta:
        ordering=['-published_at',]

    # def get_queryset(self):
    #     queryset = BlogPost.objects.all()
    #     for post in queryset:
    #         if len(post.text) > 100:
    #             queryset.post.text = queryset.post.text[:100] + '...'
    #     return queryset

# class BlogPostCreateView(LoginRequiredMixin, CreateView):
#     login_url = '/blog/error/'
#     redirect_field_name = 'redirect_to'
#     model = BlogPost
#
#
#     def form_valid(self, form):
#         if self.request.user.id:
#             text = form.cleaned_data['text']
#             img = form.cleaned_data['img']
#             BlogPost.objects.create(text=text, img=img, user_id=self.request.user.id)
#             return HttpResponseRedirect(reverse_lazy('blogapp:posts-list'))
#         else:
#             return redirect(reverse('blogapp:login-error'))


# def create_post(request: HttpRequest):
#     if request.method == 'POST':
#         if request.user.id:
#             post_form = BlogPostForm(request.POST, instance=BlogPost())
#             img_form = ImageForm(request.POST, request.FILES)
#             if post_form.is_valid() and img_form.is_valid():
#                 new_post = post_form.save(commit=False)
#                 new_post.instance.user_id = request.user.id
#                 new_post.save()
#                 files = request.FILES.getlist('img')
#                 for image in files:
#                     new_img = img_form.save(commit=False)
#                     new_img.post = new_post
#                     new_img.save()
#                 return HttpResponseRedirect(reverse_lazy('blogapp:posts-list'))
#         else:
#             return redirect(reverse('blogapp:login_error'))
#     else:
#         post_form = BlogPostForm()
#         return render(request, 'blogapp/post_form.html', {'form': post_form})


def create_post(request: HttpRequest):
    if request.method == 'POST':
        post_form = BlogPostForm(request.POST, request.FILES)
        if request.user.id:
            if post_form.is_valid():
                text = post_form.cleaned_data['text']
                images = post_form.cleaned_data['img']
                post = BlogPost.objects.create(text=text, user_id=request.user.id)
                # for image in images:  todo точнее так:
                for image in request.FILES.getlist('img'):
                    Image.objects.create(img=image, post=post)
                return HttpResponseRedirect(reverse_lazy('blogapp:posts-list'))
            else:
                render(request, 'blogapp/post_form.html', {'form': post_form})
        else:
            return redirect(reverse('blogapp:login_error'))
    else:
        post_form = BlogPostForm()
        return render(request, 'blogapp/post_form.html', {'form': post_form})



# class PostCreateView(FormView):
#     form_class = BlogPostForm
#     template_name = 'post_form.html'
#     success_url = reverse_lazy('blogapp:posts-list')
#
#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('img')
#         if form.is_valid():
#             form.save()
#             for f in files:
#                 Image.objects.create(img=f)
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)



class PostDetailView(DetailView):
    template_name = 'blogapp/post_detail.html'
    model = BlogPost
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.filter(post=self.object.pk)
        return context


class LoginErrorView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'blogapp/login-error.html')


def upload_post(request: HttpRequest):
    if request.method == 'POST':
        upload_post_form = UploadPostForm(request.POST, request.FILES)
        if upload_post_form.is_valid():
            file = upload_post_form.cleaned_data['file'].read()
            post_str = file.decode('utf-8').split('\n')
            csv_reader = reader(post_str, delimetr=',', quotechar='"')
            for row in csv_reader:
                BlogPost.objects.create(text=row[0], date=row[1])
            return redirect(reverse('blogapp:posts-list'))
    else:
        upload_post_form = UploadPostForm()
        return render(request, 'blogapp/upload-posts.html', {'form': upload_post_form})

