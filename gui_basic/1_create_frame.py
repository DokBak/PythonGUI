from tkinter import *

root = Tk()
root.title("DokBak GUI") # title() 프로그램의 이름을 지정해 줄 수 있다.
#root.geometry("640x480") # (가로)x(세로)+(x축거리)+(y축거리) tkinter에서 화면크기 조절시에는 *가 아닌 소문자 x 를 사용해야한다.  
root.geometry("640x480+0+0") # 시작위치는 +를 이용해서 조절가능하다.

root.resizable(False,False) # 창의 크기 조절가능여부 설정 resizable(x축 변경 여부,y축 변경 여부) # False는 불가.

root.mainloop()

