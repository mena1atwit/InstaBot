
import os
from time import sleep
from selenium import webdriver
import random
import time
from collections import Counter

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

def tags_navigation(hashtags):
    for tags in hashtags:
        tag_list.append(f'https://www.instagram.com/tags/{hashtags[tags]}/')

def skip_nine():
    #skip the top 9 posts
    pass
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


# 1
def like(max_number_of_likes, time_between, skip_top_nine):

    if skip_top_nine:


        number_of_likes = 0
    #for every post liked, number_of_likes++
    if number_of_likes >= max_number_of_likes:
        # stop liking, and return to first_session, find next index.

        pass


# 2
def follow(accounts_to_follow, accounts_to_follow_following, accounts_to_follow_likers, post_index, hashtags, desired_following, time_between, skip_top_nine):
    accounts_to_follow = 5
    desired_following = 5
    desired_following_likes = 5
    follow_followers = True
    follow_likers = False
    follow_user = True
    # just following user
    if follow_user and not follow_followers:
        for names in account_names:
            driver.get(f'https://www.instagram.com/{names}/')
            driver.implicitly_wait(5)
            user_account = driver.find_element_by_xpath(
                "/ html/body/div[1]/div/div/section/main/div/header/section/div[1]/div[2]/div / div / div / span / span[1] / button").click()

    # if following user and following the user's followers
    if follow_followers and follow_user:
        desired_following += 1
        for names in account_names:
            driver.get(f'https://www.instagram.com/{names}/')
            driver.implicitly_wait(5)
            user_account = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button").click()
            sleep(2)
            followers = driver.find_element_by_xpath(
                "/ html / body / div[1] / div / div / section / main / div / header / section / ul / li[2] / a")
            followers.click()

            for x in range(desired_following):
                try:
                    index = x + 1
                    driver.find_element_by_xpath(
                        f"/html/body/div[6]/div/div/div[2]/ul/div/li[{index}]/div/div[3]/button").click()
                    sleep(1)
                except NoSuchElementException:
                    x += 1
                    continue
    # if following the user's followers, but not following the user
    if follow_followers and not follow_user:
        driver.get(f'https://www.instagram.com/{account_names}/')
        driver.implicitly_wait(5)
        followers = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        followers.click()

        for x in range(desired_following):
            try:
                index = x + 1
                driver.find_element_by_xpath(
                    f"/html/body/div[6]/div/div/div[2]/ul/div/li[{index}]/div/div[3]/button").click()
            except NoSuchElementException:
                x -= 1
                continue

    # if others we follow like it
    # /html/body/div[6]/div[2]/div/article/div[3]/section[2]/div/div[2]/a
    # if no others we follow like it
    # /html/body/div[6]/div[2]/div/article/div[3]/section[2]/div/div/a

    if follow_likers:
        # get post here
        driver.get('https://www.instagram.com/p/CSr9trvpAra/')
        sleep(2)
        # open likes page
        likes = driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[2]/div/div/a").click()
        sleep(2)
        for x in range(desired_following):
            try:
                like_index = x + 1
                driver.find_element_by_xpath(
                    f"/html/body/div[6]/div/div/div[2]/div/div/div[{like_index}]/div[3]/button").click()
                sleep(1)
            except NoSuchElementException:
                continue


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
def comment(hashtags, max_number_of_comments, time_between, comment_input, feed, skip_top_nine):
    comments = 0
    if skip_top_nine:
        skip_nine()
    while comments >= max_number_of_comments:
        if hashtags:
            driver.get(tag_list(0))

            comments += comments
        if feed:
            driver.get("https://www.instagram.com/")

            comments += comments
    #find comment input and start commenting from priority of hashtags>feed.
    #comments with timer
    random()
        #stop commenting, and return to first_session, find next index.
    pass


# 5
def dm(hashtags, number_of_dms, time_between, dm_input, users, skip_top_nine):
    # hashtags are presented in a list
    # goto hashtag index 0
    dm_max = number_of_dms
    dms = 0
    #get user dm input
    #timer inbetween
    #go through tags and/or users and dm
    if dms >= dm_max:
    # stop dming, and return to first_session, find next index.
        pass

def main():
    input_loop(do_tag=True)


if __name__ == '__main__':
    main()
