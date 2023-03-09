from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .filters import LessonFilter
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from ll.auth_helper import get_sign_in_url, get_token_from_code, store_token, store_user, remove_user_and_token, get_token
from ll.graph_helper import get_user
import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from datetime import datetime
from .resources import LessonResource
now = timezone.now()

def home(request):
  context = initialize_context(request)
  return render(request, 'll/home.html', context)

def initialize_context(request):
  context = {}

  # Check for any errors in the session
  error = request.session.pop('flash_error', None)

  if error != None:
    context['errors'] = []
    context['errors'].append(error)

  # Check for user in the session
  context['user'] = request.session.get('user', {'is_authenticated': False})
  return context

def sign_in(request):
  # Get the sign-in URL
  sign_in_url, state = get_sign_in_url()
  # Save the expected state so we can validate in the callback
  request.session['auth_state'] = state
  # Redirect to the Azure sign-in page
  return HttpResponseRedirect(sign_in_url)

def callback(request):
  # Get the state saved in session
  expected_state = request.session.pop('auth_state', '')
  # Make the token request
  token = get_token_from_code(request.get_full_path(), expected_state)

  # Get the user's profile
  user = get_user(token)

  # Save token and user
  store_token(request, token)
  store_user(request, user)

  return HttpResponseRedirect(reverse('ll:home'))

def sign_out(request):
  # Clear out the user and token
  remove_user_and_token(request)

  return HttpResponseRedirect(reverse('ll:home'))

def lesson_delete(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    lesson.delete()
    return redirect('ll:lesson_list')

def lesson_new(request):
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.created_date = timezone.now()
            lesson.author = request.session.get('user')
            lesson.save()
            lessons = Lesson.objects.filter(created_date__lte=timezone.now())
            return render(request, 'll/add_confirmation.html',
                          {'lessons': lessons})
    else:
        form = LessonForm()
        # print("Else")
    return render(request, 'll/lesson_new.html', {'form': form})


def lesson_edit(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == "POST":
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            lesson = form.save()
            # lesson.customer = lesson.id
            lesson.updated_date = timezone.now()
            lesson.save()
            lessons = Lesson.objects.filter(created_date__lte=timezone.now())
            return render(request, 'll/edit_confirmation.html', {'lessons': lessons})
    else:
        # print("else")
        form = LessonForm(instance=lesson)
    return render(request, 'll/lesson_edit.html', {'form': form})

def search(request):
    lesson_list = Lesson.objects.all()
    lesson_filter = LessonFilter(request.GET, queryset=lesson_list)
    return render(request, 'search/user_list.html', {'filter': lesson_filter})

def export_Lessons_toCSV(request):
    lesson_resource = LessonResource()
    dataset = lesson_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="lessons.csv"'
    return response





