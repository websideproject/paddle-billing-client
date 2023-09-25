from typing import Callable

from paddle_billing_client.models.common import Paginate


def paginate(get: Callable, **kwargs):
    response = get(**kwargs)
    yield response

    if response.meta.pagination is None:
        raise Exception("Pagination is not supported for this endpoint")

    while response.meta.pagination.has_more and response.meta.pagination.next:
        response = get(paginate=Paginate(next=response.meta.pagination.next))
        yield response
