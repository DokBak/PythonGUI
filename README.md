# PythonGUI
Python GUI program

작업 환경 
1. OS : macOS Big Sur 11.5.2 
2. 언어 : Python 3.9.7 
3. IDE(편집기) : VS CODE 
4. tkinter : kinter, t-kinter, tk-inter등으 불리며, 파이썬 설치시 자동 설치되는 기본 패키지

공부 자료 출처 : 유투브 "나도코딩" nadocoding.tistory.com

2021년 10월 2일
    GUI 프로그램 이미지 합치기프로그램(4_merge_image.py)
        1. 파이썬 이미지 라이브러리를 선언
            from PIL import ImageGrab
        2. 선택된 리스트의 정보 취득
            변수명 = Image.open()
                파라미터 : 파일의 경로
            변수명.size[0] : 가로 길이
            변수명.size[1] : 세로 길이
        3. 결과물 이미지의 크기 계산
            가로 길이는 각각의 이미지들의 최대값
            세로 길이는 각각의 이미지들의 총합
        4. 스케치북 준비
            변수명 = Image.new()
                파라미터 : "RGB", (사이즈), "배경색"
                "RGB"는 고정값 (다른 설정옵션이 있을수도 있음)
                (사이즈)는 튜플로 가로세로 길이를 명시(3.의 값을 기입)
                (255,255,255) 흰색으로 지정
        5. 세로길이 위치정보 설정
            세로길이 위치정보를 설정해주지 않을 경우 같은 좌표에 이미지들이 중복되어 합쳐지는 결과가 나온다.
            이미지의 세로값을 더해주면서 위치정보를 변경해준다.
        6. 이미지 붙이기
            이미지변수명.paste()
                파라미터 : 이미지파일변수,(좌표)
                이미지리스트에서 하나씩 작업을 할때 순서에 맞는 리스트 파일을 의미
                좌표는 x좌표는 0으로 고정, y좌표는 5.에서 작업했던 세로길이 위치정보를 설정
        7. 파일경로 설정
            변수명 = os.path.join()
                파라미터 : 파일경로, 파일명
                파일경로는 저장될 파일의 경로를 의미
                파일명은 저장된 파일의 이름을 의미
        8. 파일 저장
            변수명.save()
                파라미터 : 파일경로
                7.에서 만든 파일경로를 지정
    GUI 프로그램 이미지 합치기프로그램(4_merge_image.py)
        1. progress bar 설정
            진행상황은 현재 어떤 이미지를 작업하는지에 대한 인덱스를 확인 할 수 있으면 된다.
            enumerate()함수를 이용
    GUI 프로그램 이미지 합치기프로그램(practice2.py, 4_merge_image.py)
        1. zip()
            파라미터 : 리스트, 리스트
            두개의 리스트를 하나의 리스트로 합칠 경우에 사용한다. 리스트에는 튜플형식으로 저장된다.
            리스트 이외의 데이터도 가능한지는 추후 공부해볼것
        2. zip(*)
            파라미터 : zip()으로 합쳐진 상태처럼 각 인덱스의 값이 튜플형식으로 저장된 리스트를 분해하는 기능
            분해하고자하는 리스트 앞에 * 를 추가한다.
            
2021년 10월 1일
    GUI 프로그램 자동 스크린 샷 저장(3_auto_screenshot.py)
        1. 파이썬 이미지 라이브러리를 선언
            from PIL import ImageGrab 
        2. 현재 스크린 이미지를 저장
            변수명 = ImageGrab.grab()
                파라미터 : 별도로 없음
            변수명.save()
                파라미터 : 저장될 파일 이름

