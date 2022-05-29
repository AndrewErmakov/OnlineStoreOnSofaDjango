from django.urls import reverse
from django.utils.http import urlencode


def reverse_with_query_params(view: str, kwargs=None, query_kwargs=None):
    """
        Custom reverse to add a query string after the url
        Example usage:
        url = my_reverse(
        'my_test_url',
        kwargs={'pk': object.id},
        query_kwargs={'next': reverse('home')}
        )
        """
    url = reverse(view, kwargs=kwargs)

    if query_kwargs:
        return f'{url}?{urlencode(query_kwargs)}'

    return url
