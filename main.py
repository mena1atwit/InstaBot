import os
from time import sleep
from selenium import webdriver
import random
import time
from collections import Counter
from selenium.webdriver.common.keys import Keys
import re

driver = webdriver.Chrome()


def login(username, password):

    username = input("Enter Username: wheis12")
    password = input("Enter Password: Chowder888")

    driver.get("https://www.instagram.com")

    username_input = driver.find_element_by_css_selector("input[name='username']")
    password_input = driver.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(username)
    sleep(5)
    password_input.send_keys(password)
    sleep(5)

    login_button = driver.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep(5)

    not_now_btn = driver.find_element_by_xpath("//button[text()='Not Now']")
    not_now_btn.click()
    sleep(5)

    not_now_btn2 = driver.find_element_by_xpath("//button[text()='Not Now']")
    not_now_btn2.click()
    sleep(5)

hashtags = list()
users = list()
whitelist = list()
tag_list = list()
max_number_of_likes = 0
desired_following = 0
desired_unfollowing = 0

def tags_sorting(hashtags):
    for tags in hashtags:
        tag_list.append(f'https://www.instagram.com/tags/{hashtags[tags]}/')



def input_loop(do_tag=False, do_user=False, do_whitelist=False):
    start_bool = do_tag or do_user or do_whitelist
    if not start_bool:
        raise ValueError('One argument must be set true')
    the_strings = ["tag", "user", "whitelist user"]
    lists = [hashtags, users, whitelist]

    filler_string = ''
    chosen_list = list()
    if do_tag:
        filler_string = the_strings[0]
        chosen_list = lists[0]
    if do_user:
        filler_string = the_strings[1]
        chosen_list = lists[1]
    if do_whitelist:
        filler_string = the_strings[2]
        chosen_list = lists[2]

    do_cont = True

    while do_cont:
        user_input = input(f"Enter a {filler_string}: ")
        chosen_list.append(user_input)
        cont = input("Continue? (Y or N): ")
        if cont.lower() == "y":
            do_cont = True
        else:
            do_cont = False

def random():
    first_session = ["1", "2", "3", "4", "5"]
    random.shuffle(first_session)

    for number in first_session:
        print(number)

    comment(feed=True)
# 1
def like(max_number_of_likes, skip_top_nine):

    if skip_top_nine:


    number_of_likes = 0
    #for every post liked, number_of_likes++
    if number_of_likes >= max_number_of_likes:
        #stop liking, and return to first_session, find next index.

    pass


# 2
def follow(accounts_to_follow, accounts_to_follow_following, accounts_to_follow_likers, post_index, hashtags, time_between, skip_top_nine):
    follows = 0
    accounts_list = ["", accounts_to_follow]
   # subcount = driver.find_element_by_id("subscriber-count").text
    #print(subcount)
    followers = driver.find_element_by_class_name("-nal3").click
    for x in range(desired_following):
        index = 1
        driver.find_element_by_xpath(f"/html/body/div[6]/div/div/div[2]/ul/div/li[{index}]]/div/div[2]/button").click
        index += 1

    for account in accounts_list:
        accounts_list.append(account)
    if follows < desired_following:
        #stop following

    pass


# 3
def unfollow(users_unfollow, whitelist, desired_unfollowing, time_between):
    unfollow_users = users_unfollow
    #unfollow input users
    list_intersection = set.intersection(set(unfollow_users),set(whitelist))
    #do not unfollow intersections
    unfollowed = 0
    #for every person unfollowed, unfollowed++
    if unfollowed >= desired_unfollowing:
        #stop unfollowing, and return to first_session, find next index
    pass


