#!/usr/bin/env python
# encoding: utf-8
"""
index.py

Created by Francisco M. Silva Ferreira on 2011-06-17.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
import os
import django

from django import http
from django import shortcuts

from google.appengine.api import mail

import logging



def index(request):
  params = {}
  
  small_prefix = "/static/img/gallery/small/gSmall_"
  large_prefix = "/static/img/gallery/large/g_"
  small = []
  large = []
  
  offset = 128
  for i in xrange(1,11):
    small_s = "%s%d.png" % (small_prefix,i)
    large_s = "%s%d.png" % (large_prefix,i)
    small.append((small_s,offset*(i-1),i))
    large.append(large_s)
    
  params["smallImages"]=small
  params["largeImages"]=large
  params["prefix"]=large_prefix
  params["offset"] = offset
  divisions = []
  for i in xrange(1,5):
    if(i<4):
      divisions.append((i,True))
    else:
      divisions.append((i,False))
      
  params["divisions"] = divisions
  
  logging.error(params)
  print params
  
  return shortcuts.render_to_response("index.html", params)
  
 

def rooms(request):
  params = {}
  return shortcuts.render_to_response("rooms.html", params)  
  
def contacts(request):
  params = {}
  return shortcuts.render_to_response("contacts.html", params)
  
def activities(request):
  params = {}
  return shortcuts.render_to_response("activities.html", params)
  
def location(request):
  params = {}
  return shortcuts.render_to_response("location.html", params)
  
def sendmail(request):
	t = "elizabeths.place.pico@gmail.com"
	subj = "Aluguer"
	date_from = request.GET['df']
	date_to = request.GET['dt']
	house = request.GET['h']
	m = request.GET['m']
	mail.send_mail(sender="samanthaPTsilveira@gmail.com",
              to=t,
              subject=subj,
              body=house+ " from:"+date_from+" to:"+date_to+" mail:" +m)
	return shortcuts.render_to_response("index.html", {})