from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import NoSuchElementException

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

def getMovieList():
    movieList=[]
    movieElements=driver.find_elements(By.CSS_SELECTOR,'li.bestChartList_chartItem__bJ0PK')
    for element in movieElements:
        item = { 'title': '', 'open_date': '', 'audience': '', 'element': None }
        divText = element.find_elements(By.CSS_SELECTOR, 'div.bestChartList_textArea__SKJ3_') 
        spanName = divText[0].find_elements(By.CSS_SELECTOR, 'span.bestChartList_name__sZyhY') 
        pDate = divText[0].find_elements(By.CSS_SELECTOR, 'p.bestChartList_info__SZwYg') 
        spanAudience = divText[0].find_elements(By.CSS_SELECTOR, 'span.bestChartList_textStick__v4WU_')
        item['title']=spanName[0].text.strip()
        if len(spanAudience)>0: 
            item['audience']=spanAudience[0].text.strip()
        else:
            item['open_date']=pDate[0].text.strip()
        item['element']=element
        movieList.append(item)
    return movieList
def getMovieElement(movieList,movieTitle):
    found_element=None
    for i in range(len(movieList)):
        if found_element==None and movieList[i]['title']==movieTitle:
            found_element=movieList[i]['element']
            print(movieTitle,"찾았음!")
            break
    return found_element
def selectDay_UsingNextClass():
        next_day_element = driver.find_element(By.CSS_SELECTOR, 
            'div.swiper-slide.swiper-slide-next.dayScroll_scrollItem__IZ35T')
        next_day_element.click()
        time.sleep(2)
        return True
def timeselct():
    timeap_element=driver.find_element(By.CSS_SELECTOR,
        'div.cnms01648_timeBtnsWrap__WZAAh')
    times=timeap_element.find_elements(By.XPATH,"./button")
    for timed in times:
        if "오후" in timed.text:
            timed.click()
            print("오후 찾음! 오후 클릭!")
            return True
    return False
def selectMovie(element):
    driver.execute_script("arguments[0].scrollIntoView();",element)
    button=element.find_element(By.CSS_SELECTOR,'button.btn.btn-md.line-main')
    time.sleep(2)
    button.click()
    print("예매 클릭!")
    time.sleep(2)
def selectCity(cityName):
    cityElement=driver.find_element(By.CSS_SELECTOR,
        'div.bottom_theaterList__zuOJA.bottom_region__2bZCS')
    cities=cityElement.find_elements(By.XPATH,"./ul/li/button")
    for city in cities:
        if cityName in city.text:
            city.click()
            print(cityName,"찾음! 도시 클릭!")
            time.sleep(2)
            return True
    return False


def select_second_showtime():
    try:
        showtime_list = driver.find_elements(By.CSS_SELECTOR, 'li.screenInfo_timeItem__y8ZXg')
        
        if len(showtime_list) >= 2:
            second_showtime = showtime_list[1]
            button_to_click = second_showtime.find_element(By.TAG_NAME, 'button')
            start_time = button_to_click.find_element(By.CSS_SELECTOR, 'span[class*="screenInfo_start"]').text
            button_to_click.click()
            return True
        else:
            return False
            
    except Exception as e:
        return False
def selectTheater(theaterName):
    theaterElements=driver.find_element(By.CSS_SELECTOR,'div.bottom_listCon__8g46z')
    theaters=theaterElements.find_elements(By.XPATH,"./ul/li/button")
    for cinema in theaters:
        if theaterName==cinema.text:
            cinema.click()
            print(theaterName,"찾음 극장 클릭!")
            time.sleep(2)
            button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-100.fill-black')
            button.click()
            print("극장선택 클릭!")
            return True
    return False

if __name__=='__main__':
    url='https://cgv.co.kr/cnm/cgvChart/movieChart'
    driver.get(url)
    time.sleep(3)

    movieList=getMovieList()
    element=getMovieElement(movieList,"극장판 귀멸의 칼날: 무한성편")
    selectMovie(element)
    if selectCity("경기"):
        time.sleep(3)
        if selectTheater("광교"):
            print("영화, 도시, 극장선택완료")
            time.sleep(3)
            selectDay_UsingNextClass()
            time.sleep(3)
            timeselct()
            time.sleep(3)
            select_second_showtime()
            time.sleep(5)
    driver.quit()