# 4
def comment(max_number_of_comments, comment_input, skip_top_nine, feed=False):
    if feed:
        driver.get("https://www.instagram.com/")

    else:
        for tag in range(len(tag_list)):
            driver.get(f'https://www.instagram.com/tags/{tag_list[tag]}/')
            if skip_top_nine:
                recent_posts = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div')
                link_list = recent_posts.find_elements_by_tag_name('a')

                real_links = list()
                while len(real_links) < max_number_of_comments:
                    driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
                    link_list = recent_posts.find_elements_by_tag_name('a')
                    for x in range(len(link_list)):
                        if link_list[x].get_attribute("href") in real_links:
                            pass
                        else:
                            if len(real_links) < max_number_of_comments:
                                real_links.append(link_list[x].get_attribute("href"))
                print(real_links)
                for z in range(len(real_links)):
                    driver.get(real_links[z])
                    time1 = random.uniform(5, 10)
                    time2 = random.uniform(5, 10)
                    time3 = random.uniform(5, 10)
                    print(time1)
                    print(time2)
                    print(time3)
                    print(z)
                    try:
                        comment_clicker = driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
                        comment_clicker.click()
                        sleep(time1)
                        comment_clicker = driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
                        comment_clicker.send_keys(comment_input)
                        sleep(time2)
                        comment_clicker = driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]")
                        comment_clicker.click()
                        sleep(time3)
                    finally:
                        continue

            else:
                while len(real_links) < max_number_of_comments:
                    driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
                    link_list = recent_posts.find_elements_by_tag_name('a')
                    for x in range(len(link_list)):
                        if link_list[x].get_attribute("href") in real_links:
                            pass
                        else:
                            if len(real_links) < max_number_of_comments:
                                real_links.append(link_list[x].get_attribute("href"))
                print(real_links)
                for z in range(len(real_links)):
                    driver.get(real_links[z])
                    time1 = random.uniform(5, 10)
                    time2 = random.uniform(5, 10)
                    time3 = random.uniform(5, 10)
                    print(time1)
                    print(time2)
                    print(time3)
                    print(z)
                    try:
                        comment_clicker = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
                        comment_clicker.click()
                        sleep(time1)
                        comment_clicker = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
                        comment_clicker.send_keys(comment_input)
                        sleep(time2)
                        comment_clicker = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]")
                        comment_clicker.click()
                        sleep(time3)
                    finally:
                        continue
    pass
# 5
def dm(max_number_of_dms, dm_input, skip_top_nine, tag_list, users= []):
    if users:
        for user in users:
            driver.get("https://www.instagram.com/direct/new/")
            dm_clicker = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/input")
            dm_clicker.click()
            dm_clicker.send_keys(users[user])
            dm_clicker = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/div[3]/button/span")
            dm_clicker.click()
            sleep(3)
            dm_clicker = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div/button/div")
            dm_clicker.click()
            sleep(3)
            dm_clicker = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/textarea[1]")
            dm_clicker.click()
            dm_clicker = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/textarea[1]")
            dm_clicker.send_keys(dm_input)
            dm_clicker = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]")
            dm_clicker.click()

    else:
        for tag in range(len(tag_list)):
            driver.get(f'https://www.instagram.com/tags/{tag_list[tag]}/')
            if skip_top_nine:
                recent_posts = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div')
                link_list = recent_posts.find_elements_by_tag_name('a')

                real_links = list()
                while len(real_links) < max_number_of_dms:
                    driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
                    link_list = recent_posts.find_elements_by_tag_name('a')
                    for x in range(len(link_list)):
                        if link_list[x].get_attribute("href") in real_links:
                            pass
                        else:
                            if len(real_links) < max_number_of_dms:
                                real_links.append(link_list[x].get_attribute("href"))
                    print(real_links)

                dm_list = list()
                for z in range(len(real_links)):
                    driver.get(real_links[z])
                    user_link = driver.find_element_by_xpath(
                        "/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/span/a")
                    dm_list.append(user_link.get_attribute("href"))
                for y in range(len(dm_list)):
                    driver.get("https://www.instagram.com/direct/new/")
                    dm_clicker = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/input")
                    dm_clicker.click()

                    s = dm_list[y]
                    result = re.search('https://www.instagram.com/(.*)/', s)
                    print(result.group(1))
                    dm_clicker.send_keys(result.group(1))

                    dm_clicker = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/div[3]/button/span")
                    dm_clicker.click()
                    sleep(3)
                    dm_clicker = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div/button/div")
                    dm_clicker.click()
                    sleep(3)
                    dm_clicker = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/textarea[1]")
                    dm_clicker.click()
                    dm_clicker = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/textarea[1]")
                    dm_clicker.send_keys(dm_input)
                    dm_clicker = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]")
                    dm_clicker.click()
    pass

def main():
    input_loop(do_tag=True)


if __name__ == '__main__':
    main()
