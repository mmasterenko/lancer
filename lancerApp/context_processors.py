from .models import GeneralInfo


def general_info(req):
    genInfo = GeneralInfo.objects.first()
    try:
        info = {
            'address': genInfo.address,
            'mainPhone': genInfo.main_phone,
            'footerText': genInfo.footerText,
            'feedbackURL': genInfo.feedbackURL
        }
    except AttributeError:
        info = {}
    return {'general_info': info}
