import tkinter.ttk as ttk # 콤보박스의 경우 패키지의 저장 루트가 다른곳에 있어서 이렇게 선언하였다.
from tkinter import *
import time
# 기본 프레임 설정 #
root = Tk()
root.title("DokBak GUI") # title() 프로그램의 이름을 지정해 줄 수 있다.
#root.geometry("640x480") # (가로)x(세로)+(x축거리)+(y축거리) tkinter에서 화면크기 조절시에는 *가 아닌 소문자 x 를 사용해야한다.  
root.geometry("640x480+0+0") # 시작위치는 +를 이용해서 조절가능하다.
root.resizable(False,False) # 창의 크기 조절가능여부 설정 resizable(x축 변경 여부,y축 변경 여부) # False는 불가.
# 기본 프레임 설정 #

# 10_메뉴 설정 #
# MAC OS에서는 tkinter만으로는 메뉴를 만들 수가 없다. 기능만 알아두자
def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root) # 메뉴 선언

menu_file = Menu(menu,tearoff=0) # menu 에 menu_file을 넣는다. tearoff
menu_file.add_command(label="New File", command= create_new_file) # add_command 메뉴에 적용시킬 커맨드 추가
menu_file.add_command(label="New Window")
menu_file.add_separator() # add_separator 구분자
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state = "disable") # 비활성화 
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) # 프로그램 종료
menu.add_cascade(label="File", menu = menu_file) # menu에 menufile로 치환

# Edit 메뉴 (빈 값)
menu.add_cascade(label= "Edit")

# Language 메뉴 추가 (radio 버튼을 통해서 택1)
menu_lang = Menu(menu,tearoff= 0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu = menu_lang)

# View 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu= menu_view) 

root.config(menu=menu) # 메뉴 표시
# 10_메뉴 설정 #

# 9_프로그래스 바 설정 # 
# 프로그래스바란 프로그램의 진행상태를 표시하는 바를 말한다.
# 프로그래스바 또한 ttk에 존재한다.
progressbar = ttk.Progressbar(root, maximum = 100, mode = "determinate")
# mode = "indeterminate" : 언제 끝날지 모르는 상태를 말할때 사용 (실행중과 같은 상태의 바, 좌우로 움직이는 모양)
# mode = "determinate" : 시작에서부터 끝까지 바가 차는 상태를 말할때 사용 (설치완료 등과같음)
progressbar.start(10) # 시작, 10ms 마다 움직임(속도)
progressbar.pack()

def progressbarbtncmd():
    progressbar.stop() # 작동 중지
progressbarbtn1 = Button(root, text = "중지", command=progressbarbtncmd) 
progressbarbtn1.pack() 

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum = 100, length = 150, variable=p_var2)
progressbar2.pack()
def progressbarbtncmd2():
    for i in range(1,101): #1 ~ 100
        time.sleep(0.01) # 0.01초 대기
        p_var2.set(i) # progressbar의 값을 설정
        progressbar2.update() #  UI업데이트
        print(p_var2.get())
progressbarbtn2 = Button(root, text = "중지", command=progressbarbtncmd2) 
progressbarbtn2.pack() 
# 9_프로그래스 바 설정 # 

# 8_콤보박스 설정 #
values = [str(i)+ "일" for i in range(1,32)] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root,height =5, values=values)
combobox.pack()
# combobox.set("카드 결재일") #최초 목록 제목 설정(값도 설정가능)
combobox.set(values[0])

readonlycombobox = ttk.Combobox(root,height =10, values=values, state = "readonly") # 읽기 전용
readonlycombobox.current(0)
readonlycombobox.pack()

def comboboxbtncmd():
    print(combobox.get()) # 선택된 값 표시
    print(readonlycombobox.get()) # 선택된 값 표시
comboboxbtn1 = Button(root, text = "선택", command=comboboxbtncmd) 
comboboxbtn1.pack()
# 8_콤보박스 설정 #

