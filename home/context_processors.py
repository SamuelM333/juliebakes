from home.models import HomePage

def hitcount(request):
    home_page = HomePage.objects.filter(slug="julie-bakes").first()

    return {
        'hitcount': home_page.hit_count.hits,
    }