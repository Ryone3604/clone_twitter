from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView
from .models import Post, ProSetting
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, ProSettingForm
from django.contrib.auth.models import User


class PostListView(ListView):
    model = Post
    template_name = "tweet/index.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    def get_context_data(self,  **kwargs):
        id = self.request.user.id
        context = super(PostListView, self).get_context_data(**kwargs)
        context.update({
            'pro_list': ProSetting.objects.filter(author=id)
            
        })
        return context






class Profile(ListView):
    model = Post
    template_name = "tweet/profile.html"
    context_object_name = 'myposts'
    ordering = ['-date_posted']
    def get_queryset(self):
        id = self.request.user.id
        myposts = Post.objects.filter(author=id)
        myposts = myposts.order_by('-date_posted')
        return myposts


    
    def get_context_data(self,  **kwargs):
        id = self.request.user.id
        context = super(Profile, self).get_context_data(**kwargs)
        context.update({
            'pro_list': ProSetting.objects.filter(author=id)
            
        })
        return context

    def get_querysethh(request,self):
        id = self.request.user.id
        myposts = Post.objects.filter(author=id)
        myposts = myposts.order_by('-date_posted')
        return render(request, 'tweet/profile.html', {'myposts': myposts})



    def get_querysetuuuu(self):
       return Post.objects.order_by('-date_posted')


    
class ProfileListView(ListView):
    model = ProSetting
    template_name = "tweet/profile.html"
    context_object_name = 'profile'

    def p_list(request):
        ps = ProSetting.objects.all()
        ps = ps.order_by('-date_posted')
        return render(request, 'tweet/profile.html', {'ps': ps})

    




class PostCreateView(CreateView,LoginRequiredMixin):
    model = Post
    form_class = PostForm
    
    template_name = 'tweet/post_create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProSettingV(UpdateView,LoginRequiredMixin):
    
    model = ProSetting
    form_class = ProSettingForm
    
    
    template_name = 'tweet/pro_setting.html'
    success_url = '../../profile/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
   



class ProSettingVV(CreateView,LoginRequiredMixin):
    model = ProSetting
    form_class = ProSettingForm
    
    
    template_name = 'tweet/pro_setting3.html'
    success_url = '../../profile/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    





# Create your views here.
