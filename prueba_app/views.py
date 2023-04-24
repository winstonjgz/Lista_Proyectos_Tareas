from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
#from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject


# Create your views here.
def index(request):
    title = 'Welcome to DJango!!!'
    #return HttpResponse("Index page")
    return render(request, "index.html", {'title': title})

def hello(request, username):
    return HttpResponse('<h1>Hola %s</h1>' % username)

def about(request):
    createdby = 'Winston Guzman'
    #return HttpResponse('<h2>About</h2>')
    return render(request, "about.html", {
        'createdby':createdby
    })

def projects(request):
    #projects = list(Project.objects.all())
    projects = Project.objects.all()
    
    #return JsonResponse(projects, safe=False)
    return render(request, "projects/projects.html", {'projects': projects})

def tasks(request):
#def tasks(request, id):
    #task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id)
    Tasks = Task.objects.all()
    #return HttpResponse('task: %s' % task.title)
    return render(request, "tasks/tasks.html", {'Tasks':Tasks})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {       'form': CreateNewTask()})
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2 )
        return redirect('tasks')
    #return render(request, 'create_task.html', {       'form': CreateNewTask()})

def create_projects(request):
    if request.method == 'GET':
        return render(request, 'projects/create_projects.html', {       'form': CreateNewProject()})
    else:
        Project.objects.create(name=request.POST['name'] )
        return redirect('projects')
    
def project_detail(request, id):
    #Project.objects.get(id=id)
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })