# from django.shortcuts import render
from django.http import HttpResponse
import RPi.GPIO as GPIO
import time

def index(request):
  led = 18

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(led, GPIO.OUT)
  GPIO.output(led, GPIO.HIGH)
  time.sleep(1)
  GPIO.output(led, GPIO.LOW)
  GPIO.cleanup()
  return HttpResponse("you just briefly turned on a led in my room. refresh this page to do it again.")
