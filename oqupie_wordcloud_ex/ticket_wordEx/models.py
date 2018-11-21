from django.db import models

# Create your models here.
class OniondeskMain(models.Model):
    id = models.BigIntegerField(primary_key=True, help_text='아이디')
    subdomain_name = models.CharField(max_length=50, unique=True, help_text='서브 도메인명 (웹 주소 앞부분)')
    host_mapping = models.CharField(max_length=200, blank=True, null=True, help_text='호스트 맵핑')
    owner_email_addr = models.CharField(max_length=190, unique=True, help_text='계정소유자 이메일 주소')
    desk_name = models.CharField(max_length=100, help_text='오니온데스크 이름')
    desk_logo_path = models.CharField(max_length=200, blank=True, null=True, help_text='오니온데스크 로고 저장위치')
    desk_favicon_path = models.CharField(max_length=200, blank=True, null=True, help_text='오니온데스크 파비콘 저장위치')
    desk_theme = models.CharField(max_length=50, default='default', help_text='오니온데스크 테마')
    desk_language = models.CharField(max_length=10, help_text='오니온데스크 기본 언어 (예: ko, en)')
    desk_timezone = models.CharField(max_length=50, help_text='오니온데스크 기본 시간대 (예: Asia/Seoul)')
    desk_date_format = models.CharField(max_length=20, help_text='오니온데스크 날짜 표시형식 (Y.m.d, m.d.Y)')
    desk_home_form_cd = models.CharField(max_length=2, help_text='오니온데스크 홈 표시형식')
    subdomain_changeable_yn = models.CharField(max_length=1, help_text='서브 도메인명 (웹 주소 앞부분) 변경 가능여부 (Y:가능, N:불가능)')
    status_cd = models.CharField(max_length=2, help_text='오니온데스크 상태')
    join_date = models.DateTimeField(help_text='오니온데스크 가입일시')
    out_date = models.DateTimeField(null=True, help_text='오니온데스크 탈퇴일시')

    class Meta:
        db_table = 'oniondesk_main'


class BrandMain(models.Model):
    """
    브랜드 정보
    """
    oniondesk_id = models.BigIntegerField(db_index=True, help_text='참고용 오니온데스크 아이디')
    brand_name = models.CharField(max_length=100, help_text='브랜드명')
    brand_language = models.CharField(max_length=10, help_text='브랜드 기본 언어 (예: ko, en)')
    brand_image_path = models.CharField(max_length=200, blank=True, null=True, help_text='브랜드 이미지 저장위치')
    ticket_email_id = models.CharField(max_length=100, help_text='고객지원 이메일 주소 앞부분')
    ticket_email_addr = models.CharField(max_length=190, unique=True, help_text='고객지원 이메일 주소')
    ticket_email_changeable_yn = models.CharField(max_length=1, help_text='고객지원 이메일 주소 변경 가능여부 (Y:가능, N:불가능)')
    ticket_email_design_yn = models.CharField(max_length=1, help_text='고객지원 이메일 답장 디자인 사용여부 (Y:사용, N:사용안함)')
    ticket_email_header_bgcolor = models.CharField(max_length=6, blank=True, null=True, help_text='고객지원 이메일 답장 header 배경색상 RGB 값')
    ticket_email_header_logo_path = models.CharField(max_length=200, blank=True, null=True, help_text='고객지원 이메일 답장 header 로고 저장위치')
    ticket_email_header_html = models.CharField(max_length=2000, blank=True, null=True, help_text='고객지원 이메일 답장 header html')
    ticket_email_footer_contents = models.TextField(blank=True, null=True, help_text='고객지원 이메일 답장 footer 내용')
    ticket_email_footer_html = models.TextField(blank=True, null=True, help_text='고객지원 이메일 답장 footer html')
    ticket_twitter_yn = models.CharField(max_length=1, help_text='고객지원 트위터 연결여부 (Y:연결, N:해제)')
    ticket_twitter_id = models.CharField(max_length=200, blank=True, null=True, help_text='고객지원 트위터 연결 아이디')
    ticket_twitter_name = models.CharField(max_length=200, blank=True, null=True, help_text='고객지원 트위터 연결 이름')
    ticket_twitter_since = models.CharField(max_length=200, blank=True, null=True, help_text='고객지원 트위터 기준 답글(가져온 답글) 아이디')
    ticket_twitter_token = models.CharField(max_length=500, blank=True, null=True, help_text='고객지원 트위터 인증토큰')
    ticket_twitter_secret = models.CharField(max_length=500, blank=True, null=True, help_text='고객지원 트위터 인증토큰 비밀번호')
    ticket_facebook_yn = models.CharField(max_length=1, help_text='고객지원 페이스북 연결여부 (Y:연결, N:해제)')
    ticket_facebook_id = models.CharField(max_length=200, blank=True, null=True, help_text='고객지원 페이스북 연결 아이디')
    ticket_facebook_name = models.CharField(max_length=200, blank=True, null=True, help_text='고객지원 페이스북 연결 이름')
    ticket_facebook_token = models.CharField(max_length=500, blank=True, null=True, help_text='고객지원 페이스북 인증토큰')
    ticket_instagram_yn = models.CharField(max_length=1, help_text='고객지원 인스타그램 연결여부 (Y:연결, N:해제)')
    ticket_instagram_id = models.CharField(max_length=200, blank=True, null=True, help_text='고객지원 인스타그램 연결 아이디')
    ticket_instagram_shortcode = models.CharField(max_length=100, blank=True, null=True, help_text='고객지원 인스타그램 글 단축코드')
    ticket_instagram_media_id = models.CharField(max_length=200, blank=True, null=True, help_text='고객지원 인스타그램 글 아이디')
    ticket_instagram_token = models.CharField(max_length=500, blank=True, null=True, help_text='고객지원 인스타그램 인증토큰')
    ticket_google_play_yn = models.CharField(max_length=1, help_text='고객지원 구글 플레이 연결여부 (Y:연결, N:해제)')
    ticket_google_play_package_name = models.CharField(max_length=200, blank=True, null=True, help_text='고객지원 구글 플레이 연결 앱 패키지명')
    ticket_google_play_json_key = models.CharField(max_length=4000, blank=True, null=True, help_text='고객지원 구글 플레이 Service Account JSON key')
    widget_icon_type = models.CharField(max_length=2, blank=True, null=True,help_text='위젯 아이콘 모양 (10:타원, 20:원)')
    widget_text = models.CharField(max_length=10, blank=True, null=True, help_text='위젯 아이콘 표시 글자')
    widget_fgcolor = models.CharField(max_length=6, blank=True, null=True, help_text='위젯 아이콘 글자색상 RGB 값')
    widget_bgcolor = models.CharField(max_length=6, blank=True, null=True, help_text='위젯 아이콘 배경색상 RGB 값')
    widget_border_color = models.CharField(max_length=6, blank=True, null=True, help_text='위젯 아이콘 테두리 색상 RGB 값')
    widget_html = models.CharField(max_length=2000, blank=True, null=True, help_text='위젯 HTML 태그')
    reg_date = models.DateTimeField(help_text='등록일시')

    class Meta:
        db_table = 'brand_main'


