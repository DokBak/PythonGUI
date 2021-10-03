import time
import keyboard
from PIL import ImageGrab
def screenshot():
    # 2021년 10월 3일 10시 30분 30초 -> _20211003_103030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img  = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("s", screenshot)
#keyboard.add_hotkey("ctrl + a", screenshot)
#keyboard.add_hotkey("F9", screenshot) # 사용자가 F9키를 누르면 스크린 샷 저장    

keyboard.wait("esc") # 사용자가 esc를 누를때 까지 프로그램 수행
