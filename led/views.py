from django.http import HttpResponse
import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.D18, 30)

def index(request):
  val = 0
  num_pixels = 10
  len = 2

  for a in range (25):
    val = val % num_pixels
    for n in range (num_pixels):
      if n >= val and n < val + len:
        pixels[n] = (0, 255, n*20)
      else:
        pixels[n] = (0,0,0)
    time.sleep(0.02)
    val = val + 1

  for n in range (num_pixels):
    pixels[n] = (0,0,0)
  return HttpResponse("nice job, you turned on a light. what an accomplishment")
