from rest_framework.pagination import PageNumberPagination


class SetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_params = "page_size"
    max_page_size = 100
