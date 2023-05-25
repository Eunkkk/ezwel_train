"""
Author : EUNKYU BAEK
GitHub :
이지웰 기차 예약 자동화
Last Modification : 2020.03.02.
"""
import sys
import time
import ezwel_bot as eb

print("Process Strat...")
print("입력된 id: ", sys.argv[1])
print("입력된 pw: ", "***")
print("입력된 출발지: ", sys.argv[3])
print("입력된 목적지: ", sys.argv[4])

# 시작시간 기록
start_time = time.time()
# 입력받은 id set
id = sys.argv[1]
# 입력받은 pw set
pw = sys.argv[2]
# 입력받은 출발지 set
dep_city = sys.argv[3]
# 입력받은 목적지 set
arr_city = sys.argv[4]
# 크롤러 가져옴
BOT = eb.EzwelBot()
# 로그인 동작
BOT.login(id, pw)
# 팝업 체크
BOT.popup_check()
# 윈도우 리스트 확인
BOT.print_window()
# 트레일 메뉴 클릭
BOT.click_trail_menu()
# 윈도우 리스트 확인
BOT.print_window()
# 윈도우 탭 변경
BOT.switch_tap()
# 윈도우 리스트 확인
BOT.print_window()
# 도시 선택
BOT.choice_city(dep_city, arr_city)