#!/usr/bin/env python3

class FilterSortMixin:
    @classmethod
    def apply_boolean_filter(cls, query, field, value):
        if value is not None:
            return query.filter(getattr(cls, field) == value)
        return query

    @classmethod
    def apply_range_filter(cls, query, field, min_value, max_value):
        if min_value is not None and max_value is not None:
            return query.filter(getattr(cls, field) >= min_value, getattr(cls, field) <= max_value)
        return query

    @classmethod
    def apply_string_filter(cls, query, field, value):
        if value:
            return query.filter_by(**{field: value})
        return query

    @classmethod
    def apply_sort_filter(cls, query, field, order):
        if field and order:
            return query.order_by(getattr(cls, field).desc()) if order == 'desc' else query.order_by(getattr(cls, field).asc())
        return query

    @classmethod
    def get_filtered(cls, filters, page, per_page):
        query = cls.query

        filter_handlers = {
            'boolean': cls.apply_boolean_filter,
            'range': cls.apply_range_filter,
            'string': cls.apply_string_filter,
            'sort': cls.apply_sort_filter
        }

        for filter_type, args_list in filters.items():
            handler = filter_handlers.get(filter_type)
            for args in args_list:
                query = handler(query, *args)

        return query.paginate(page=page, per_page=per_page, error_out=False)
