from django.conf import settings  # import the settings file


def app_info(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'APP_VERSION': settings.APP_VERSION}
