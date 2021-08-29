
def follow(accounts_to_follow, accounts_to_follow_following, post_likers, post_index, desired_following_likes, hashtags, desired_following, time_between, skip_top_nine):
    follows = 0
    accounts_list = ["", accounts_to_follow]

    followers = driver.find_element_by_class_name("-nal3").click
    for x in range(desired_following):
        index = 1
        driver.find_element_by_xpath(f"/html/body/div[6]/div/div/div[2]/ul/div/li[{index}]]/div/div[2]/button").click
        index += 1
    for y in range(desired_following_likes):
        like_index = 1
        driver.find_element_by_xpath("").click

        #xpath if post found through navigation
        #/ html / body / div[6] / div[2] / div / article / div[3] / section[2] / div / div / a

        #link of post (is same regardless of post
        #/ html / body / div[1] / section / main / div / div[1] / article / div[3] / section[2] / div / div / a

        like_index+=1
    for liker in post_likers:
        accounts_list.append(liker)
    for account in accounts_list:
        accounts_list.append(account)

    if follows < desired_following:
        main()

    pass


def main():
    follow()


if __name__ == '__main__':
    main()
