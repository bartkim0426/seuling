from django.http import HttpResponse
from django.conf import settings

def render(template_name, context):
    with open(settings.BASE_DIR + "/templates/"+ template_name + ".html", "r") as template:
        content = template.read()
        for key, value in context.items():
            content = content.replace(
                   "## " + key + " ##", value 
                    )
    return HttpResponse(content)