class TicketCategory(models.Model):
    """
    티켓 유형 정보
    """
    oniondesk_id = models.BigIntegerField(db_index=True, help_text='참고용 오니온데스크 아이디')
    brand = models.ForeignKey(BrandMain, on_delete=models.CASCADE, help_text='브랜드 정보')
    category_name = models.CharField(max_length=100, help_text='티켓 유형 명칭')
    order_no = models.PositiveIntegerField(default=0, help_text='정렬순서')
    display_yn = models.CharField(max_length=1, help_text='표시여부 (Y:표시, N:숨김)')

    class Meta:
        db_table = 'ticket_category'


class TicketMain(models.Model):
    """
    티켓 메인 정보
    """
    oniondesk_id = models.BigIntegerField(db_index=True, help_text='참고용 오니온데스크 아이디')
    brand = models.ForeignKey(BrandMain, on_delete=models.CASCADE, help_text='브랜드 정보')
    brand_name = models.CharField(max_length=100, help_text='브랜드명')
    ticket_no = models.BigIntegerField(help_text='브랜드별 티켓 순번')
    channel_cd = models.CharField(max_length=2, help_text='채널')
    category = models.ForeignKey('TicketCategory', on_delete=models.SET_NULL, null=True, help_text='티켓 유형 정보')
    importance_cd = models.CharField(max_length=2, default='10',help_text='중요도 (10:낮음, 20:보통, 30:높음, 40:긴급)')
    sender_customer_id = models.BigIntegerField(help_text='보낸사람 고객 정보')
    subject = models.CharField(max_length=200, help_text='주제')
    contents = models.TextField(help_text='설명')
    recent_reply = models.CharField(max_length=100, help_text='최근 대화 내용')
    email_message_id = models.CharField(max_length=200, blank=True, null=True, help_text='이메일 메시지 아이디')
    email_to = models.CharField(max_length=200, null=True, default='', help_text='받은이메일 주소')
    twitter_id = models.CharField(max_length=200, blank=True, null=True, help_text='트위터 글 아이디')
    facebook_id = models.CharField(max_length=200, blank=True, null=True, help_text='페이스북 글 아이디')
    instagram_id = models.CharField(max_length=200, blank=True, null=True, help_text='인스타그램 글 아이디')
    google_play_review_id = models.CharField(max_length=200, blank=True, null=True, help_text='구글 플레이 리뷰 아이디')
    brand_facebook_id = models.BigIntegerField(null=True,help_text='브랜드별 페이스북 연결 정보')
    charge_team_id = models.BigIntegerField(null=True, help_text='담당자 그룹 정보')
    charge_member_id = models.BigIntegerField(null=True, help_text='담당자 멤버 정보')
    assign_member_id = models.BigIntegerField(null=True, help_text='담당자를 배정한 멤버 정보')
    status_cd = models.CharField(max_length=2, help_text='처리 상태 (10:신규, 20:진행, 30:대기, 40:해결, 99:종료)')
    reply_yn = models.CharField(max_length=1, help_text='티켓 답변유무 (Y:유, N:무)')
    customer_help_yn = models.CharField(max_length=1, blank=True, null=True,help_text='고객 도움여부 (NULL:평가전, Y:도움긍정, N:도움부정)')
    html_yn = models.CharField(max_length=1, default='N', help_text='설명 HTML 여부 (Y:HTML, N:TXT)')
    manual_yn = models.CharField(max_length=1, default='N', help_text='수동 생성여부 (Y:수동, N:자동)')
    spam_yn = models.CharField(max_length=1, default='N', help_text='스팸여부 (Y:스팸, N:일반)')
    delete_yn = models.CharField(max_length=1, default='N', help_text='삭제여부 (Y:삭제, N:삭제아님)')
    reg_date = models.DateTimeField(help_text='최초 등록일시')
    mod_date = models.DateTimeField(null=True, help_text='최종 변경일시')
    assign_date = models.DateTimeField(null=True, help_text='최종 배정일시')
    resolve_date = models.DateTimeField(null=True, help_text='해결일시')
    closed_date = models.DateTimeField(null=True, help_text='종료일시')
    delete_date = models.DateTimeField(null=True, help_text='스팸 등록일시 또는 삭제일시')

    class Meta:
        db_table='ticket_main'