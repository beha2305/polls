from django.shortcuts import render, HttpResponse
from .models import Questions, Answers
def response(request):
    print(request.method)
    text = Questions.objects.all()
    return render(request, 'poll.html', {'ques' : text} )
def ans(request, question_id):
    print(request.method)
    question_name = Questions.objects.get(pk=question_id)
    text = Answers.objects.filter(question_id = question_id)
    return render(request, 'ans.html', {'text':text, 'question_name':question_name})