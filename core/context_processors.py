from .models import League

def add_to_base(request):
    return {
        'leagues' : League.objects.all()
    }