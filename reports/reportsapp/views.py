from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse


def index(request):
    return HttpResponse('it works...')