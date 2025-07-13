
# testing_data/admin.py
from django.contrib import admin
from .models import TestResult

@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = (
        'test_date', 'mix_name', 'water_cement_ratio', 'sand_aggregate_ratio',
        'air_content_percent', 'slump', 'created_at'
    )
    list_filter = ('test_date', 'mix_name') # 管理者サイトでフィルタリング可能に
    search_fields = ('mix_name',) # 配合名で検索可能に
    date_hierarchy = 'test_date' # 日付で階層的に絞り込み