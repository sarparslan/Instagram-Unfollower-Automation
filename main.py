from selenium import webdriver
import time
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()

#Lists for holding the datas
followers_list = []
following_list = []
def login(username,password):
    browser.get("https://www.instagram.com/")
    time.sleep(2)

    username_box = browser.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
    username_box.click()
    username_box.send_keys(username)
    time.sleep(2)

    password_box = browser.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
    password_box.click()
    password_box.send_keys(password)
    time.sleep(2)

    login_button = browser.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div")
    login_button.click()
    time.sleep(3)

    #for avoid to save the login informations
    try:
        save_login_info = browser.find_element(By.XPATH,"/html/body/div[1]/section/main/div/div/div/div/button")
        save_login_info.click()
        time.sleep(2)
    except:
        pass

    #for turn off notifications
    try:
        turn_off_notifications = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]")
        turn_off_notifications.click()
        time.sleep(2)
    except:
        pass

def getFollowers():
    #finding and then clicking the profile button
    profile_button = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a")
    profile_button.click()
    time.sleep(3)

    #finding and then clicking the followers button
    followers_button= browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div")
    followers_button.click()
    time.sleep(2)

    #JavaScript codes for using the scroll bar
    jscommand = """
       toscroll = document.querySelector("._aano");
       toscroll.scrollTo(0, toscroll.scrollHeight);
       var length=toscroll.scrollHeight;
       return length;
       """
    length = browser.execute_script(jscommand)
    match = False
    while (match == False):
        lastCount = length
        time.sleep(2)
        length = browser.execute_script(jscommand)
        if lastCount == length:
            match = True
    time.sleep(5.5)

    all_followers = browser.find_elements(By.CSS_SELECTOR,"._aacl._aaco._aacw._aacx._aad7._aade")
    for followers in all_followers:
        #adding items to the followers list
        followers_list.append(followers.text)

def getFollowing():
    time.sleep(7)
    #quiting the followers button in order to press the following button
    quit = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[3]/div/button")
    quit.click()
    time.sleep(3)

    #finding and then clicking the following button
    following_button= browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]/a/div")
    following_button.click()
    time.sleep(2)

    #JavaScript codes for using the scroll bar
    jscommand = """
    toscroll = document.querySelector("._aano");
    toscroll.scrollTo(0, toscroll.scrollHeight);
    var length=toscroll.scrollHeight;
    return length;
    """
    length = browser.execute_script(jscommand)
    match = False
    while (match == False):
        lastCount = length
        time.sleep(2)
        length = browser.execute_script(jscommand)
        if lastCount == length:
            match = True
    time.sleep(5.5)
    all_following = browser.find_elements(By.CSS_SELECTOR,"._aacl._aaco._aacw._aacx._aad7")

    for following in all_following:
       following_list.append(following.text)

def compare():
    #creating a new list for holding the unfollowers
    list_difference = []
    for item in following_list:
        if item not in followers_list:
            list_difference.append(item)
        else:
            continue
    print("Users Who Unfollowed")
    print('\n'.join(map(str, list_difference)))

login('username','password')
getFollowers()
getFollowing()
compare()