2021년 9월 29일
    GUI 프로그램 이미지 합치기프로그램(2_basic_function.py)
        1. from tkinter import filedialog
            파일 탐색기를 여는 패키지가 있으므로 추가만 해주면 된다.
            기본 패키지를 추가시키는 __all__에 정의 된 내용만 사용가능하다.
                from tkinter import *
        2. 파일 탐색기 열어 파일 선택
            변수명 = filedialog.askopenfilenames()
                파라미터 : title, filetypes, initialdir
                title은 파일탐색기의 이름
                filetypes는 확장자를 정하는 옵션을 부여할수 있다. 가급적 튜플 형식으로 작성 
                    예) ("PNG 파일","*.png")
                initialdir는 파일 탐색기가 최초에 여는 경로를 보여준다.
        3. 파일 탐색기에서 폴더 선택
            변수명 = filedialog.askdirectory()
                파라미터 : 별도로 없음
        4. 파일 추가
            파일 탐색기를 열어서 작업을 할 파일을 선택해 추가한다.
        5. 선택 삭제
            리스트박스에서 선택된 내용을 삭제한다.
            리스트박스에서 선택된 내용을 삭제시 리스트의 인덱스를 뒤에서부터 삭제한다.
                for index in reversed(list_file.curselection())
                앞에서부터 삭제하면 뒤의 인덱스가 한 칸씩 앞으로 오며 선택내용이 삭제 안 될 수 있다.
        6. 저장 경로(폴더)
            파일 탐색기에서 폴더를 선택하여, 프로그램의 저장경로 위치에 반영해준다.
        7. 시작
            선택된 각 옵션들을 값 확인
            파일 목록에 값이 있는지 확인
            저장 경로가 선택되어 있는지 확인
    리스트의 reverse와 reversed의 차이(practice.py)
        1. reverse
            리스트.reverse
                리스트의 순서를 아예 역으로 바꾼다.
        2. reversed
            reversed(리스트)
                reversed()의 파라미터로 리스트를 넣어준다.
        3. 결론
            리스트를 역으로 바꾸는 리스트의 기능으로써 바꾸는건지 별도의 함수로써 바꾸는건지를 확인할 수 있다.
            
2021년 9월 28일
    GUI 프로그램 이미지 합치기프로그램(1_create_layout.py)
        1.  프레임 구성
                파일 프레임
                리스트 프레임
                저장경로 프레임
                옵션 프레임
                    가로 넓이 레이블
                    가로 넓이 콤보
                    간격 옵션 레이블
                    간격 옵션 콤보
                    파일 포멧 레이블
                    파일 포멧 콤보
                진행 상황 프레임
                실행 프레임
        2. 이 파일에서는 프로그램의 레이아웃 정의 하였다.

