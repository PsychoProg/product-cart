from django.http import HttpResponse
from django.shortcuts import render
# from .task import add
import logging
def index(request):
 logger = logging.getLogger("loggers")
 message = {
  'message' : "user visits index()"
 }
 logger.info(message)
 return HttpResponse("hello")