# 7_라디오박스 설정 #
# radiobox = Label(root, text= "메뉴를 선택하세요.")
# radiobox.pack() 
# 위의 두줄을 아래와 같이 사용할 수도 있다. 다만 레이블의 값을 변경할 경우에는 변수에 저장해주어야한다.
Label(root, text= "메뉴를 선택하세요.").pack()
burger_var = IntVar() # 여기에 int형으로 값을 저장한다.
btn_burger1 = Radiobutton(root, text= "햄버거", value=1, variable = burger_var)
btn_burger1.select() # 기본 선택값
btn_burger2 = Radiobutton(root, text= "치즈버거", value=2, variable = burger_var)
btn_burger3 = Radiobutton(root, text= "치킨버거", value=3, variable = burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()
Label(root, text= "음료를 선택하세요.").pack()
drink_var = StringVar()
btn_drink1= Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink2= Radiobutton(root, text="제로콜라", value="제로콜라", variable=drink_var)
btn_drink2.select()
btn_drink3= Radiobutton(root, text="펩시콜라", value="팹시콜라", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def radioboxbtncmd():
    print(burger_var.get()) # 햄버거 중 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get())
radioboxbtn1 = Button(root, text = "주문", command=radioboxbtncmd) 
radioboxbtn1.pack()
# 7_라디오박스 설정 #

# 6_체크박스 설정 # 
chkvar = IntVar() # chkvar에 int형으로 값을 저장한다.
chkbox = Checkbutton(root, text = "오늘 하루 보지 않기", variable = chkvar) # variable에 체크유무를 저장하기에 필수로 필요하다.
chkbox.select() # 코드적으로 기본값이 선택이 되어있는 상태로 만들어준다.
chkbox.deselect() # 코드적으로 기본값이 선택이 되어있지 않은 상태로 만들어준다.
chkbox.pack()
chkvar2 = IntVar() # chkvar에 int형으로 값을 저장한다.
chkbox2 = Checkbutton(root, text = "일주일 동안 보지 않기", variable = chkvar2) # variable에 체크유무를 저장하기에 필수로 필요하다.
chkbox2.pack()

def checkboxbtncmd():
    print(chkvar.get()) # 체크의 값을 취득, 0: 체크해제, 1:체크상태
    print(chkvar2.get()) # 체크의 값을 취득, 0: 체크해제, 1:체크상태
checkboxbtn1 = Button(root, text = "체크박스 데이터 확인", command=checkboxbtncmd) 
checkboxbtn1.pack()
# 6_체크박스 설정 #

# 5_리스트 박스 설정 #
listbox = Listbox(root,selectmode = "extended", height = 0)
# selectmode에는  single,extended등이 있는데 single은 한개의 값만, extendend는 여러개의 값을 선택 가능하다.
# height는 0으로 설정시 리스트에 저장된 값의 갯수만큼 보여주고, 값을 지정한 경우는 지정된 값만큼의 공간을 만든뒤 리스트를 표시해준다.
listbox.insert(0,"사과")
listbox.insert(END,"수박") # 인덱스를 지정해주면 해당 인덱스에 데이터가 들어가지만 순서가 상관이 없을 경우 END로 지정하여 순차적으로 입력되도록 사용한다. 
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END,"포도")
listbox.pack()

def listbtncmd():
    listbox.delete(END) # delete() 리스트 박스의 값을 삭제, 인덱스 값을 지정하면 인덱스 데이터가 삭제된다.(0,1,2,...)
def listbtncmd2():
    print("리스트박스에는 ",listbox.size(),"개의 데이터가 있습니다.")
def listbtncmd3():
    print("1번째부터 3번째까지의 항목은 : ",listbox.get(0,END)) # 리스트의 인덱스를 지정
def listbtncmd4():
    print("선택된 항목 : ", listbox.curselection()) # 선택된 인덱스값을 확인

listbtn1 = Button(root, text = "리스트 데이터 삭제", command=listbtncmd) 
listbtn1.pack()

listbtn2 = Button(root, text = "리스트 갯수 확인", command = listbtncmd2)
listbtn2.pack()

listbtn3 = Button(root, text = "리스트 항목 확인", command = listbtncmd3)
listbtn3.pack()
listbtn4 = Button(root, text = "선택된 항목 확인", command = listbtncmd4)
listbtn4.pack()
# 5_리스트 박스 설정 #

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

