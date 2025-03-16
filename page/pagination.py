from __future__ import absolute_import, unicode_literals
from django.core.paginator import EmptyPage, PageNotAnInteger
from .pager import Pager

def paginate(page_id, number_items, per_page=20):
    paginator = Pager(number_items, per_page)
    
    try:
        mypager = paginator.page(page_id)
    except PageNotAnInteger:
        mypager = paginator.page(1)
    except EmptyPage:
        mypager = paginator.page(paginator.num_pages)
    except:
        mypager = paginator.page(1)

    index = mypager.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    # Get our new page range. In the latest versions of Django page_range returns 
    # an iterator. Thus pass it to list, to make our slice possible again.
    page_range = list(paginator.page_range)[start_index:end_index]
    mypager.page_range = page_range
    mypager.max_index = max_index
    return mypager