2021년 9월 27일
    GUI 프로그램 메시지박스 설정(11_messagebox.py)
        1. 메시지박스 패키지 포함
            import tkinter.messagebox as msgbox
            메시지 박스의 경우 별도의 패키지에 있기에 이렇게 패키지 포함
        2. 알림 메시지 
            msgbox.showinfo()
                파라미터 : 프로그램 바 표시메시지, 메시지박스 내 표시메시지
                이미지 : i의 원 이미지(파랑)
                버튼 : 확인
        3. 경고 메시지
            msgbox.showwarning()
                파라미터 : 프로그램 바 표시메시지, 메시지박스 내 표시메시지
                이미지 : !의 삼각형 이미지(노랑)
                버튼 : 확인
        4. 에러 메시지
            msgbox.showerror()
                파라미터 : 프로그램 바 표시메시지, 메시지박스 내 표시메시지
                이미지 : X의 원 이미지(빨강)
                버튼 : 확인
        5. 확인 취소 메시지
            msgbox.askokcancel()
                파라미터 : 프로그램 바 표시메시지, 메시지박스 내 표시메시지
                이미지 : ?의 원 이미지(파랑)
                버튼 : 확인, 취소
        6. 재시도 취소 메시지
            msgbox.askretrycancel()
                파라미터 : 프로그램 바 표시메시지, 메시지박스 내 표시메시지
                이미지 : !의 삼각형 이미지(노랑)
                버튼 : 재시도, 취소
        7. 예 아니오 메시지
            msgbox.askyesno()
                파라미터 : 프로그램 바 표시메시지, 메시지박스 내 표시메시지
                이미지 : ?의 원 이미지(파랑)
                버튼 : 예, 아니오
        8. 예 아니오 취소 메시지
            msgbox.askyesnocancel()
                파라미터 : 프로그램 바 표시메시지, 메시지박스 내 표시메시지
                이미지 : ?의 원 이미지(파랑)
                버튼 : 예, 아니오, 취소
        9. 메시지박스 버튼값 취득
            각각의 메시지 박스 함수를 변수에 담아서 그 변수의 값을 확인한다.
            재시도, 확인 : 1 (True)
            아니오 : 0 (False)
            확인 : ok
            취소 : 예, 아니오, 취소의 경우 취소는 None값을 갖는다.
    GUI 프로그램 프레임 설정(12_frame.py)
        1. 프레임 설정
            변수명 = Frame()
                파라미터 : 프레임이 생성될 프로그램, relief, bd
                relief은 테두리 모양을 의미. 예)solid
                bd은 외곽선 두께 예) 1
        2. 프레임 반영
            변수명.pack()
                파라미터 : side, fill, expand
                side는 프레임이 표시될 위치
                fill은 꽉 채우는 옵션(상하)
                expand을 true로 넣으면 펼쳐지는 옵션(좌우)
        3. 프레임 사용법
            각종 기능들을 정의 할때 root에 표시되도록 설정하였는데 root가 아닌 프레임에 표시되도록 정의하면 관리가 편해진다.
    GUI 프로그램 스크롤바 설정(13_scrollbar.py)
        1. 스크롤바 사용팁
            스크롤바는 프레임으로 사용하고 싶은 기능과 세트로 설정해두는 것이 좋다.
        2. 스크롤바 설정
            변수명 = Scrollbar()
                파라미터 : 프레임변수
        3. 스크롤바 표시
            변수명.pack()
                파라미터 : side, fill
                side는 스크롤바는 보통 우측이나 아래에 위치했다.
                fill옵션을 주지 않는다면 기본값의 스크롤바로 설정된다. 예) "x"나 "y"로 설정
        4. 스크롤바와 연결 할 리스트박스 옵션 추가
            y축으로 설정된 스크롤바의 경우
                yscrollcommand = 변수명.set
        5. 리스트박스와 연결 할 스크롤바 설정
            변수명.config(command=listbox.yview)
        6. 4번과 5번의 설정이 있어주어야 리스트박스와 스크롤바와의 연동이 제대로 이루어진다.
    GUI 프로그램 그리드 설정(14.grid.py)
        1. 그리드 설정
            변수명.grid()
            파라미터 : row, column, rowspan, columspan, sticky, padx, pady
            row은 행 위치
            colum은 열 위치
            rowspan은 현재 위치로부터 아래쪽으로 몇 줄을 더함
            columspan은 현재 위치로부터 오른쪽으로 몇 칸을 더함
            sticky는 N+E+W+S 와 같이 방향을 지정해서 늘린다.
            padx는 내부 내용을 기준으로 x축의 길이를 늘린다.
            pady는 내부 내용을 기준으로 y축의 길이를 늘린다.
            버튼등을 표시할때는 지금까지는 pack()으로 표시하였는데 pack()은 쌓는 느낌이고, grid()는 좌표에 위치시키는 느낌이다.
            

