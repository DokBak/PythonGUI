from tkinter import *
# 기본 프레임 설정 #
root = Tk()
root.title("DokBak GUI") # title() 프로그램의 이름을 지정해 줄 수 있다.
#root.geometry("640x480") # (가로)x(세로)+(x축거리)+(y축거리) tkinter에서 화면크기 조절시에는 *가 아닌 소문자 x 를 사용해야한다.  
root.geometry("640x480+0+0") # 시작위치는 +를 이용해서 조절가능하다.
root.resizable(False,False) # 창의 크기 조절가능여부 설정 resizable(x축 변경 여부,y축 변경 여부) # False는 불가.
# 기본 프레임 설정 #

# 4_텍스트 및 엔트리 설정 # 
txt= Text(root, width = 30, height = 5) # 텍스트 위젯 생성
txt.pack()
txt.insert(END, "글자를 입력하세요.") # 기본 값 설정. (여러줄 입력 가능)

e = Entry(root, width=30) # 텍스트 위젯 생성(한 줄만 입력 가능)
e.pack()
e.insert(0,"한 줄만 입력해요")
def btncmd():
    # 내용 출력
    print("txt 문자열 취득", txt.get("1.0",END)) # 1 : 첫번째 라인, 0 : 0번째 column 위치, END는 끝까지 
    print("entry 문자열 취득", e.get()) # 전부 
    # 내용 삭제
    txt.delete("1.0", END) 
    e.delete(0,END)

btn = Button(root, text = "클릭", command = btncmd)
btn.pack()
# 4_텍스트 및 엔트리 설정 # 

# 3_레이블 설정 #
label1 = Label(root, text = "안녕하세요.")
label1.pack()
photo = PhotoImage(file = "gui_basic/img.png")
label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text= "또 만나요")

    global photo2
    photo2 = PhotoImage(file = "gui_basic/img2.png")
    label2.config(image = photo2)

btn8 = Button(root, text = "클릭", command = change)
btn8.pack()
# 3_레이블 설정 #

# 2_버튼 설정 # 
btn1 = Button(root,text="버튼1111111111") # Button() root에, 텍스트는 버튼1로 설정된 버튼을 만든다.
btn1.pack() # 버튼1 객체를 프로그램에 표시

# 객체(버튼) 사이즈 조절시 padx,pady와 width,height의 차이
# padx, pady : (내부의 텍스트의 길이 + 여유공간)으로 객체를 생성
# width, height : 내부의 텍스트 길이와 상관없이 버튼 사이즈 고정(버튼사이즈보다 긴 텍스트는 비정상출력)
btn2 = Button(root, padx = 0, pady = 5, text="버튼2222222222") # padx : 객체(버튼)의 가로사이즈 조절, pady : 객체(버튼)의 세로사이즈 조절
btn2.pack()
btn3 = Button(root, padx = 5, pady = 0, text="버튼3333333333")
btn3.pack()
btn4 = Button(root, width = 5, height = 10, text="버튼4444444444")
btn4.pack()
btn5 = Button(root, fg = "blue", bg = "red", text="버튼5") # fg : 폰트색 옵션, bg : 배경색 옵션 
btn5.pack() # 현재 배경색 설정(bg)은 적용안되고 있다.
photo = PhotoImage(file = "gui_basic/img.png")
btn6 = Button(root, image = photo)
btn6.pack()
def btncmd():
    print("버튼이 클릭되었어요.")
btn7 = Button(root, text="동작하는 버튼", command = btncmd )
btn7.pack()
# 2_버튼 설정 #

root.mainloop()

