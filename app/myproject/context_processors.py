from typing import Dict

from django import template

from advanced_htmx.constants import HTMXTriggers

register = template.Library()


def extra_template_variables(request):
    htmx_triggers: Dict[str, str] = {trigger.name: trigger.value for trigger in HTMXTriggers}
    return {"htmx_triggers": htmx_triggers}
