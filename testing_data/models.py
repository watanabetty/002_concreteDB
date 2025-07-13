
# testing_data/models.py
from django.db import models

class TestResult(models.Model):
    test_date = models.DateField(verbose_name="試験日") # 日付
    mix_name = models.CharField(max_length=255, verbose_name="配合名") # 文字列
    water_cement_ratio = models.FloatField(verbose_name="水セメント比") # 小数点数
    sand_aggregate_ratio = models.FloatField(verbose_name="S/A") # 小数点数 (s/a)
    air_content_percent = models.FloatField(verbose_name="空気量(%)") # 小数点数

    # W, N, H, M, L, S, G は何の略か不明ですが、配合成分と仮定してFloatFields
    w_value = models.FloatField(verbose_name="W") # 水量？
    n_value = models.FloatField(verbose_name="N") # 細骨材？
    h_value = models.FloatField(verbose_name="H") # 粗骨材？
    m_value = models.FloatField(verbose_name="M") # 混和剤？
    l_value = models.FloatField(verbose_name="L") # 混和剤？
    s_value = models.FloatField(verbose_name="S") # 砂？
    g_value = models.FloatField(verbose_name="G") # 砂利？

    slump = models.FloatField(verbose_name="スランプ(mm)", null=True, blank=True) # スランプ
    air_content_result = models.FloatField(verbose_name="測定空気量(%)")
    # 最初の「空気量」と最後の「空気量」が重複しているため、一つにしました。
    # もし異なる意味合いなら、air_content_percent と air_content_final のように区別してください。

    created_at = models.DateTimeField(auto_now_add=True) # 作成日時を自動記録
    updated_at = models.DateTimeField(auto_now=True) # 更新日時を自動記録

    class Meta:
        verbose_name = "試験結果"
        verbose_name_plural = "試験結果"
        ordering = ['-test_date'] # 試験日降順で並べ替え

    def __str__(self):
        return f"{self.test_date} - {self.mix_name}"