
# testing_data/views.py
from django.shortcuts import render, redirect
from .forms import TestResultForm
from .models import TestResult # 一覧表示用
from django.db.models import Q # Qオブジェクトをインポート
from django.core.paginator import Paginator # 追加

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

    # 検索機能
    query = request.GET.get('q') # URLパラメータ 'q' を取得
    if query:
        results = results.filter(
            Q(mix_name__icontains=query) | # 配合名で部分一致検索（大文字小文字を区別しない）
            Q(test_date__icontains=query) # 試験日でも検索（日付の文字列形式に注意）
        )

    # フィルタリング機能（例: 特定の配合名でフィルタ）
    filter_mix_name = request.GET.get('mix_name')
    if filter_mix_name:
        results = results.filter(mix_name=filter_mix_name)

    # データの並べ替え
    sort_by = request.GET.get('sort_by', '-test_date') # デフォルトは試験日の降順
    results = results.order_by(sort_by)

    # ページネーション
    paginator = Paginator(results, 20)  # 1ページあたり20件表示
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # テンプレートに渡すデータ
    context = {
        'page_obj': page_obj, # ページオブジェクトを渡す
        # 'results': results,
        'query': query, # 検索ボックスに元の検索クエリを表示するため
        'filter_mix_name': filter_mix_name, # フィルターの選択状態を保持するため
        'sort_by': sort_by, # 並べ替えの選択状態を保持するため
        'available_mix_names': TestResult.objects.values_list('mix_name', flat=True).distinct(), # フィルタリング用の配合名リスト
    }

    # return render(request, 'testing_data/test_result_list.html', {'results': results})
    return render(request, 'testing_data/test_result_list.html', context)