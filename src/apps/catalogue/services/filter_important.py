def get_important_items(self, queryset):
    try:
        is_important = self.request.query_params.get('important')
        if is_important is not None:
            is_important = is_important.lower() == 'true'
            return queryset.filter(important=is_important)

        return queryset
    except Exception as e:
        return queryset