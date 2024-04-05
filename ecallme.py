import sys
import threading
import pyautogui
import paddleocr
import rapidfuzz
global PREVIOUS_FRAME_TXT


if (len(sys.argv) >= 5):
    topx, topy, WIDTH, HEIGHT = list(map(lambda x: int(x), sys.argv[1:]))
else:
    topx, topy, WIDTH, HEIGHT = list([0, 0, 1900, 1080])
PASTE_DIST=rapidfuzz.distance.DamerauLevenshtein

PREVIOUS_FRAME_TXT = ""
BIN_DUMP_DIR = "./bin_dumps"
ocr = paddleocr.PaddleOCR(lang='en',
                          rec_model_dir="_models/rec/en/en_PP-OCRv4_rec_infer",
                          det_model_dir="_models/det/en/en_PP-OCRv4_det_infer",
                          use_gpu=True,
                          cls=False, show_log=False)


def save_screen():
    pyautogui.screenshot("./straight_to_disk.png", region=(topx, topy, WIDTH, HEIGHT))
    return ocr.ocr("./straight_to_disk.png")

def get_screen():
    r=save_screen()
    s=""
    global PREVIOUS_FRAME_TXT
    txts=list(map(lambda e: e[1][0], r[0]))
    dist=PASTE_DIST.normalized_distance(" ".join(txts), PREVIOUS_FRAME_TXT)
    #print(dist)
    if dist > 0.3:
        PREVIOUS_FRAME_TXT=" ".join(txts)
        print(PREVIOUS_FRAME_TXT)

    threading.Timer(1, get_screen).start()


threading.Timer(3, get_screen).start()

# dumpenv.dump_data(ocr, './bin_dumps')
# print(r)
