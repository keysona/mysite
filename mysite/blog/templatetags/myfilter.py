import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()  #自定义filter时必须加上


@register.filter(is_safe=True)  #注册template filter
@stringfilter  #希望字符串作为参数
def custom_markdown(value):
    return mark_safe(markdown.markdown(value, extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite'],safe_mode=True,enable_attributes=False))


@register.filter    #注册template filter
@stringfilter  #希望字符串作为参数
def custom_date(value):
    year,month,day = value.split(' ')[0].split('-')
    del_zero = lambda x:x if not x.startswith('0') else x[1]
    return year + "年" + del_zero(month) + "月" + del_zero(day) + "日"

@register.filter
@stringfilter
def cut(value,cut_line):
    lines = value.split('\n')
    end = int(cut_line)
    if len(lines) > end:
        for i in range(end,-1,-1):
            if "<p>" in lines[i]:
                end = i
                break
    return mark_safe('\n'.join(lines[0:end-1]))

