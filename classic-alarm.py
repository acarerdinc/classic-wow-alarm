import numpy as np
import cv2
from mss import mss
from PIL import Image
import os
from playsound import playsound
import time

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class ClassicAlarm():

    def __init__(self):
        self.pos = np.inf
        self.reading = True
        self.mp3_list = self.read_mp3_list()
        pass
    
    def read_mp3_list(self):
        files = []
        sounds_dir = 'sounds'
        for filename in os.listdir(sounds_dir):
            if filename.endswith(".mp3"):
                file_path = os.path.join(sounds_dir, filename)
                files.append(file_path)
        return files
                
    def play_alarm(self):
        orc_face = cv2.imread('orc_face.jpg')
        counter = 0 
        cv2.imshow('WORK COMPLETE!', orc_face)
        while cv2.waitKey(100) != 27:
            playsound(self.mp3_list[0])
            counter += 1
            if counter > 100:
                break
        
        cv2.destroyAllWindows()

    def get_img(self):
        sct = mss()
		
		# specify monitor region
        mon = sct.monitors[1:][0]
        mon['left'] = int(mon['width'] * 0.3)
        mon['top'] = int(mon['height'] * 0.3)
        mon['height'] = int(mon['height'] * 0.2)
        mon['width'] = int(mon['width'] * 0.35)

        # get screenshot
        sct_img = sct.grab(mon)
        img = np.array(Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX"), dtype=np.uint8)

        # get mask for text (yellow template)
        lower = (125, 125, 0)
        upper = (255, 255, 50)
        mask = np.array(cv2.inRange(np.array(img), lower, upper), dtype=np.float32)

        return mask

    def get_pos(self, img):
        text = pytesseract.image_to_string(img)
        a = text.replace('\n', ' ')
        a = a.replace(':', '')
        words = a.split(' ')
        if 'queue' in words:
            #words.index('queue')
            self.pos = words[words.index('queue') + 1]
            self.pos = self.pos.replace('l', '1')
            print('Program running... Position in queue: {}         '.format(self.pos), end='\r')
            if not self.reading:
                print('Queue information is now available again. Program is running as normal. Position: {}'.format(self.pos))
            self.reading = True
        else:
            if self.reading:
                print('Cannot read queue information. Check the screen. Last position: {}'.format(self.pos))
            self.reading = False
            self.pos = np.inf
            
        try:
            self.pos = float(self.pos)
        except:
            pass
        finally:
            self.pos = np.inf
        return self.pos
     


ca = ClassicAlarm()
position_th = 3950
	 
while 1:
    img = ca.get_img()
    pos = ca.get_pos(img)
    if pos < position_th:
        ca.play_alarm()
        break
    time.sleep(1)
