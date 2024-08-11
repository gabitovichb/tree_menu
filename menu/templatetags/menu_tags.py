from typing import Any

from django import template
from django.db.models import QuerySet

from menu.models import MenuItem, Statuses


register = template.Library()


@register.inclusion_tag("menu/menu.html", takes_context=True)
def draw_menu(context: Any, menu_name: str) -> dict[str, Any]:
    menu_items: QuerySet[MenuItem] = MenuItem.objects.filter(menu__name=menu_name, status=Statuses.AVAILABLE)
    objects_dict: dict[str, Any] = {}

    menu_item: MenuItem
    for menu_item in menu_items:
        if menu_item.parent is None:
            objects_dict[str(menu_item.id)] = {"item": menu_item, "subitems": []}
        else:
            objects_dict[str(menu_item.parent_id)]["subitems"].append(menu_item)

    result: dict[str, Any] = {"menu_name": menu_name, "data": list(objects_dict.values())}
    return {"result": result}
