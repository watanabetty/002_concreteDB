# testing_data/forms.py
from django import forms
from .models import TestResult

class TestResultForm(forms.ModelForm):
    class Meta:
        model = TestResult
        fields = '__all__' # モデルのすべてのフィールドをフォームに含める
        # fields = ['test_date', 'mix_name', ...] # 特定のフィールドのみ含める場合はリストで指定
        widgets = {
            'test_date': forms.DateInput(attrs={'type': 'date'}), # HTML5の日付入力ウィジェット
        }