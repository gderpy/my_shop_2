from django import template

register = template.Library()


@register.filter
def price_format(value):
    try:
        value = int(value)
        return f"{value:,}".replace(",", " ")
    except (TypeError, ValueError):
        return value

