from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,TemplateView
from django.views.generic.edit import FormMixin
from manage_post.models import Article, Category
from manage_post.forms import CommentForm
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
class IndiceView(ListView):
    model = Article
    template_name = 'manage_post/indice.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)

        #Enviar articulos activos estado=true
        context['articles'] = Article.objects.filter(status=True)

        #Obtener categorias destacadas
        context['navbar_category'] = Category.objects.filter(featured=True)
        return context
        
        
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'manage_post/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #Enviar articulos activos de acuerdo a su categoria
        context['articles'] = Article.objects.filter(status=True).filter(
            categories=Category.objects.get(slug=self.kwargs['slug'])
        )

        # Obtener categorias destacadas
        context['navbar_category'] = Category.objects.filter(featured=True)
        return context

class ListAllCategoriesView(ListView):
    model = Category
    template_name = 'manage_post/category_list.html'
    context_object_name = 'categories'

class ShowPostDetailView(FormMixin, DetailView):
    model = Article
    template_name = 'manage_post/article_detail.html'
    form_class = CommentForm
    context_object_name = 'article'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.article_id = Article.objects.get(slug=self.kwargs['slug'])
        form.instance.user_id = User.objects.get(id=self.request.user.id)

        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'slug': self.kwargs['slug']})
    
class IndexView(ListView):
    model=Article
    template_name = 'manage_post/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #Enviar articulos featured estado=true
        context['destacados'] = Article.objects.filter(featured=True)

        #Enviar articulos activos estado=true
        context['articles'] = Article.objects.filter(status=True)
        return context
    
class NosotrosView(ListView):
    model=Article
    template_name = 'manage_post/nosotros.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #Enviar articulos featured estado=true
        context['destacados'] = Article.objects.filter(featured=True)

        #Enviar articulos activos estado=true
        context['articles'] = Article.objects.filter(status=True)

class ContactoView(ListView):
    model=Article
    template_name = 'manage_post/contacto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #Enviar articulos featured estado=true
        context['destacados'] = Article.objects.filter(featured=True)

        #Enviar articulos activos estado=true
        context['articles'] = Article.objects.filter(status=True)

        