2021년 9월 26일
    GUI 프로그램 메뉴 설정(10_menu.py)
        1. 메뉴 사전 정보
            MAC OS에서는 tkinter만으로는 메뉴바 생성이 안된다.(?) 
                - 이 코드로는 메뉴가 표시되지 않았다.
        2. 메뉴 선언
            변수명 = Menu()
                파라미터 : 메뉴가 생성될 프로그램
        3. 메뉴 표시
            메뉴가 생성될 프로그램.config(menu= 변수명)
                예) root.config(menu = menu)
        4. 세부메뉴 선언
            변수명 = Menu()
                파라미터 : [2.]의변수명, tearoff = 0
        5. 세부메뉴의 기능 추가
            변수명.add_command()
                파라미터 : label, command, state
                label은 표시되는 메뉴의 이름
                command은 실행 내용 
                    ※command = root.quit으로 하면 프로그램종료
                state를 disable로 설정하면 비활성화
        6. 세부메뉴 구분자
            변수명.add_separator()
                파라미터 : 별도로 없음
        7. 상위메뉴와 하위메뉴를 연결
            변수명.add_cascade()
                파라미터 : label, [2.]의변수명
                label은 표시될 메뉴명
                [2.]의변수명 = 하위 메뉴변수명
    GUI 프로그램 퀴즈(15_quiz.py)
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
        파일 입출력에 대한 부분은 한 번더 공부해볼것.

2021년 9월 25일
    GUI 프로그램 체크박스 설정(6_checkbox.py)
        1. 체크박스 설정
            변수명 = Checkbutton()
                파라미터 : 체크박스가 생성될 프로그램, 체크박스설명(text), 체크여부변수(varibale)
                text에는 체크박스의 설명을 작성.
                variable에는 체크 박스에 체크여부를 판단하는 변수를 체크박스 전에 선언후 사용한다.
                예) chkvar = IntVar()
        2. 체크박스 디폴트 선택 설정
            변수명.select()
                파리미터 : 별도로 없음
                기본값이 선택이 되어있는 상태로 설정
            변수명.deselect()
                파라미터 : 별도로 없음
                기본값이 선택이 되어있지 않은 상태로 설정
        3. 체크되어있는 값을 취득 
            variable의변수명.get()        
                파라미터 : 별도로 없음
                취득값이 0 : 체크 해제상태, 1 : 체크 상태
    GUI 프로그램 라디오버튼 설정(7_radiobutton.py)
        1. 라디오버튼 설정
            변수명 = Radiobutton()
                파라미터 : 라디오버튼이 생성될 프로그램, 라디오버튼설명(text), 값(value), 라디오버튼체크여부변수(variable) 
                text에는 라디오버튼의 설명을 작성
                value 해당 라디오버튼에 설정할 값
                variable에는 라디오박스의 체크여부를 판단하는 변수를 사용 [예) 변수명 = StringVar()을 선언해서 문자열로도 받을 수 있다.]
        2. 라디오버튼 디폴트 선택 설정
            변수명.select()
                파라미터 : 별도로 없음
        3. 체크되어있는 값을 취득
            variable의변수명.get()
                파라미터 : 별도로 없음
    GUI 프로그램 콤보박스 설정(8_combobox.py)
        1. 콤보박스를 사용하기 위한 패키지 임포트
            기존 tkinter 사용 임포트
                from tkinter import *
            콤보박스의 패키지는 tkinter내에 ttk폴더에 존재에 하므로
                import tkinter.ttk as ttk
        2. 콤보박스 설정
            변수명 = ttk.Combobox()
                파라미터 : 콤보박스가 생성될 프로그램, height, values, state
                height : 콤보박스에서 한 번에 몇개의 데이터가 표시되는지를 설정
                values : 콤보박스에 표시될 데이터 리스트
                state : "readonly"로 설정 할 경우, 콤보박스는 읽기전용으로만 사용
        3. 기본값 설정
            변수명.set()
                파라미터 : 파라미터로 작성된 값이 기본값으로 설정된다. 콤보박스 값도 가능
                            예)값을 선택해주세요.
            변수명.current()
                파라미터 : 지정한 인덱스 값이 기본값으로 표시
        4. 체크되어있는 값을 취득 
            변수명.get()
                파라미터 : 별도로 없음
    GUI 프로그램 프로그래스 바 설정(9_progressbar.py)
        1. 프로그래스바를 사용하기 위한 패키지 임포트
            기존 tkinter 사용 임포트
                from tkinter import *
            프로그래스바의 패키지는 tkinter내에 ttk폴더에 존재에 하므로
                import tkinter.ttk as ttk
        2. 프로그래스바 설정
            변수명 = ttk.Progressbar()
                파라미터 : 프로그래스바가 생성될 프로그램, maximum, mode, length, variable
                maximum : 최대값을 지정(일반적으로 100%를 최대값으로 생각하기에 100으로 설정)
                mode : 표시 모드를 설정
                    indeterminate : 언제끝이 날지 모르는 상태를 표시(좌우로 움직이는 형태로 표시됨)
                    determinate : 시작에서부터 끝까지 바가 차는 상태를 표시(좌에서 우로 게이지가 차는 형태로 표시됨)
                length : 프로그래스바의 길이를 설정
                variable : 현재 상태의 값을 확인 가능하다.
        3. 프로그래스바 업데이트
            변수명.update()
                파라미터 : 별도로 없음
                variable값이 시간에 따라, 작업 진척에 따라 진척상황을 표시할 때 실시간으로 보여주기 위함

