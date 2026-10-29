from django.template import Library
from .. import models
from django import http
import jdatetime as jd 

register = Library()

@register.simple_tag
def convert_date(date) : 
    return jd.datetime.fromgregorian(date=date)