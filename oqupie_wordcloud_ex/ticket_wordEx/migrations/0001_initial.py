# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-04 01:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oniondesk', models.BigIntegerField(db_index=True, help_text='참고용 오니온데스크 아이디')),
                ('brand_name', models.CharField(help_text='브랜드명', max_length=100)),
                ('brand_language', models.CharField(help_text='브랜드 기본 언어 (예: ko, en)', max_length=10)),
                ('brand_image_path', models.CharField(blank=True, help_text='브랜드 이미지 저장위치', max_length=200, null=True)),
                ('ticket_email_id', models.CharField(help_text='고객지원 이메일 주소 앞부분', max_length=100)),
                ('ticket_email_addr', models.CharField(help_text='고객지원 이메일 주소', max_length=190, unique=True)),
                ('ticket_email_changeable_yn', models.CharField(help_text='고객지원 이메일 주소 변경 가능여부 (Y:가능, N:불가능)', max_length=1)),
                ('ticket_email_design_yn', models.CharField(help_text='고객지원 이메일 답장 디자인 사용여부 (Y:사용, N:사용안함)', max_length=1)),
                ('ticket_email_header_bgcolor', models.CharField(blank=True, help_text='고객지원 이메일 답장 header 배경색상 RGB 값', max_length=6, null=True)),
                ('ticket_email_header_logo_path', models.CharField(blank=True, help_text='고객지원 이메일 답장 header 로고 저장위치', max_length=200, null=True)),
                ('ticket_email_header_html', models.CharField(blank=True, help_text='고객지원 이메일 답장 header html', max_length=2000, null=True)),
                ('ticket_email_footer_contents', models.TextField(blank=True, help_text='고객지원 이메일 답장 footer 내용', null=True)),
                ('ticket_email_footer_html', models.TextField(blank=True, help_text='고객지원 이메일 답장 footer html', null=True)),
                ('ticket_twitter_yn', models.CharField(help_text='고객지원 트위터 연결여부 (Y:연결, N:해제)', max_length=1)),
                ('ticket_twitter_id', models.CharField(blank=True, help_text='고객지원 트위터 연결 아이디', max_length=200, null=True)),
                ('ticket_twitter_name', models.CharField(blank=True, help_text='고객지원 트위터 연결 이름', max_length=200, null=True)),
                ('ticket_twitter_since', models.CharField(blank=True, help_text='고객지원 트위터 기준 답글(가져온 답글) 아이디', max_length=200, null=True)),
                ('ticket_twitter_token', models.CharField(blank=True, help_text='고객지원 트위터 인증토큰', max_length=500, null=True)),
                ('ticket_twitter_secret', models.CharField(blank=True, help_text='고객지원 트위터 인증토큰 비밀번호', max_length=500, null=True)),
                ('ticket_facebook_yn', models.CharField(help_text='고객지원 페이스북 연결여부 (Y:연결, N:해제)', max_length=1)),
                ('ticket_facebook_id', models.CharField(blank=True, help_text='고객지원 페이스북 연결 아이디', max_length=200, null=True)),
                ('ticket_facebook_name', models.CharField(blank=True, help_text='고객지원 페이스북 연결 이름', max_length=200, null=True)),
                ('ticket_facebook_token', models.CharField(blank=True, help_text='고객지원 페이스북 인증토큰', max_length=500, null=True)),
                ('ticket_instagram_yn', models.CharField(help_text='고객지원 인스타그램 연결여부 (Y:연결, N:해제)', max_length=1)),
                ('ticket_instagram_id', models.CharField(blank=True, help_text='고객지원 인스타그램 연결 아이디', max_length=200, null=True)),
                ('ticket_instagram_shortcode', models.CharField(blank=True, help_text='고객지원 인스타그램 글 단축코드', max_length=100, null=True)),
                ('ticket_instagram_media_id', models.CharField(blank=True, help_text='고객지원 인스타그램 글 아이디', max_length=200, null=True)),
                ('ticket_instagram_token', models.CharField(blank=True, help_text='고객지원 인스타그램 인증토큰', max_length=500, null=True)),
                ('ticket_google_play_yn', models.CharField(help_text='고객지원 구글 플레이 연결여부 (Y:연결, N:해제)', max_length=1)),
                ('ticket_google_play_package_name', models.CharField(blank=True, help_text='고객지원 구글 플레이 연결 앱 패키지명', max_length=200, null=True)),
                ('ticket_google_play_json_key', models.CharField(blank=True, help_text='고객지원 구글 플레이 Service Account JSON key', max_length=4000, null=True)),
                ('widget_icon_type', models.CharField(blank=True, help_text='위젯 아이콘 모양 (10:타원, 20:원)', max_length=2, null=True)),
                ('widget_text', models.CharField(blank=True, help_text='위젯 아이콘 표시 글자', max_length=10, null=True)),
                ('widget_fgcolor', models.CharField(blank=True, help_text='위젯 아이콘 글자색상 RGB 값', max_length=6, null=True)),
                ('widget_bgcolor', models.CharField(blank=True, help_text='위젯 아이콘 배경색상 RGB 값', max_length=6, null=True)),
                ('widget_border_color', models.CharField(blank=True, help_text='위젯 아이콘 테두리 색상 RGB 값', max_length=6, null=True)),
                ('widget_html', models.CharField(blank=True, help_text='위젯 HTML 태그', max_length=2000, null=True)),
                ('reg_date', models.DateTimeField(help_text='등록일시')),
            ],
            options={
                'db_table': 'brand_main',
            },
        ),
        migrations.CreateModel(
            name='TicketCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oniondesk_id', models.BigIntegerField(db_index=True, help_text='참고용 오니온데스크 아이디')),
                ('category_name', models.CharField(help_text='티켓 유형 명칭', max_length=100)),
                ('order_no', models.PositiveIntegerField(default=0, help_text='정렬순서')),
                ('display_yn', models.CharField(help_text='표시여부 (Y:표시, N:숨김)', max_length=1)),
                ('brand', models.ForeignKey(help_text='브랜드 정보', on_delete=django.db.models.deletion.CASCADE, to='ticket_wordEx.BrandMain')),
            ],
            options={
                'db_table': 'ticket_category',
            },
        ),
        migrations.CreateModel(
            name='TicketMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oniondesk_id', models.BigIntegerField(db_index=True, help_text='참고용 오니온데스크 아이디')),
                ('brand_name', models.CharField(help_text='브랜드명', max_length=100)),
                ('ticket_no', models.BigIntegerField(help_text='브랜드별 티켓 순번')),
                ('channel_cd', models.CharField(help_text='채널', max_length=2)),
                ('importance_cd', models.CharField(default='10', help_text='중요도 (10:낮음, 20:보통, 30:높음, 40:긴급)', max_length=2)),
                ('sender_customer', models.BigIntegerField(help_text='보낸사람 고객 정보')),
                ('subject', models.CharField(help_text='주제', max_length=200)),
                ('contents', models.TextField(help_text='설명')),
                ('recent_reply', models.CharField(help_text='최근 대화 내용', max_length=100)),
                ('email_message_id', models.CharField(blank=True, help_text='이메일 메시지 아이디', max_length=200, null=True)),
                ('email_to', models.CharField(default='', help_text='받은이메일 주소', max_length=200, null=True)),
                ('twitter_id', models.CharField(blank=True, help_text='트위터 글 아이디', max_length=200, null=True)),
                ('facebook_id', models.CharField(blank=True, help_text='페이스북 글 아이디', max_length=200, null=True)),
                ('instagram_id', models.CharField(blank=True, help_text='인스타그램 글 아이디', max_length=200, null=True)),
                ('google_play_review_id', models.CharField(blank=True, help_text='구글 플레이 리뷰 아이디', max_length=200, null=True)),
                ('brand_facebook', models.BigIntegerField(help_text='브랜드별 페이스북 연결 정보', null=True)),
                ('charge_team', models.BigIntegerField(help_text='담당자 그룹 정보', null=True)),
                ('charge_member', models.BigIntegerField(help_text='담당자 멤버 정보', null=True)),
                ('assign_member', models.BigIntegerField(help_text='담당자를 배정한 멤버 정보', null=True)),
                ('status_cd', models.CharField(help_text='처리 상태 (10:신규, 20:진행, 30:대기, 40:해결, 99:종료)', max_length=2)),
                ('reply_yn', models.CharField(help_text='티켓 답변유무 (Y:유, N:무)', max_length=1)),
                ('customer_help_yn', models.CharField(blank=True, help_text='고객 도움여부 (NULL:평가전, Y:도움긍정, N:도움부정)', max_length=1, null=True)),
                ('html_yn', models.CharField(default='N', help_text='설명 HTML 여부 (Y:HTML, N:TXT)', max_length=1)),
                ('manual_yn', models.CharField(default='N', help_text='수동 생성여부 (Y:수동, N:자동)', max_length=1)),
                ('spam_yn', models.CharField(default='N', help_text='스팸여부 (Y:스팸, N:일반)', max_length=1)),
                ('delete_yn', models.CharField(default='N', help_text='삭제여부 (Y:삭제, N:삭제아님)', max_length=1)),
                ('reg_date', models.DateTimeField(help_text='최초 등록일시')),
                ('mod_date', models.DateTimeField(help_text='최종 변경일시', null=True)),
                ('assign_date', models.DateTimeField(help_text='최종 배정일시', null=True)),
                ('resolve_date', models.DateTimeField(help_text='해결일시', null=True)),
                ('closed_date', models.DateTimeField(help_text='종료일시', null=True)),
                ('delete_date', models.DateTimeField(help_text='스팸 등록일시 또는 삭제일시', null=True)),
                ('brand', models.ForeignKey(help_text='브랜드 정보', on_delete=django.db.models.deletion.CASCADE, to='ticket_wordEx.BrandMain')),
                ('category', models.ForeignKey(help_text='티켓 유형 정보', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ticket_wordEx.TicketCategory')),
            ],
            options={
                'db_table': 'ticket_main',
            },
        ),
    ]