2021년 9월 24일
    GUI 프로그램 레이블 설정(3_label.py)
        1. 레이블 설정
            변수명 = Label()
                파라미터 : 레이블이 생성될 프로그램, 각종 옵션
        2. 레이블 객체 프로그램에 반영
            변수명.pack()
        3. 레이블 옵션 image
            해당 레이블에 이미지 파일을 설정
        4. 레이블 옵션 config
            레이블의 기존기능을 변경해준다.
        5. 함수내에 있는 변수를 프로그램 내에서도 지속적으로 사용하고 싶을 경우 글로벌변수(global)로 설정해주어야 한다.
            global 변수명
    GUI 프로그램 텍스트위젯, 엔트리 설정(4_txt_entry.py)
        1. 텍스트위젯 설정
            변수명 = Text()
                파라미터 : 텍스트위젯이 생성될 프로그램, width,height 텍스트 위젯의 크기
                여러줄 입력이 가능하다.
        2. 텍스트위젯 초기값 설정
            변수명.insert()
                파라미터 : END, "표시값"
                END는 삽입 위치(INDEX)를 의미하는듯 싶다.
        3. 텍스트 위젯 내용 취득
            변수명.get()
                파라미터 : 시작위치,끝위치
                시작위치는 "1.0"으로 입력시 1은 첫번째 라인을 의미하고, 0은 0번째 인덱스를 의미
                끝위치는 END를 사용하여 끝까지를 의미
        4. 텍스트 내용 삭제
            변수명.delete()
                파라미터 : 시작위치,끝위치
                시작위치는 "1.0"으로 입력시 1은 첫번째 라인을 의미하고, 0은 0번째 인덱스를 의미
                끝위치는 END를 사용하여 끝까지를 의미
        5. 엔트리 설정
            변수명 = Entry()
                파라미터 : 엔트리가 생성될 프로그램, width(가로길이)
                한 줄만 입력가능하므로 height옵션은 없다.
        6. 엔트리 초기값 설정
            변수명.insert()
                파라미터 : 0(인덱스 0번째부터), "표시값"
                한 줄만 입력이 가능하다.
        7. 엔트리 내용 취득
            변수명.get()
                파라미터 : 별도로 없음
        8. 엔트리 내용 삭제
            변수명.delete()
                파라미터 : 0,END
                인덱스 0부터 끝까지의 내용을 삭제
    GUI 프로그램 리스트박스 설정(5_listbox.py)
        1. 리스트박스 설정
            변수명 = Listbox()
                파라미터 : 리스트박스가 생성될 프로그램, selectmode, height
                selectmode에 설정값은 extended와 single이 있다.
                    extended : 리스트박스에서 다중 선택을 허용
                    single   : 리스트박스에서 단일 선택만 가능
                height에서 설정값은 숫자로 설정
                    0인 경우는 리스트박스에서 표시될 리스트 숫자만큼을 전부 보여주는 옵션
                    1 이상의 숫자는 해당 숫자만큼의 표시해주는 옵션
        2. 리스트박스에 데이터 추가
            변수명.insert()
                파라미터 : 인덱스, 값
                인덱스는 숫자로 지정가능하며, END로 지정시 맨 뒤에 순차적으로 추가된다.
        3. 리스트박스에 데이터 삭제
            변수명.delete()
                파라미터 : 인덱스
                리스트박스의 값을 삭제할 인덱스 값을 지정
        4. 리스트박스의 데이터 갯수 확인
            변수명.size()
                파라미터 : 별도로 없음
        5. 리스트박스의 데이터 확인
            변수명.get()
                파라미터 : 0, END
                리스트박스의 데이터를 확인하고 싶은 인덱스 값을 지정 (시작위치, 종료위치)
        6. 리스트박스에서 선택된 항목 확인
            변수명.curselection()
                파라미터 : 별도로 없음
                선택된 인덳의 값이 출력된다.(한 개만 선택시에도 값뒤에 쉼표가 붙는 문제가 발생)

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
                파라미터 : "프로그램명"
                프로그램을 실행 시켰을 때의 프로그램명을 설정해줄수 있다.
        4. 프로그램의 창 사이즈 및 시작 위치 설정
            root.geometry()
                파라미터 : "(가로)x(세로)+(x축)+(y축)"
                가로와세로값만 작성하면 시작위치는 디폴트값으로 설정되어 프로그램이 실행된다.
                가로와 세로사이에는 소문자x로 띄어쓰기 없이 작성해야한다.
                시작위치는+뒤에 작성하되 x축만y축만 설정하는 것은 불가능하다. 0값이라도 입력하여야한다.
        5. 프로그램의 창 사이즈 조절여부 설정
            root.resizable()
                파라미터 : bool,bool
                입력값은 True, False의 boolean값을 입력하며 순서대로 x축,y축 창 사이즈 변경여부를 설정한다.
    GUI 프로그램 버튼 설정(2_button.py)
        1. 버튼 객체 생성 
            변수명 = Button()
                파라미터 : 버튼이 생성될 프로그램, 각종 옵션(텍스트, 사이즈, 색설정 등등) 
        2. 버튼 객체 프로그램에 반영
            변수명.pack()
                파라미터 : 별도로 없음
        3. 버튼 옵션 text
            버튼에 표시되는 값을 설정
        3. 버튼 옵션 fg
            버튼에 표시되는 텍스트의 색을 설정
        4. 버튼 옵션 bg
            버튼의 배경색을 설정
        5. 버튼 옵션 padx,pady
            버튼의 크기 조절 : 내부 텍스트의 길이 + 여분의 길이
        6. 버튼 옵션 width, height
            버튼의 크기 조절 : 버튼 사이즈 고정
                버튼사이즈보다 텍스트가 긴 경우, 텍스트가 비정상 출력된다.
        7. 이미지 추출
            변수명 = PhotoImage()
                파라미터 : file = "경로"
        8. 버튼 옵션 image
            버튼의 표시 설정을 이미지로 설정
        9. 버튼 옵션 command
            버튼을 클릭시 동작하는 함수를 설정
            
2021년 9월 22일
    GUI 프로그램 만들기 환경 설정(1_create_frame.py)
        파이썬 설치시 기본포함 패키지라고 설명되었지만 현재 사용중인 PC는 M1 맥북
        brew로 패키지를 관리중인데 파이썬만 설치시에는 tkinter가 찾을 수 없다는 에러가 발생했다.
        별도의 tk 패키지를 설치해야한다.
            해결방법 : brew install python-tk@3.9