from django.shortcuts import redirect, render
from django.urls import reverse
from .models import TodoModel
from django.views import View
from .forms import AddTodoForm
from django.contrib.auth.models import User
from utils.get_ip import get_user_ip


def index(request):
    ip = get_user_ip(request)
    user, create = User.objects.get_or_create(username=ip)

    if request.method == 'POST':
        if delete := request.POST.get('delete'):
            d_todo = TodoModel.objects.filter(id=delete).delete()
            return redirect('/')

        if is_done := request.POST.get('is_done'):
            todo = TodoModel.objects.filter(id=is_done).first()
            todo.is_done = True
            todo.save()
            return redirect('/')

        form = AddTodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            if len(title) > 0 and not TodoModel.objects.filter(title=title).exists():
                c_todo = TodoModel.objects.create(owner=user, title=title)
                return redirect('/')

            form.add_error('title', 'the title cannot be empty or title is exists')
            
        return render(request, 'todo_app/index.html', {'form': form})

    form = AddTodoForm()

    todos = TodoModel.objects.filter(owner=user).order_by('created')
    return render(request, 'todo_app/index.html', {'todos': todos, 'form': form})


def todo_detail(request, slug):
    todo = TodoModel.objects.filter(slug=slug).first()

    if request.method == 'POST':
        description = request.POST.get('description')
        if description is not None:
            todo.description = description
            todo.save()
            return redirect(reverse('todo_detail', kwargs={'slug': todo.slug}))

    return render(request, 'todo_app/detail.html', {'todo': todo})
