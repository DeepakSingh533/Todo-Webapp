from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .models import *
from .forms import *

# Create your views here.
@login_required(login_url='login')
def index(request):
	current_user = request.user
	user_name = current_user.username
	todo_list= todo.objects.filter(user_name__exact=user_name)
	#todo_list= todo.objects.order_by('id')


	total_todo=todo.objects.filter(user_name__exact=user_name).count()
	completed_todo =todo.objects.filter(user_name__exact=user_name,complete__exact=True).count()
	uncompleted_todo = todo.objects.filter(user_name__exact=user_name,complete__exact=False).count()
	
	
	
	

	form = TodoForm()


	context={'todo_list' : todo_list, 'form' : form,'total_todo':total_todo,'completed_todo':completed_todo,'uncompleted_todo':uncompleted_todo,'user_name':user_name}

	return render(request,'Todo/index.html',context)


@require_POST
def addTodo(request):
	form = TodoForm(request.POST)
	current_user = request.user
	user_name = current_user.username
	                                                                        
	if form.is_valid() :
		new_todo = todo(text=request.POST['text'],user_name=user_name)
		new_todo.save()


	return redirect('index')	



def completeTodo(request, Todo_id):
	Todo = todo.objects.get(pk = Todo_id)
	Todo.complete = True
	Todo.save()

	return redirect('index') 


def deletecompleted(request):
	current_user = request.user
	user_name = current_user.username
	todo.objects.filter(user_name__exact=user_name,complete=True).delete()
	return redirect('index')

def deleteall(request):
	current_user = request.user
	user_name = current_user.username
	todo.objects.filter(user_name__exact=user_name).delete()
	return redirect('index')	

#def delete(request):
#	todo.objects.get(pk= Todo_id).delete()

#	return redirect('index')	



#***************************************************************************************************************#


def signup_view(request):
	if request.method == 'GET':
		form = UserCreationForm()


	else:
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			
			#login here
			login(request,user)

			return redirect('index')	

	return render(request,'Todo/signup.html',{'form':form})


def login_view(request):
	if request.method == 'GET':
		form = AuthenticationForm()

	else:
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request,user)
			if 'next' in request.POST :
				return redirect(request.POST.get('next'))
			else:
				return redirect('index')
		

	return render(request,'Todo/login.html',{'form':form})
		

def logout_view(request):
	if request.method == 'POST':

		logout(request)

		return redirect('login')

	

#*****************************************************************************************************

def start(request):

	return render(request,'Todo/start.html')


def shortcut(request):
	return redirect('index')  
 	
