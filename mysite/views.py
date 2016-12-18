from django.http import HttpResponse
import datetime

def current_datetime(request):
    #offset = int(offset)
    #dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    now = datetime.datetime.now()
    html = ("<html><body>it is now %s. </body><html>" % now)
    return HttpResponse(html)

def hours_ahead(request,offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    #now = datetime.datetime.now()
    html = ("<html><body>In %s hour(s), it is will be %s. </body><html>" % (offset, dt))
    return HttpResponse(html)