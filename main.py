import os
from time import sleep
from selenium import webdriver
import random
import time
from collections import Counter

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import re

driver = webdriver.Chrome()
driver.implicitly_wait(5)

class InstaBot():
    def __init__(self):
        pass

    def login(self, username, password):

        driver.get("https://www.instagram.com")

        username_input = driver.find_element_by_css_selector("input[name='username']")
        password_input = driver.find_element_by_css_selector("input[name='password']")

        username_input.send_keys(username)
        sleep(0)
        password_input.send_keys(password)
        sleep(0)

        login_button = driver.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(0)

        not_now_btn = driver.find_element_by_xpath("//button[text()='Not Now']")
        not_now_btn.click()
        sleep(0)

        not_now_btn2 = driver.find_element_by_xpath("//button[text()='Not Now']")
        not_now_btn2.click()
        sleep(0)

        hashtags = list()
        users = list()
        whitelist = list()
        tag_list = list()
        max_number_of_likes = 0
        desired_following = 0
        desired_unfollowing = 0

    # 1
    def like(self, max_number_of_likes, tags, time_between, skip_top_nine):

        for tag in range(len(tags)):
            driver.get(f'https://www.instagram.com/tags/{tags[tag]}')

            # Intial
            posts = None
            if skip_top_nine:
                posts = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]')
            else:
                posts = driver.find_element_by_xpath('/html/body/div[1]/section/main/article')

            a_element = posts.find_elements_by_tag_name('a')

            actual_links = list()

            for x in range(len(a_element)):
                if len(actual_links) < max_number_of_likes:
                    actual_links.append(a_element[x].get_attribute('href'))

            while len(actual_links) < max_number_of_likes:
                driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
                a_element = posts.find_elements_by_tag_name('a')

                for x in range(len(a_element)):
                    if a_element[x].get_attribute('href') in actual_links:
                        pass
                    else:
                        if len(actual_links) < max_number_of_likes:
                            actual_links.append(a_element[x].get_attribute('href'))
                sleep(1)

            # with open('links.txt', "a") as f:
            #     for x in range(len(actual_links)):
            #         print(actual_links[x], file=f)

            for x in range(len(actual_links)):
                print(x)
                driver.get(actual_links[x])
                try:
                    dur1 = time_between
                    dur2 = time_between
                    print(dur1)
                    print(dur2)
                    sleep(dur1)
                    driver.find_element_by_xpath(
                        '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
                    sleep(dur2)
                except NoSuchElementException:
                    continue

    # 2
    def follow(self,accounts_to_follow, follow_user, follow_followers, post_index, follow_likers, hashtag, skip_top_nine,
               time_between):
        # just following user
        if follow_user and follow_followers == 0:
            for names in accounts_to_follow:
                driver.get(f'https://www.instagram.com/{names}/')
                driver.implicitly_wait(5)
                user_account = driver.find_element_by_xpath(
                    "/ html/body/div[1]/div/div/section/main/div/header/section/div[1]/div[2]/div / div / div / span / span[1] / button").click()

        # if following user and following the user's followers
        if follow_followers > 0 and follow_user:
            # accounts_to_follow += 1
            for names in accounts_to_follow:
                driver.get(f'https://www.instagram.com/{names}/')
                driver.implicitly_wait(5)
                user_account = driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button").click()
                sleep(time_between)
                followers = driver.find_element_by_xpath(
                    "/ html / body / div[1] / div / div / section / main / div / header / section / ul / li[2] / a")
                followers.click()

                for x in range(follow_followers):
                    try:
                        index = x + 1
                        driver.find_element_by_xpath(
                            f"/html/body/div[6]/div/div/div[2]/ul/div/li[{index}]/div/div[3]/button").click()
                        sleep(time_between)
                    except NoSuchElementException:
                        x += 1
                        continue
        # if following the user's followers, but not following the user
        if follow_followers > 0 and not follow_user:
            driver.get(f'https://www.instagram.com/{accounts_to_follow[1]}/')
            driver.implicitly_wait(5)
            followers = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
            followers.click()

            for x in range(follow_followers):
                try:
                    index = x + 1
                    driver.find_element_by_xpath(
                        f"/html/body/div[6]/div/div/div[2]/ul/div/li[{index}]/div/div[3]/button").click()
                except NoSuchElementException:
                    x -= 1
                    continue

        if follow_likers > 0 and not post_index == [""]:
            # get post here
            for posts in post_index:
                driver.get(f'{posts}')
                sleep(time_between)
                # open likes page
                likes = driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[2]/div/div/a").click()
                sleep(time_between)
                for x in range(follow_likers):
                    try:
                        like_index = x + 1
                        driver.find_element_by_xpath(
                            f"/html/body/div[6]/div/div/div[2]/div/div/div[{like_index}]/div[3]/button").click()
                        sleep(time_between)
                    except NoSuchElementException:
                        continue
        # follow from post index
        if not post_index == [""]:
            for posts in post_index:
                driver.get(f'{posts}')
        if not hashtag == [""]:
            for hashtags in hashtag:
                ran_once = False
                driver.get(f'https://www.instagram.com/explore/tags/{hashtags}/')
                for x in range(len(hashtag)):
                    if not ran_once and not skip_top_nine:
                        driver.find_element_by_xpath(
                            f"/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]").click()
                    elif not ran_once and skip_top_nine:
                        driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]").click()
                    sleep(time_between)
                    try:
                        driver.find_element_by_xpath(
                            ("/html/body/div[6]/div[2]/div/article/header/div[2]/div[1]/div[2]/button")).click()
                        print("Couldnt follow from tag")
                    except NoSuchElementException:
                        continue
                    sleep(time_between)

                    if ran_once:
                        driver.find_element_by_xpath("/html/body/div[6]/div[1]/div/div/a[2]").click()
                    if skip_top_nine:
                        driver.find_element_by_xpath("/html/body/div[6]/div[1]/div/div/a[2]").click()
                        ran_once = True
                    elif not ran_once and not skip_top_nine:
                        driver.find_element_by_xpath("/html/body/div[6]/div[1]/div/div/a").click()
                        ran_once = True

    # 3
    def unfollow(users_unfollow, followers_unfollow, time_between):
        # unfollow from list of following
        if followers_unfollow > 0:
            driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span").click()
            driver.find_element_by_xpath(
                "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div").click()
            driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
            followers = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/ul/div")
            for x in range(followers_unfollow + 1):
                if x == 0:
                    continue
                try:
                    # unfollowing user
                    driver.find_element_by_xpath(
                        f"/html/body/div[6]/div/div/div[3]/ul/div/li[{x}]/div/div[3]/button").click()
                    sleep(time_between)
                    # confirming unfollow
                    driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()
                except NoSuchElementException:
                    x -= 1
                    print("no such catched")
                    continue

        # unfollow a list of users
        if not users_unfollow == [""]:
            for names in users_unfollow:
                driver.get(f'https://www.instagram.com/{names}/')
                sleep(time_between)
                driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button/div/span").click()

                sleep(time_between)
                driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]").click()

    # 4
    def comment(self, max_number_of_comments, comment_input, tag_list, skip_top_nine=True, feed=False):
        if feed:
            driver.get("https://www.instagram.com/")
            for r in range(1, max_number_of_comments):
                try:
                    comment_clicker = driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[1]/div[3]/div/article[" + str(r) + "]/div[3]/section[3]/div/form/textarea")
                    comment_clicker.click()
                    comment_clicker = driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[1]/div[3]/div/article[" + str(r) + "]/div[3]/section[3]/div/form/textarea")
                    comment_clicker.send_keys(comment_input)
                    comment_clicker = driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[1]/div[3]/div/article[" + str(r) + "]/div[3]/section[3]/div/form/button[2]")
                    comment_clicker.click()
                    sleep(2)
                except NoSuchElementException:
                    driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)

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
                    posts = driver.find_element_by_xpath('/html/body/div[1]/section/main/article')
                    link_list = posts.find_elements_by_tag_name('a')
                    real_links = list()
                    while len(real_links) < max_number_of_comments:
                        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
                        link_list = posts.find_elements_by_tag_name('a')
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
        pass

    # 5
    def dm(self, max_number_of_dms, dm_input, skip_top_nine, tag_list, users_input, users=False):
        if users:
            for user in range(len(users_input)):
                driver.get("https://www.instagram.com/direct/new/")
                dm_clicker = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/input")
                dm_clicker.click()
                dm_clicker = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/input")
                dm_clicker.send_keys(users_input[user])
                dm_clicker = driver.find_element_by_xpath(
                    "/html/body/div[2]/div/div/div[2]/div[2]/div/div/div[3]/button/span")
                dm_clicker.click()
                sleep(3)
                dm_clicker = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div/button/div")
                dm_clicker.click()
                sleep(3)
                dm_clicker = driver.find_element_by_xpath(
                    "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
                dm_clicker.click()
                dm_clicker = driver.find_element_by_xpath(
                    "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
                dm_clicker.send_keys(dm_input)
                dm_clicker = driver.find_element_by_xpath(
                    "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
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
                        dm_clicker = driver.find_element_by_xpath(
                            "/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/input")
                        dm_clicker.click()

                        s = dm_list[y]
                        result = re.search('https://www.instagram.com/(.*)/', s)
                        print(result.group(1))
                        dm_clicker.send_keys(result.group(1))

                        dm_clicker = driver.find_element_by_xpath(
                            "/html/body/div[2]/div/div/div[2]/div[2]/div/div/div[3]/button/span")
                        dm_clicker.click()
                        sleep(3)
                        dm_clicker = driver.find_element_by_xpath(
                            "/html/body/div[2]/div/div/div[1]/div/div[2]/div/button/div")
                        dm_clicker.click()
                        sleep(3)
                        dm_clicker = driver.find_element_by_xpath(
                            "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
                        dm_clicker.click()
                        dm_clicker = driver.find_element_by_xpath(
                            "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
                        dm_clicker.send_keys(dm_input)
                        dm_clicker = driver.find_element_by_xpath(
                            "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
                        dm_clicker.click()
                else:
                    posts = driver.find_element_by_xpath('/html/body/div[1]/section/main/article')
                    link_list = posts.find_elements_by_tag_name('a')
                    real_links = list()
                    while len(real_links) < max_number_of_dms:
                        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
                        link_list = posts.find_elements_by_tag_name('a')
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
                        dm_clicker = driver.find_element_by_xpath(
                            "/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/input")
                        dm_clicker.click()

                        s = dm_list[y]
                        result = re.search('https://www.instagram.com/(.*)/', s)
                        print(result.group(1))
                        dm_clicker.send_keys(result.group(1))

                        dm_clicker = driver.find_element_by_xpath(
                            "/html/body/div[2]/div/div/div[2]/div[2]/div/div/div[3]/button/span")
                        dm_clicker.click()
                        sleep(3)
                        dm_clicker = driver.find_element_by_xpath(
                            "/html/body/div[2]/div/div/div[1]/div/div[2]/div/button/div")
                        dm_clicker.click()
                        sleep(3)
                        dm_clicker = driver.find_element_by_xpath(
                            "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
                        dm_clicker.click()
                        dm_clicker = driver.find_element_by_xpath(
                            "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
                        dm_clicker.send_keys(dm_input)
                        dm_clicker = driver.find_element_by_xpath(
                            "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
                        dm_clicker.click()
        pass
