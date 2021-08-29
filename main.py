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

def tags_sorting(hashtags):
    for tags in hashtags:
        tag_list.append(f'https://www.instagram.com/tags/{hashtags[tags]}/')

def tag_navigation():



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
def like(max_number_of_likes, time_between, skip_top_nine):

    if skip_top_nine:


    number_of_likes = 0
    #for every post liked, number_of_likes++
    if number_of_likes >= max_number_of_likes:
        #stop liking, and return to first_session, find next index.

    pass


# 2
def follow(accounts_to_follow, accounts_to_follow_following, accounts_to_follow_likers, post_index, hashtags, desired_following, time_between, skip_top_nine):
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
def comment(hashtags, max_number_of_comments, time_between, comment_input, skip_top_nine, feed=False):
    if feed:
        driver.get("https://www.instagram.com/")

    if skip_top_nine:
        recent_posts = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div')
        links = recent_posts.find_elements_by_tag_name('a')

        def duplicate(link):
            return link not in links

        valid_links = list(filter(duplicate(), links))

        while len(slinks) < max_number_of_comments:
            driver.get(tag_list(0))
            comment_clicker = driver.find_element_by_xpath("/html[1]/body[1]/div[6]/div[2]/div[1]/article[1]/div[3]/section[3]/div[1]/form[1]/textarea[1]").click()
            comment_clicker.send_keys(comment)
            slinks = list()
            for x in range(len(links)):
                slinks.append(links[x].get_attribute('href'))

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
