from django import template

register = template.Library()


@register.filter
def placeholdit_if_none(img, size):
    if not img:
        return 'http://placehold.it/%s' % size
    else:
        return img.url
