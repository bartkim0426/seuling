from django.http import HttpResponse
from django.conf import settings

def render(template_name, context):
    header_content = open(settings.BASE_DIR + "/templates/header.html", "r").read()
    footer_content = open(settings.BASE_DIR + "/templates/footer.html", "r").read()
        
    with open(settings.BASE_DIR + "/templates/"+ template_name + ".html", "r") as template:
        content = template.read()
        content = content.replace("## header ##", header_content)
        content = content.replace("## footer ##", footer_content)
        for key, value in context.items():
            content = content.replace(
                   "## " + key + " ##", value 
                    )
    return HttpResponse(content)
