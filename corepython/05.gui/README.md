# 5. GUI Programming
- http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/

Example	Filename
5-1	tkhelloA.py (tkhello1.py in early printings of this book)
5-2	tkhelloB.py (tkhello2.py in early printings of this book)
5-3	tkhelloC.py (tkhello3.py in early printings of this book)
5-4	tkhelloD.py (tkhello4.py in early printings of this book)
5-5	pfaGUI.py (pfaGUI2.py in early printings of this book)
5-6	listdir.py
5-7	animalTix.pyw
5-8	animalPmw.pyw
5-9	animalWx.pyw
5-10	animalGtk.pyw
5-11	animalTtk.pyw
5-12	animalTtk3.pyw
extra	animalPmw3.pyw
extra	animalTix3.pyw
extra	listdir3.py
extra	pfaGUI3.py
extra	tkhelloA3.py
extra	tkhelloB3.py
extra	tkhelloC3.py
extra	tkhelloD3.py

Note: there is no "animalGtk3.py" (Python 3 version of animalGtk.py)

- Tkinter
    - 파이썬의 기본 GUI Library / UI Toolkit
    - Tk Toolkit 을 기반으로 하고, Tcl(Tool Command Language)을 위해 만들어진 것
    - Install
        - >>> import Tkinter
- 5 단계
    - 1) from Tkinter import *
    - 2) 최상위 윈도우 객체 생성 : top = Tkinter.Tk()
    - 3) GUI 컴포넌트 구성
    - 4) 애플리케이션 코드 연결
    - 5) 메인 이벤트 루프 실행 : Tkinter.mainloop()