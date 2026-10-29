from django.template import Library
import jdatetime

register = Library()


@register.filter
def date_changer(date) : 
    current_date = jdatetime.datetime.fromgregorian(
        date=date
    )
    return jdatetime.datetime.strftime(current_date , "%Y/%m/%d")
@register.filter
def filesize_filter(file): 
    if hasattr(file , "size") : 
        size = file.size
    else : 
        return 0
    return round(file.size / (1024 * 1024) , 2)