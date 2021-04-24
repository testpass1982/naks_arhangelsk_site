from .models import Menu, Profile


def profile_chunks(request):
    profile = Profile.objects.first()
    return {"profile": profile}


def menu_urls(request):
    menu_urls = Menu.objects.all()
    menu_dict = {}
    for url in menu_urls:
        menu_dict[url.url_code] = {"url": url.url, "title": url.title}
    return {
        "page_urls": menu_dict,
    }
