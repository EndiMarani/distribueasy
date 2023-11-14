from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, css_class, placeholder=None):
    widget = value.as_widget(attrs={'class': css_class})
    if placeholder:
        widget = widget.replace('></', f' placeholder="{placeholder}"></')
    return widget
