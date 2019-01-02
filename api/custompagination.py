from rest_framework.pagination import LimitOffsetPagination


class LimitOffsetPaginationWithUpperBound(LimitOffsetPagination):
    max_limit = 40
