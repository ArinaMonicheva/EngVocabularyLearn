import inspect
import signal
import oGUI
import pyautogui as pyautogui
from paddleocr import PaddleOCR
import time, threading
import asyncio, sys,json
from videocr import save_subtitles_to_file
'''
if __name__ == '__main__':
    save_subtitles_to_file('example_cropped.mp4', 'example.srt', lang='en',
     sim_threshold=80, conf_threshold=50, use_fullframe=True,
    # Models different from the default mobile models can be downloaded here: https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.3/doc/doc_en/models_list_en.md
    # det_model_dir='<PADDLEOCR DETECTION MODEL DIR>', rec_model_dir='<PADDLEOCR RECOGNITION MODEL DIR>',
     brightness_threshold=210, similar_image_threshold=1000, frames_to_skip=1)
'''
'''

def foo():
  pyautogui.screenshot("./straight_to_disk.png")
  r = ocr.ocr("./straight_to_disk.png")
  try:
    f.write(str(r) + "\n\n")
    l.append(str(r))
  except:
    l.append(str(r))
  print(r)
  threading.Timer(1, foo)..start()
'''
'''
ocr = PaddleOCR(lang='en', rec_model_dir="_models/rec/en/en_PP-OCRv4_rec_infer", det_model_dir= "_models/det/en/en_PP-OCRv4_det_infer", use_gpu=True)
#r=ocr.ocr("./_2.png")
bufsize = 512
f = open('res.txt', 'w', buffering=bufsize)
l=[]

# compute_input.py


#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    #get our data as an array from read_in()
    lines = read_in()
    #create a numpy array

    #return the sum to the output stream
    print(lines)

#start process
if __name__ == '__main__':
    main()
'''
'''
for line in sys.stdin:

  print("READY")

  for line in sys.stdin:
    print("PYTHON RECEIVED: %s" % line.strip())'''
'''
  pyautogui.screenshot("./straight_to_disk.png")
  r = ocr.ocr("./straight_to_disk.png")
  try:
    f.write(str(r) + "\n\n")
    l.append(str(r))
  except:
    l.append(str(r))
  print(str(r))
'''

bufsize = 4
f = open('res.txt', 'w', buffering=bufsize)
l = []

def sigint_handler(signal, frame):
  f.writelines(l)
  sys.stderr.write('\nInterrupted')
  cleanup(0)
  PREVIOUS_FRAME_TXT=""

def _cleanup(attr, method, args):
  code = 0
  if hasattr(attr, method):
    try:
      getattr(attr, method)(*args)
    except Exception as exc:
      sys.stderr.write(f"Error cleaning up attribute {repr(attr)}: {exc}")
      code = 1
  return code

signal.signal(signal.SIGINT, sigint_handler)
def cleanup(code=0):
  for attr in globals().values():
    if not (inspect.isclass(attr) or inspect.isfunction(attr)):
      if not code:
        code |= _cleanup(attr, "__del__", ())
        code |= _cleanup(attr, "__exit__", (None, None, None))

  exit(code)



# -- Maincode down here --
def main():
  ocr = PaddleOCR(lang='en',
                  rec_model_dir="_models/rec/en/en_PP-OCRv4_rec_infer",
                  det_model_dir="_models/det/en/en_PP-OCRv4_det_infer",
                  use_gpu=True,
                  cls=False)


  def foo():
    try:
      pyautogui.screenshot("./straight_to_disk.png")
      r = ocr.ocr("./straight_to_disk.png")
      l.append(str(r))
      print(r)
      threading.Timer(1, foo).start()
    except (Exception, KeyboardInterrupt):
      f.writelines(l)
      print(l)
      print(">>> Error or keyboard interrupt")

  threading.Timer(10,foo).start()

# -- Maincode Ends
if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    sys.stderr.write('\nInterrupted')
    cleanup(0)