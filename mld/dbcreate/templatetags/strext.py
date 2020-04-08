from django import template


register = template.Library()


def last_cap(string_to_cap):

    return f'{string_to_cap[:len(string_to_cap) - 1]}{string_to_cap[-1].title()}'


register.filter('last_cap', last_cap)