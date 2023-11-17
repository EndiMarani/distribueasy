from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, css_class, placeholder=None):
    widget = value.as_widget(attrs={'class': css_class})
    if placeholder:
        widget = widget.replace('></', f' placeholder="{placeholder}"></')
    return widget

@register.filter(name='tipo_cliente_extenso')
def tipo_cliente_extenso(value):
    tipos_cliente = {
        'PF': 'Pessoa Física',
        'PJ': 'Pessoa Jurídica',
    }
    return tipos_cliente.get(value, value)
