from django.http import HttpResponse
import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.D18, 30)

def index(request):
  val = 0
  num_pixels = 6

  for a in range (50):
    val = val + 1
    val = val % num_pixels
    for n in range (num_pixels):
      if n>=val:
        pixels[n] = (255, 150, 5)
      else:
        pixels[n] = (0,0,0)
    time.sleep(0.01)

  for n in range (num_pixels):
    pixels[n] = (0,0,0)
  return HttpResponse("nice job, you turned on a light. what an accomplishment")
