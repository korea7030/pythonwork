# -*- coding: utf-8 -*-
def simple_html_tag(tag, msg):
    print('<{0}>{1}</{0}>'.format(tag, msg))


simple_html_tag('h1', '심플 해당 타이틀')

print('-'*30)


# 함수를 리턴
def html_tag(tag):
    print('call html_tag')

    def wrap_text(msg):
        print('wrap_text')
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text


print_h1 = html_tag('h1')
# print(print_h1)  # wrap_text 함수 object 할당
print_h1('첫 번째 해당 타이틀')
print_h1('두 번째 해당 타이틀')

print_p = html_tag('p')
print_p('이것은 패러그래프')
