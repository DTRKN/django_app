from django import template
from django.urls import reverse
from test_app.utils import get_menu_tree

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_tree = get_menu_tree(menu_name)
    context = {
        'menu_tree': menu_tree,
        'request_path': request.path,
        'reverse': reverse,
        'menu_name': menu_name,
    }
    return template.render(context, 'menu.html')