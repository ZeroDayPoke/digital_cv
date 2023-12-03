# app/models/mixins.py

class FilterSortMixin:
    filter_type_handlers = {
        'boolean': lambda query, cls, field, value: query.filter(getattr(cls, field) == value) if value is not None else query,
        'range': lambda query, cls, field, min_value, max_value: query.filter(getattr(cls, field) >= min_value, getattr(cls, field) <= max_value) if min_value and max_value else query,
        'string': lambda query, cls, field, value: query.filter_by(**{field: value}),
        'sort': lambda query, cls, field, order: query.order_by(getattr(cls, field).desc()) if order == 'desc' else query.order_by(getattr(cls, field).asc())
    }

    @classmethod
    def get_filtered(cls, filters, page, per_page):
        query = cls.query

        for filter_type, args in filters.items():
            for arg in args:
                handler = cls.filter_type_handlers.get(filter_type)
                if handler:
                    query = handler(query, cls, *arg)

        return query.paginate(page=page, per_page=per_page, error_out=False)
