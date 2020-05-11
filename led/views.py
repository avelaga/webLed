# from django.shortcuts import render
from django.http import HttpResponse
import RPi.GPIO as GPIO
import time

def index(request):
  led = 18

  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(led, GPIO.OUT)
  GPIO.output(led, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(led, GPIO.LOW)
  GPIO.cleanup()
  return HttpResponse("nice job, you turned on a light. what an accomplishment")
