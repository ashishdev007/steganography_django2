
"""
In this module encoding and decoding happens on the R,G, and B values of pixels if they meet the criteria
"""
from apps.steganography.utils.status import createStatus, getProgress, setProgressMultiProcessing, deleteStatus, getStatusObject
from django.db import connection

import time
from PIL import Image
import threading
import multiprocessing
from io import StringIO
import binascii
import math

def rgb2hex(r,g,b):
  return '#{:02x}{:02x}{:02x}'.format(r,g,b)

def hex2rgb(hexcode):
  # return ImageColor.getcolor(hexcode, "RGB")
  hexcode = hexcode[1:]
  return tuple(map(lambda x : int(hexcode[x:x+2], 16), (0,2,4)))

def str2bin(message):
  binary = bin(int(binascii.hexlify(message), 16))
  return binary[2:]

def bin2str(binary):
  message = binascii.unhexlify("%x" % (int('0b' + binary, 2)))
  try:
    message =  message.decode("utf8")
  except UnicodeDecodeError:
    message = message.decode("ascii")
  except:
    print("Bit Array decode error!")
  finally:
    return str(message)
  
def enhanced_encode(hexcode, digit):
  hexcode = list(hexcode[1:])
  # hexTargets = (hexcode[1], hexcode[3], hexcode[5])
  consumed = 0;

  for i in range(3):
    num = 2*i + 1
    if(hexcode[num] in ("0", "1", "2", "3", "4", "5")):
      try:
        hexcode[num] =  digit[consumed]
      except IndexError:
        break
      
      consumed += 1;
  hexcode = "#" + "".join(hexcode)
  return hexcode, consumed

def enhanced_decode(hexcode):
  digit = ""
  hexcode = list(hexcode[1:])
  hexTargets = (hexcode[1], hexcode[3], hexcode[5])

  for i in range(3):
    if (hexTargets[i] in ("0", "1")):
      digit += hexTargets[i]

  return digit

def enhanced_hide(file, message, id):
  connection.close()
  img = Image.open(file)
  updatable = True
  lock = multiprocessing.Lock()

  binary = str(str2bin(message) + "1"*15 + "0")

  if img.mode in "RGBA":
    img = img.convert("RGBA")
    datas = list(img.getdata())
    
    digit = 0

    start = time.time()
    for i  in range(0,len(datas)):
      item = datas[i]
      
      if (digit < len(binary)):
        progress = math.floor(digit*100/len(binary))
        updatable = True if progress % 20 != 0 else updatable

        if(updatable and progress % 20 == 0):
          updatable = False
          t1 = multiprocessing.Process(target=setProgressMultiProcessing, args=(id, progress, lock))
          t1.start()

        (newpix, consumed) = enhanced_encode(rgb2hex(item[0], item[1], item[2]), binary[digit: digit+3])

        if newpix != None:
          r,g,b = hex2rgb(newpix)
          datas[i] = (r,g,b, item[3])

          digit += consumed
      else:
        break
    
    img.putdata(datas)
    deleteStatus(id)

    print("-------------------------")
    print("Done in ", time.time()-start)
    print("-------------------------")
    return img
  
  return "Incorrect Image mode, couldn't hide"


def enhanced_retr(file, id):
  img = Image.open(file)
  # status = getStatusObject(id)
  binary = StringIO()
  answer = ""

  lock = multiprocessing.Lock()
  updatable = True

  if img.mode in "RGBA":
    img = img.convert("RGBA")
    datas = img.getdata()

    length = len(datas)
    complete = 0

    for item in datas:
      digit = enhanced_decode(rgb2hex(item[0], item[1], item[2]))

      progress = math.floor(complete*100/length)
      complete += 1
      
      updatable = True if progress % 5 != 0 else updatable

      if(updatable and progress % 5 == 0):
        updatable = False
        t1 = multiprocessing.Process(target=setProgressMultiProcessing, args=(id, progress, lock))
        t1.start()

      if digit != None:
        binary.write(digit)

        if(binary.tell() - 16 >= 0):
          binary.seek(binary.tell() - 16)

          if (binary.read(16) == "1111111111111110"):
            print("Success!")
            answer = binary.getvalue()
            binary.close()
            deleteStatus(id)
            return bin2str(answer[:-16])
    
    answer = binary.getvalue()
    binary.close()
    deleteStatus(id)
    return bin2str(answer)
  return "Incorrect Image mode, couldn't retrivev"
