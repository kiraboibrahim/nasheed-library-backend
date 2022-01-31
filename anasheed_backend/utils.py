from .settings import MAX_RESULTS_PER_PAGE

def paginated_results(page, queryset):
    if  page is not None:
        # Donot accept a page <= 0 because the offset will be negative
        page = int(page)
        if page <= 0:
            page = 1
        offset = (page - 1) * MAX_RESULTS_PER_PAGE
        end = offset + MAX_RESULTS_PER_PAGE
        # Add the number of songs each artist has
        return queryset[offset:end]
    else:
        # Return all the data without pagination
        return queryset
