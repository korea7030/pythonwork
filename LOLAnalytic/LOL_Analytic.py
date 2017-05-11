# selenium 관련 모듈
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# beautifulsoup 관련 모듈
from bs4 import BeautifulSoup
# collection dictionary 관련 모듈
import collections
# mongodb 모듈
import pymongo

import sys

# url 정보
base_url = 'http://lol.inven.co.kr/dataninfo/match/teamList.php?'
page_url = 'pg={}'
base_url_2 = '&iskin=lol&shipGroup=1&teamName=SKT+T1'

# xpath 정보
listTop_xpath = "//div[@class='listTop']"
wTeam_xpath = "//div[@class='wTeam']"
lTeam_xpath = "//div[@class='lTeam']"
score_xpath = "//div[@class='score']"

player_lst = [] # a tag click 시 나타나는 html에 대한 정보 list

game = collections.OrderedDict() # 입력한 순서대로 dictionary
p_keys = ['K', 'D', 'A', 'KDA', 'help'] # KDA 입력위한 dictionary key 값
p_dict = collections.OrderedDict() # player data dictionary

# mongodb connection 및 document 설정
client = pymongo.MongoClient('localhost', 27017)
db = client['lol_database']
games_doc = db.games
players_doc = db.players

firefox = Firefox()
for page in range(1,11):
    full_url = base_url + page_url.format(page) + base_url_2
    firefox.get(full_url)
    listFrame = firefox.find_elements_by_xpath("//div[@class='listFrame']")

    for lst in listFrame:
        game["date"] = lst.find_element_by_class_name('date').text
        p_dict['date'] = lst.find_element_by_class_name('date').text
        # print(lst.find_element_by_class_name('title').text) # 대회 title
        game["title"] = lst.find_element_by_class_name('title').text
        p_dict['title'] = lst.find_element_by_class_name('title').text
        # print(lst.find_element_by_class_name('stage').text)  # 경기 수
        game["stage"] = lst.find_element_by_class_name('stage').text
        lst.find_element_by_class_name('listDetail').find_element_by_class_name('detail').click()

        wait = WebDriverWait(firefox, 10)
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'player')))

        print(lst.find_element_by_class_name('wTeam').find_element_by_class_name('leftPart').find_element_by_class_name('teamname').text)
        if lst.find_element_by_class_name('wTeam').find_element_by_class_name('leftPart').find_element_by_class_name('teamname').text in ['SKT T1', 'SK Telecom T1']:
            print("--------------------------------wTeam이 SK인경우--------------------------------")
            game["win_team"] = lst.find_element_by_class_name('wTeam').find_element_by_class_name('leftPart').find_element_by_class_name('teamname').text
            game["res"] = lst.find_element_by_class_name('wTeam').find_element_by_class_name('rightPart').text
            p_dict["res"] = lst.find_element_by_class_name('wTeam').find_element_by_class_name('rightPart').text
            game["opp_team"] = lst.find_element_by_class_name('lTeam').find_element_by_class_name('rightPart').find_element_by_class_name('teamname').text

            player_list = lst.find_element_by_class_name('detailTable').find_element_by_class_name('left')
            players = player_list.find_elements_by_tag_name("li")
            player_lst = players

            for player in player_lst:
                # print(player.get_attribute('innerHTML'))
                soup = BeautifulSoup(player.get_attribute('innerHTML'), "lxml")

                player_name = soup.find('a') # player id
                champion = soup.find("img", class_='champicon', onmouseover=True) # champion

                if player_name is not None:
                    p_dict['player'] = player_name.text
                # print(soup)
                    if champion is not None:
                        champ_arr = champion['onmouseover'].split("'")  # champion 명만 뽑기
                        p_dict['champion'] = champ_arr[1]

                        p2_lst = soup.find('ul', class_='p2')
                        # print(p2_lst)
                        p_list = []
                        if p2_lst is not None:
                            for p2 in p2_lst:
                                # print(p2)
                                p_list.append(p2.text)

                            for i, key in enumerate(p_keys):
                                p_dict[key] = p_list[i]
                            # print(p_dict)
                            try:
                                if "_id" in p_dict:
                                    del p_dict["_id"]
                                print(p_dict)
                                players_doc.insert_one(p_dict)
                            except:
                                print("insert failed", sys.exc_info())
                                client.close()
                        else:
                            continue

                    else :
                        continue
                else:
                    continue
        else :
            print("--------------------------------lTeam이 SK인 경우--------------------------------")
            game["win_team"] = lst.find_element_by_class_name('lTeam').find_element_by_class_name(
                'rightPart').find_element_by_class_name('teamname').text
            game["res"] = lst.find_element_by_class_name('lTeam').find_element_by_class_name('leftPart').text
            p_dict["res"] = lst.find_element_by_class_name('lTeam').find_element_by_class_name('leftPart').text
            game["opp_team"] = lst.find_element_by_class_name('wTeam').find_element_by_class_name(
                'leftPart').find_element_by_class_name('teamname').text

            player_list = lst.find_element_by_class_name('detailTable').find_element_by_class_name('right')
            players = player_list.find_elements_by_tag_name('li')
            player_lst = players

            # print(player_lst)
            for player in player_lst:
                soup = BeautifulSoup(player.get_attribute('innerHTML'), "lxml")
                player_name = soup.find('a')
                # print(soup)
                champion = soup.find("img", class_='champicon', onmouseover=True)  # champion

                if player_name is not None:
                    p_dict['player'] = player_name.text
                    # print(soup)
                    if champion is not None:
                        champ_arr = champion['onmouseover'].split("'")  # champion 명만 뽑기
                        p_dict['champion'] = champ_arr[1]

                        p2_lst = soup.find('ul', class_='p2')
                        p_list = []
                        if p2_lst is not None:
                            for p2 in p2_lst:
                                # print(p2)
                                p_list.append(p2.text)

                                # print(p_list)
                            for i, key in enumerate(p_keys):
                                p_dict[key] = p_list[i]
                            # print(p_dict)
                            try:
                                if "_id" in p_dict:
                                    del p_dict["_id"]
                                print(p_dict)
                                players_doc.insert_one(p_dict)
                            except:
                                print("insert failed", sys.exc_info())
                                client.close()
                        else:
                            continue
                    else:
                        continue
                else:
                    continue

        # collection.insert(game)
        print(game)
        try:
            if "_id" in game:
                del game["_id"]
            games_doc.insert_one(game)
        except:
            print("insert failed", sys.exc_info())
            client.close()
        # print(p_dict)
        print("--------------------------------------------------------------------------------------") # 점수

client.close()
firefox.close()