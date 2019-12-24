import time

from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# Specify firefox.exe
binary = FirefoxBinary("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")

# Indicate saved firefox instance to use (remembers saved accounts & passwords)
profile = FirefoxProfile("C:\\Users\\Delbert_F\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\syov4xfw.default")

driver = webdriver.Firefox(profile)

# Which page/day to access 
# driver.get('https://fantasy.espn.com/basketball/team?leagueId=78370592&teamId=8&seasonId=2020')
# driver.get('https://fantasy.espn.com/basketball/team?leagueId=78370592&teamId=8&seasonId=2020&scoringPeriodId=65&statSplit=singleScoringPeriod')
driver.get('https://fantasy.espn.com/basketball/team?leagueId=78370592&teamId=8&seasonId=2020&scoringPeriodId=66&statSplit=singleScoringPeriod')

# TODO: Encapsulating for loop to automate action for each day


# Look at bench (last 3 slots/rows): find players with games on the bench
bench_arr = [0,0,0]    # represents 3 bench players and whether they have game

# check which bench player has game 
for i in range(11, 14):
    xpath = "//*[@id='espn-analytics']/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div/div/section/table/tbody/tr/td[1]/div/table/tbody/tr[" + str(i) + "]/td[4]/div"
    player = driver.find_element_by_xpath(xpath)

    if player.text[0] != "-":
        bench_arr[i-11] = 1

print(bench_arr)
    
# check if there's player with game on bench AND empty slot in roster, make swap
for i in range(len(bench_arr)):
    playing = bench_arr[i]
#     # bench player has game
    if playing == 1:
        i += 11
        benchbutton_xpath = "//*[@id='espn-analytics']/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div/div/section/table/tbody/tr/td[1]/div/table/tbody/tr[" + str(i) + "]/td[3]/div/div/button"
        # click on player's MOVE button
        benchbutton = driver.find_element_by_xpath(benchbutton_xpath)
        benchbutton.click()

        # only roster players with suitable position will have MOVE button avaiable to click
        for i in range(1,11):
            try:
                rosterbutton_xpath = "//*[@id='espn-analytics']/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div/div/section/table/tbody/tr/td[1]/div/table/tbody/tr[" + str(i) +"]/td[3]/div/div/button"
                rosterbutton = driver.find_element_by_xpath(rosterbutton_xpath)

                # if succesfully found button, check if player does not have game
                rosterplaying_xpath = "//*[@id='espn-analytics']/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div/div/section/table/tbody/tr/td[1]/div/table/tbody/tr[" + str(i) + "]/td[4]/div"
                rosterplaying = driver.find_element_by_xpath(rosterplaying_xpath)
                
                # if plyaer does not have game conduct swap
                if (rosterplaying.text[0] == "-"):
                    print("player " + str(i) + " is a suitable swap")
                    rosterbutton.click()
                    break   # end inner for loop, no need to look for next button

            # if roster player does onto contain button, goes into except block
            except:
                print("player " + str(i) + " is not a suitable swap")

        # NEED TO ADD LOGGING FOR EXCEPTION CASES

        # if cannot find player to swap
        print("EXCEPTION CASEl NO AVAILABLE PLAYERS TO CONDUCT SWAP WITH")
        
        # break outer for loop, stop considering subsequent bench players, require manual intervention to fix case
        break