# Quiz) tkinter를 이용한 메모장 프로그램을 만드시오.

# [GUI 조건]
# 1. title :  제목 없음 - Windows 메모장
# 2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
# 3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
# 3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
# 3-3. 끝내기 : 프로그램 종료
# 4. 프로그램 시작 시 본문은 비어 있는 상태
# 5. 하단 status 바는 필요 없음
# 6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함
# 7. 본문 우측에 상하 스크롤 바 넣기
import os
from tkinter import *

root = Tk()
root.title("Windows 메모장")
root.geometry("300x200+100+100") #  크기 설정
root.resizable(True,True) # 크기 변경 가능
menu = Menu(root)
menu_file = Menu(menu,tearoff = 0)
filename = "mynote.txt"
def open_file(): # 파일 입출력에 대한 복습이 필요하다.
    if os.path.isfile(filename): # 파일이 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf8") as file:
            text.delete("1.0",END)
            text.insert(END,file.read())

def save_file(): # 파일 입출력에 대한 복습이 필요하다.
    with open(filename, "w", encoding="utf8") as file:
        file.write(text.get("1.0",END))

menu_file.add_command(label="열기",command=open_file)
menu_file.add_command(label="저장",command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기",command=root.quit)
menu.add_cascade(label="파일",menu = menu_file)

menu_edit = Menu(menu,tearoff = 0)
menu.add_cascade(label="편집",menu = menu_edit)

menu_rule = Menu(menu,tearoff = 0)
menu.add_cascade(label="서식",menu = menu_rule)

menu_view = Menu(menu,tearoff = 0)
menu.add_cascade(label="보기",menu = menu_view)

menu_help = Menu(menu,tearoff = 0)
menu.add_cascade(label="도움말",menu = menu_help)

root.config(menu=menu)

frame = Frame(root)
frame.pack()
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

text = Text(frame,yscrollcommand=scrollbar.set)
# Text()에서 width=300,height=200 로 창과같은 사이즈로 설정하는것말고 pack()에서 fill, expand로 하는편이 좋다.

text.pack(side="left",fill="both", expand=True)
scrollbar.config(command=text.yview)

root.mainloop()