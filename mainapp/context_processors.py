from .models import Menu, Profile


def profile_chunks(request):
    profile = Profile.objects.first()
    return {'profile': profile}


def menu_urls(request):
    # print('...menu_urls context_processors works...')
    menu_urls = Menu.objects.all()
    # print('urls in database:', len(menu_urls))
    # print(menu_urls)
    menu_dict = {}
    for url in menu_urls:
        menu_dict[url.url_code] = {'url': url.url, 'title': url.title}
    # print(menu_dict)
    # print('ABOUT_US', menu_dict['ABOUT_US']['url'])
    return {'page_urls': menu_dict,}
