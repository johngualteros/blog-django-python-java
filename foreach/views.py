
from django.shortcuts import render,redirect
from .models import Comment
# Create your views here.
def index(request):
    comments=Comment.objects.all()
    return render(request, 'index.html', {'comments':comments})

def create_comment(request):
    comment=Comment(description=request.POST['description'])
    comment.save()
    print(request.POST)
    return redirect('/foreach/')
    
def delete_comment(request,comment_id):
    comment=Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('/foreach/')

def error404(request, exception):
    return render(request, exception, '404.html')
