from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from models import Card

import stripe

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


