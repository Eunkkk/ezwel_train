"""
Author : EUNKYU BAEK
GitHub :
이지웰 기차 예약 자동화
Last Modification : 2020.03.02.
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class EzwelBot:
    def __init__(self):
        # 셀레늄 웹드라이버에 입력할 옵션을 지정합니다.
        self.options = Options()
        # 옵션에 해상도를 입력합니다.
        self.options.add_argument("--window-size=1024,768")
        # 옵션에 헤드리스를 명시합니다. 주석을 해제하면 헤드리스로 작업이 수행됩니다.
        # self.options.add_argument("headless")
        # 옵션을 입력해서 크롬 웹드라이버를 불러옵니다.
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)
        # 트윗할 메시지들을 저장할 공간을 만듭니다.
        self.contents = []

    # 크롤러를 종료하는 메서드입니다.
    # 굳이 한줄짜리 코드를 함수로 만든 데에는 여러 이유가 있습니다만,
    # 쉽게 설명하자면 클래스 외부에서 클래스 내부 자료에 너무 깊게 관여하는 상황을 원하지 않기 때문입니다.
    def kill(self):
        self.driver.quit()

    # 로그인을 수행하는 메서드입니다.
    def login(self, id, ps):
        # 트위터 로그인창으로 들어갑니다.
        self.driver.get("https://nhic.ezwel.com/")
        # 로딩이 오래 걸릴 수 있으니 잠시 대기합니다.
        time.sleep(3)
        # 아이디를 입력하기 위해 아이디 입력창 요소를 찾아옵니다.
        id_input = self.driver.find_element(By.NAME, "loginSearchBean.userId")
        # id를 입력합니다.
        id_input.send_keys(id)

        # 비밀번호를 입력합니다.
        # 트위터의 경우 비밀번호 입력창은 session[password] 라는 이름을 갖고 있습니다.
        ps_input = self.driver.find_element(By.NAME, "loginSearchBean.password1")
        ps_input.send_keys(ps)
        ps_input.send_keys(Keys.RETURN)

    def popup_check(self):
        time.sleep(2)
        is_display = self.driver.find_element(By.ID, "hd_main_layer_popup" ).is_displayed()
        if is_display:
            popup_close_btn = self.driver.find_element(By.CLASS_NAME, "hd_popup_layer_cls")
            popup_close_btn.click()

    def click_trail_menu(self):
        all_menu_xpath = '//*[@id="maingnb_wrap"]/div[1]/a'
        all_menu = self.driver.find_element(By.XPATH, all_menu_xpath)
        all_menu.send_keys(Keys.ENTER)
        time.sleep(1)
        trail_menu_xpath = '//*[@id="topgnb_wrap"]/div[2]/div/div/div/div[1]/div[5]/ul/li[7]/a'
        trail_menu = self.driver.find_element(By.XPATH, trail_menu_xpath)
        trail_menu.send_keys(Keys.ENTER)

    # 윈도우 리스트 확인
    def print_window(self):
        print(self.driver.window_handles)

    # 윈도우 탭 변경
    def switch_tap(self):
        last_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(last_tab)

    def choice_city(self):
        time.sleep(5)
        choice_btn = self.driver.find_element(By.CLASS_NAME, "city-select")
        choice_btn.click()

