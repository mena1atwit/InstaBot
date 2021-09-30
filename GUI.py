import sys
from main import InstaBot
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QComboBox

bot = InstaBot()
bot.login("wheis13", "Chowder888")


class BoldTitle(QLabel):
    def __init__(self, text=''):
        super(BoldTitle, self).__init__()
        self.setText(text)

        self.setFont(QFont("San Serif", weight=QFont.Bold))


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('InstaBot')
        self.setFixedWidth(1000)

        mainLayout = QVBoxLayout()
        self.setStyleSheet("""QLineEdit{height: 15px; font-size: 15px}QLabel{font-size: 15px}""")

        # Like Section

        # Maximum Likes
        self.max_number_of_likes = QLineEdit()
        self.max_like_hbox = QHBoxLayout()
        self.max_like_hbox.addWidget(QLabel("Max Number of Likes "))
        self.max_like_hbox.addWidget(self.max_number_of_likes)

        # Like by Tags
        self.tags_like = QLineEdit()
        self.tags_like_hbox = QHBoxLayout()
        self.tags_like_hbox.addWidget(QLabel("Hashtags to Like "))
        self.tags_like_hbox.addWidget(self.tags_like)

        # Like Delay
        self.delay_like = QLineEdit()
        self.delay_like_hbox = QHBoxLayout()
        self.delay_like_hbox.addWidget(QLabel("Like Delay "))
        self.delay_like_hbox.addWidget(self.delay_like)

        # Skip Top Nine
        self.skip_top_nine_like = QComboBox()
        self.skip_top_nine_like.addItems(["Yes", "No"])
        self.skip_top_nine_like_hbox = QHBoxLayout()
        self.skip_top_nine_like_hbox.addWidget(QLabel("Skip Top Nine "))
        self.skip_top_nine_like_hbox.addWidget(self.skip_top_nine_like)

        # Order
        self.order_like = QLineEdit()
        self.order_like_hbox = QHBoxLayout()
        self.order_like_hbox.addWidget(QLabel("Order "))
        self.order_like_hbox.addWidget(self.order_like)

        # Like-Main Layout
        mainLayout.addWidget(BoldTitle("Like"))
        mainLayout.addLayout(self.max_like_hbox)
        mainLayout.addLayout(self.tags_like_hbox)
        mainLayout.addLayout(self.delay_like_hbox)
        mainLayout.addLayout(self.skip_top_nine_like_hbox)
        mainLayout.addLayout(self.order_like_hbox)

        # Comment Section

        # Max Number of Comments
        self.max_number_of_comments = QLineEdit()
        self.max_comments_hbox = QHBoxLayout()
        self.max_comments_hbox.addWidget(QLabel('Max Number of Comments '))
        self.max_comments_hbox.addWidget(self.max_number_of_comments)

        # Comment by Tags
        self.tags_comment = QLineEdit()
        self.tags_comment_hbox = QHBoxLayout()
        self.tags_comment_hbox.addWidget(QLabel("Hashtags to Comment "))
        self.tags_comment_hbox.addWidget(self.tags_comment)

        # Comment Delay
        self.delay_comment = QLineEdit()
        self.delay_comment_hbox = QHBoxLayout()
        self.delay_comment_hbox.addWidget(QLabel("Comment Delay "))
        self.delay_comment_hbox.addWidget(self.delay_comment)

        # Skip Top Nine
        self.skip_top_nine_comment = QComboBox()
        self.skip_top_nine_comment_hbox = QHBoxLayout()
        self.skip_top_nine_comment.addItems(["Yes", "No"])
        self.skip_top_nine_comment_hbox.addWidget(QLabel("Skip Top Nine "))
        self.skip_top_nine_comment_hbox.addWidget(self.skip_top_nine_comment)

        # Order
        self.order_like_comment = QLineEdit()
        self.order_like_comment_hbox = QHBoxLayout()
        self.order_like_comment_hbox.addWidget(QLabel("Order"))
        self.order_like_comment_hbox.addWidget(self.order_like_comment)

        # Comment Input
        self.comment_input = QLineEdit()
        self.comment_input_hbox = QHBoxLayout()
        self.comment_input_hbox.addWidget(QLabel("Comment Inputs "))
        self.comment_input_hbox.addWidget(self.comment_input)

        # Comment-Main Layout
        mainLayout.addWidget(BoldTitle("Comment"))
        mainLayout.addLayout(self.max_comments_hbox)
        mainLayout.addLayout(self.tags_comment_hbox)
        mainLayout.addLayout(self.delay_comment_hbox)
        mainLayout.addLayout(self.skip_top_nine_comment_hbox)
        mainLayout.addLayout(self.order_like_comment_hbox)
        mainLayout.addLayout(self.comment_input_hbox)

        # DM Section

        # Max DMs
        self.max_number_of_dms = QLineEdit()
        self.max_number_of_dms_hbox = QHBoxLayout()
        self.max_number_of_dms_hbox.addWidget(QLabel("Max Number of DMs "))
        self.max_number_of_dms_hbox.addWidget(self.max_number_of_dms)

        # DM Inputs
        self.dm_input = QLineEdit()
        self.dm_input_hbox = QHBoxLayout()
        self.dm_input_hbox.addWidget(QLabel("DM Inputs "))
        self.dm_input_hbox.addWidget(self.dm_input)

        # Skip Top Nine
        self.skip_top_nine_dm = QComboBox()
        self.skip_top_nine_dm.addItems(["Yes", "No"])
        self.skip_top_nine_dm_hbox = QHBoxLayout()
        self.skip_top_nine_dm_hbox.addWidget(QLabel("Skip Top Nine"))
        self.skip_top_nine_dm_hbox.addWidget(self.skip_top_nine_dm)

        # DM Tags
        self.tags_dm = QLineEdit()
        self.tags_dm_hbox = QHBoxLayout()
        self.tags_dm_hbox.addWidget(QLabel("Hashtags to DM "))
        self.tags_dm_hbox.addWidget(self.tags_dm)

        # DM Users
        self.users_dm = QLineEdit()
        self.users_dm_hbox = QHBoxLayout()
        self.users_dm_hbox.addWidget(QLabel("Users to DM "))
        self.users_dm_hbox.addWidget(self.users_dm)

        # DM Delay
        self.delay_dm = QLineEdit()
        self.delay_dm_hbox = QHBoxLayout()
        self.delay_dm_hbox.addWidget(QLabel("DM Delay"))
        self.delay_dm_hbox.addWidget(self.delay_dm)

        # DM-Main Layout
        mainLayout.addWidget(BoldTitle("Direct Message (DM)"))
        mainLayout.addLayout(self.max_number_of_dms_hbox)
        mainLayout.addLayout(self.dm_input_hbox)
        mainLayout.addLayout(self.skip_top_nine_dm_hbox)
        mainLayout.addLayout(self.tags_dm_hbox)
        mainLayout.addLayout(self.users_dm_hbox)
        mainLayout.addLayout(self.delay_dm_hbox)

        # Follow Section

        # Accounts to Follow
        self.accounts_to_follow = QLineEdit()
        self.accounts_to_follow_hbox = QHBoxLayout()
        self.accounts_to_follow_hbox.addWidget(QLabel("Accounts to Follow "))
        self.accounts_to_follow_hbox.addWidget(self.accounts_to_follow)

        # Follow Followers
        self.follow_followers = QComboBox()
        self.follow_followers.addItems(['Yes', 'No'])
        self.follow_followers_hbox = QHBoxLayout()
        self.follow_followers_hbox.addWidget(QLabel("Follow Followers "))
        self.follow_followers_hbox.addWidget(self.follow_followers)

        # Follow Likers
        self.follow_likers = QComboBox()
        self.follow_likers.addItems(['Yes', 'No'])
        self.follow_likers_hbox = QHBoxLayout()
        self.follow_likers_hbox.addWidget(QLabel("Follow Likers "))
        self.follow_likers_hbox.addWidget(self.follow_likers)

        # Post Index
        self.post_index = QLineEdit()
        self.post_index_hbox = QHBoxLayout()
        self.post_index_hbox.addWidget(QLabel("Post Index "))
        self.post_index_hbox.addWidget(self.post_index)

        # Follow Tags
        self.tags_follow = QLineEdit()
        self.tags_follow_hbox = QHBoxLayout()
        self.tags_follow_hbox.addWidget(QLabel("Hashtags to Follow"))
        self.tags_follow_hbox.addWidget(self.tags_follow)

        # Follow Delay
        self.delay_follow = QLineEdit()
        self.delay_follow_hbox = QHBoxLayout()
        self.delay_follow_hbox.addWidget(QLabel("Follow Delay "))
        self.delay_follow_hbox.addWidget(self.delay_follow)

        # Skip Top Nine
        self.skip_top_nine_follow = QComboBox()
        self.skip_top_nine_follow.addItems(["Yes", "No"])
        self.skip_top_nine_follow_hbox = QHBoxLayout()
        self.skip_top_nine_follow_hbox.addWidget(QLabel("Skip Top Nine"))
        self.skip_top_nine_follow_hbox.addWidget(self.skip_top_nine_follow)

        # Follow-Main Layout
        mainLayout.addWidget(BoldTitle('Follow'))
        mainLayout.addLayout(self.accounts_to_follow_hbox)
        mainLayout.addLayout(self.follow_followers_hbox)
        mainLayout.addLayout(self.follow_likers_hbox)
        mainLayout.addLayout(self.post_index_hbox)
        mainLayout.addLayout(self.tags_follow_hbox)
        mainLayout.addLayout(self.delay_follow_hbox)
        mainLayout.addLayout(self.skip_top_nine_follow_hbox)

        # Unfollow Section

        # Unfollow Users
        self.users_unfollow = QLineEdit()
        self.users_unfollow_hbox = QHBoxLayout()
        self.users_unfollow_hbox.addWidget(QLabel("Accounts to Unfollow "))
        self.users_unfollow_hbox.addWidget(self.users_unfollow)

        # Whitelist Users
        # self.whitelist = QLineEdit()
        # self.whitelist_hbox = QHBoxLayout()
        # self.whitelist_hbox.addWidget(QLabel("Whitelist Users "))
        # self.whitelist_hbox.addWidget(self.whitelist)

        # Desired Unfollow
        self.desired_unfollowing = QLineEdit()
        self.desired_unfollowing_hbox = QHBoxLayout()
        self.desired_unfollowing_hbox.addWidget(QLabel("Desired Unfollowing"))
        self.desired_unfollowing_hbox.addWidget(self.desired_unfollowing)

        # Unfollow Delay
        self.delay_unfollow = QLineEdit()
        self.delay_unfollow_hbox = QHBoxLayout()
        self.delay_unfollow_hbox.addWidget(QLabel("Unfollow Delay"))
        self.delay_unfollow_hbox.addWidget(self.delay_unfollow)

        # Unfollow-Main Layout
        mainLayout.addWidget(BoldTitle('Unfollow'))
        mainLayout.addLayout(self.users_unfollow_hbox)
        # mainLayout.addLayout(self.whitelist_hbox)
        mainLayout.addLayout(self.desired_unfollowing_hbox)
        mainLayout.addLayout(self.delay_unfollow_hbox)

        self.Confirm = QPushButton('Run')

        self.Confirm.setStyleSheet('font-size: 30px')
        mainLayout.addWidget(self.Confirm)
        self.Confirm.clicked.connect(self.confirm_click)
        self.setLayout(mainLayout)

    def confirm_click(self):
        # take out print when done testing

        # Likes
        max_num_likes_input = self.max_number_of_likes.text()
        tags_like_input = self.tags_like.text()
        delay_like_text_input = self.delay_like.text()
        skip_top_nine_like_input = self.skip_top_nine_like.currentText()
        skip_top_nine_like_input_bool = True
        if skip_top_nine_like_input.lower() == 'yes':
            skip_top_nine_like_input_bool = True
        else:
            skip_top_nine_like_input_bool = False

        # order_like_input = self.order_like.text()
        print("Likes:")
        print(str("Maximum Number of Likes: " + max_num_likes_input))
        print(str("Tags like: " + tags_like_input))
        print(str("Delay for Likes: " + delay_like_text_input))
        print(str("Skip Top Nine: " + skip_top_nine_like_input))
        # print("\n") #this is for skip
        # print(str("Order of Likes: " + order_like_input))
        print("\n")
        bot.like(int(max_num_likes_input), [tags_like_input], int(delay_like_text_input), skip_top_nine_like_input_bool)

        # Comments
        print("Comments: ")
        max_num_comments_input = self.max_number_of_comments.text()
        tags_comment_input = self.tags_comment.text()
        delay_comment_input = self.delay_comment.text()
        skip_top_nine_comment_input = self.skip_top_nine_comment.currentText()
        skip_top_nine_comment_input_bool = True
        if skip_top_nine_comment_input.lower() == 'yes':
            skip_top_nine_comment_input_bool = True
        else:
            skip_top_nine_comment_input_bool = False
        # order_comment_input = self.order_like_comment.text()
        commment_input_input = self.comment_input.text()
        print(str("Maximum Number of Comments: " + max_num_comments_input))
        print(str("Tags to Comment: " + tags_comment_input))
        print(str("Delay for Comments: " + delay_comment_input))
        # print("\n")  # this is for skip
        # print(str("Order of Comments: " + order_comment_input))
        print(str("Comment Input: " + commment_input_input))
        print("\n")
        bot.comment(int(max_num_comments_input), commment_input_input, [tags_comment_input], delay_comment_input, skip_top_nine_comment_input_bool)

        # dm
        print("Dms: ")
        max_num_dms_input = self.max_number_of_dms.text()
        dm_input_input = self.dm_input.text()
        # skip top 9
        tags_dm_input = self.tags_dm.text()
        users_dm_input = self.users_dm.text()
        delay_dm_input = self.delay_dm.text()
        skip_top_nine_dm_input = self.skip_top_nine_dm.currentText()
        skip_top_nine_dm_input_bool = True
        if skip_top_nine_dm_input.lower() == 'yes':
            skip_top_nine_dm_input_bool = True
        else:
            skip_top_nine_dm_input_bool = False
        print(str("Maximum Number of dms: " + max_num_dms_input))
        print(str("dm input: " + dm_input_input))
        # print("\n")  # this is for skip
        print(str("tags dm: " + tags_dm_input))
        print(str("users dm input: " + users_dm_input))
        print(str("delay dm: " + delay_dm_input))
        print("\n")
        bot.dm(int(max_num_dms_input), dm_input_input, [tags_dm_input], users_dm_input, skip_top_nine_dm_input_bool)

        # follow
        print("Follow: ")
        accounts_to_follow_input = self.accounts_to_follow.text()
        follow_followers_input = self.follow_followers.currentText()
        follow_likers_input = self.follow_likers.currentText()
        post_index_input = self.post_index.text()
        tags_follow_input = self.tags_follow.text()
        delay_follow_input = self.delay_follow.text()
        # top 9
        skip_top_nine_follow_input = self.skip_top_nine_dm.currentText()
        skip_top_nine_follow_input_bool = True
        if skip_top_nine_follow_input.lower() == 'yes':
            skip_top_nine_follow_input_bool = True
        else:
            skip_top_nine_follow_input_bool = False
        print(str("Accounts to follow: " + accounts_to_follow_input))
        print(str("follow_followers: " + follow_followers_input))
        print(str("follow likers: " + follow_likers_input))
        print(str("post index: " + post_index_input))
        print(str("tags follow: " + tags_follow_input))
        print(str("delay follow input: " + delay_follow_input))
        # print("\n")  # this is for skip
        print("\n")
        bot.follow([accounts_to_follow_input], int(follow_followers_input), int(follow_likers_input), [post_index_input], [tags_follow_input], int(delay_follow_input), skip_top_nine_follow_input_bool)

        # unfollow
        print("unfollow: ")
        users_unfollow_input = self.users_unfollow.text()
        # whitelist_input = self.whitelist.text()
        desired_unfollowing_input = self.desired_unfollowing.text()
        delay_unfollow_input = self.delay_unfollow.text()

        print(str("users to unfollow: " + users_unfollow_input))
        # print(str("whitelist " + whitelist_input))
        print(str("desired unfollowing: " + desired_unfollowing_input))
        print(str("delay unfollowing: " + delay_unfollow_input))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())
