import tkinter.ttk as ttk # 콤보박스의 경우 패키지의 저장 루트가 다른곳에 있어서 이렇게 선언하였다.
import tkinter.messagebox as msgbox # 메시지 박스의 경우 별도의 패키지에 있어서 이렇게 선언하였다.
from tkinter import *
import time
# 기본 프레임 설정 #
root = Tk()
root.title("DokBak GUI") # title() 프로그램의 이름을 지정해 줄 수 있다.
#root.geometry("640x480") # (가로)x(세로)+(x축거리)+(y축거리) tkinter에서 화면크기 조절시에는 *가 아닌 소문자 x 를 사용해야한다.  
root.geometry("640x480+0+0") # 시작위치는 +를 이용해서 조절가능하다.
root.resizable(False,False) # 창의 크기 조절가능여부 설정 resizable(x축 변경 여부,y축 변경 여부) # False는 불가.
# 기본 프레임 설정 #

# 14_그리드 설정 #
# 팩은 쌓는 느낌이고, 그리드는 좌표에 위치 하는 느낌 

#gridbtn1 = Button(root, text= "버튼1")
#gridbtn2 = Button(root, text= "버튼2")
# gridbtn1.pack(side="left")
# gridbtn2.pack(side="right")
# gridbtn1.grid(row=0, column=0)
# gridbtn2.grid(row=1, column=1)

# 맨 윗줄
btn_f16 = Button(root, text= "F16", width=5, height=2)
btn_f17 = Button(root, text= "F17", width=5, height=2)
btn_f18 = Button(root, text= "F18", width=5, height=2)
btn_f19 = Button(root, text= "F19", width=5, height=2)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady =3)
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady =3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady =3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady =3)

# clear줄
btn_clear = Button(root, text= "clear", width=5, height=2)
btn_equal = Button(root, text= "=", width=5, height=2)
btn_div = Button(root, text= "/", width=5, height=2)
btn_mul = Button(root, text= "*", width=5, height=2)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady =3)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady =3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady =3)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady =3)

# 7 시작 줄
btn_7 = Button(root, text= "7", width=5, height=2)
btn_8 = Button(root, text= "8", width=5, height=2)
btn_9 = Button(root, text= "9", width=5, height=2)
btn_sub = Button(root, text= "-", width=5, height=2)

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady =3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady =3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady =3)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady =3)

# 4 시작 줄
btn_4 = Button(root, text= "4", width=5, height=2)
btn_5 = Button(root, text= "5", width=5, height=2)
btn_6 = Button(root, text= "6", width=5, height=2)
btn_add = Button(root, text= "+", width=5, height=2)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady =3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady =3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady =3)
btn_add.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady =3)

# 1 시작 줄
btn_1 = Button(root, text= "1", width=5, height=2)
btn_2 = Button(root, text= "2", width=5, height=2)
btn_3 = Button(root, text= "3", width=5, height=2)
btn_enter = Button(root, text= "enter", width=5, height=2) # 세로로 합쳐짐

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady =3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady =3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady =3)
btn_enter.grid(row=4, column=3, rowspan= 2, sticky=N+E+W+S, padx=3, pady =3) # 현재 위치로부터 아래쪽으로 몇 줄을 더함

# 0 시작 줄
btn_0 = Button(root, text= "0", width=5, height=2)
btn_point = Button(root, text= ".", width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady =3) # 현재 위치로부터 오른쪽으로 몇 칸 더함
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady =3)
# 14_그리드 설정 #
 
# 13_스크롤바 설정 #
# 13까지의 소스가 있다면 그리드 설정은 적용 될 수 없기에 생략하였다.
# 2_버튼 설정 #

root.mainloop()

