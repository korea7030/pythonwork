from django import forms
from .models import TbBook

class AddForm(forms.ModelForm):
    class Meta:
        model = TbBook
        fields = ('c_bno','c_ttle','c_sbttle','c_authr','c_publshr','c_pub_dt','c_formt','c_pges','c_sttus','c_rting','c_ys24rt','c_diffrting','c_categry','c_strt_dt','c_fin_dt','c_red_prid','c_week_yn','c_red_tm','c_red_resn','c_fund_rou','c_rou_cat')

