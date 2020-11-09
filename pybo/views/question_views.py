from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from ..models import Question
from ..forms import QuestionForm

@login_required(login_url='common:login')
def question_create(request): 
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.author = request.user
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)    

@login_required(login_url='common:login')
def question_modify(request, question_id): 
    question = get_object_or_404(Question, pk=question_id) 
    if question.author != request.user:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question_id)
        
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.author = request.user
            question.save()
            return redirect('pybo:detail', question_id=question_id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)  
    
@login_required(login_url='common:login')
def question_delete(request, question_id): 
    question = get_object_or_404(Question, pk=question_id) 
    if question.author != request.user:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question_id)
    question.delete()   
    return redirect('pybo:index')

