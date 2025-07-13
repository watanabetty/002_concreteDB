
# testing_data/views.py
from django.shortcuts import render, redirect
from .forms import TestResultForm
from .models import TestResult # 一覧表示用

def add_test_result(request):
    if request.method == 'POST':
        form = TestResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test_result_list') # 成功したら一覧ページへリダイレクト
    else:
        form = TestResultForm() # GETリクエストなら空のフォームを表示
    return render(request, 'testing_data/add_test_result.html', {'form': form})

def test_result_list(request):
    results = TestResult.objects.all() # 全ての試験結果を取得
    return render(request, 'testing_data/test_result_list.html', {'results': results})