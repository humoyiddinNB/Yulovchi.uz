from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import View
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import Project
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie


def homePageView(request):
    return render(request,'index.html')


class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'posts.html', {'posts' : posts})


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            full_message = f"From: {name} <{email}>\n\nMessage:\n{message}"

            try:
                send_mail(
                    subject=f"New message from {name}",
                    message=full_message,
                    from_email='defendereviver71@gmail.com',
                    recipient_list=['defendereviver71@gmail.com'],
                    fail_silently=False,
                )
                return JsonResponse({'success': True, 'message': 'Xabaringiz muvaffaqiyatli yuborildi!'})
            except Exception as e:
                return JsonResponse({'success': False, 'message': f'Xatolik yuz berdi: {str(e)}'})
        else:
            errors = {field: errors[0] for field, errors in form.errors.items()}
            return JsonResponse({'success': False, 'errors': errors})



class ProjectsView(View):
    def get(self, request):
        all_projects = Project.objects.all()
        return render(request, 'projects.html', {'all_projects' : all_projects})





@method_decorator(csrf_exempt, name='dispatch')
class ProjectDetailView(View):
    def get(self, request, id):
        project = get_object_or_404(Project, pk=id)
        project.views += 1
        project.save()
        return render(request, 'project_detail.html', {'project': project})

    def post(self, request, id):
        if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

        project = get_object_or_404(Project, pk=id)
        project.likes += 1
        project.save()
        return JsonResponse({
            'success': True,
            'message': 'Like qo‘shildi!',
            'likes': project.likes
        })

    def delete(self, request, id):
        if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

        project = get_object_or_404(Project, pk=id)
        if project.likes > 0:
            project.likes -= 1
            project.save()
        return JsonResponse({
            'success': True,
            'message': 'Like olib tashlandi!',
            'likes': project.likes
        })


def post_list(request):
    posts = Post.objects.all()
    # Like bosgan postlar saqlanadi (aslida biz localStorage ishlatyapmiz,
    # lekin sayt uchun auth bo'lgan foydalanuvchilar uchun shu usul ham qo'shilishi mumkin)
    liked_posts = []

    context = {
        'posts': posts,
        'liked_posts': liked_posts,
    }
    return render(request, 'posts/post_list.html', context)


@require_POST
def post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.views += 1
    post.save()
    return JsonResponse({'success': True, 'views': post.views})

@require_POST
def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    data = json.loads(request.body)
    if data.get('liked'):
        post.likes += 1
    else:
        post.likes -= 1
    post.save()
    return JsonResponse({'success': True, 'likes': post.likes})