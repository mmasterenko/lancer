from .models import GeneralInfo


def general_info(req):
    info = GeneralInfo.objects.first()
    try:
        info = {
            'address': info.address,
            'mainPhone': info.phone,
            'footerText': info.footerText
        }
    except AttributeError:
        info = {}
    return {'general_info': info}
