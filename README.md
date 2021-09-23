# PythonGUI
Python GUI program

작업 환경 
1. OS : macOS Big Sur 11.5.2 
2. 언어 : Python 3.9.7 
3. IDE(편집기) : VS CODE 
4. tkinter : kinter, t-kinter, tk-inter등으 불리며, 파이썬 설치시 자동 설치되는 기본 패키지

공부 자료 출처 : 유투브 "나도코딩" nadocoding.tistory.com
2021년 9월 23일
    GUI 프로그램 기본 프레임 설정(1_create_frame.py)
        1. GUI 프로그램을 만들기 위해 도움을 받을 패키지 tkinter를 임포트 
            from tkinter import *
        2. 프로그램 초기화 및 메인 루프 설정
            pygame에서도 초기화 작업과 실제 이벤트를 구현하는 부분과 동일하다.
            root = Tk()
            root.mainloop()
        3. 제목 설정
            root.tilte()
                예 : "프로그램명"
                프로그램을 실행 시켰을 때의 프로그램명을 설정해줄수 있다.
        4. 프로그램의 창 사이즈 및 시작 위치 설정
            root.geometry()
                예 : "(가로)x(세로)+(x축)+(y축)"
                가로와세로값만 작성하면 시작위치는 디폴트값으로 설정되어 프로그램이 실행된다.
                가로와 세로사이에는 소문자x로 띄어쓰기 없이 작성해야한다.
                시작위치는+뒤에 작성하되 x축만y축만 설정하는 것은 불가능하다. 0값이라도 입력하여야한다.
        5. 프로그램의 창 사이즈 조절여부 설정
            root.resizable()
                예 : bool,bool
                입력값은 True, False의 boolean값을 입력하며 순서대로 x축,y축 창 사이즈 변경여부를 설정한다.
2021년 9월 22일
    GUI 프로그램 만들기 환경 설정(1_create_frame.py)
        파이썬 설치시 기본포함 패키지라고 설명되었지만 현재 사용중인 PC는 M1 맥북
        brew로 패키지를 관리중인데 파이썬만 설치시에는 tkinter가 찾을 수 없다는 에러가 발생했다.
        별도의 tk 패키지를 설치해야한다.
            해결방법 : brew install python-tk@3.9