import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QFont, QColor

class StandardItem(QStandardItem):
    def __init__(self, txt="", font_size=12, set_bold=False, color=QColor(0,0,0)):
        super().__init__()

        fnt = QFont("Open Sans", font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)

class Expandable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("InstaBot")
        self.resize(900, 850)

        collapsable = QTreeView()
        collapsable.setHeaderHidden(True)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()

        "--------------------------------------"

        Like = StandardItem("Like", 16, set_bold= True)
        max_number_of_likes = StandardItem("max_number_of_likes", 14)
        tags_like = StandardItem("tags", 14)
        delay_like = StandardItem("delay", 14)
        skip_top_9_like = StandardItem("delay", 14)
        order_like = StandardItem("order", 14)
        Like.appendRow(max_number_of_likes)
        Like.appendRow(tags_like)
        Like.appendRow(delay_like)
        Like.appendRow(skip_top_9_like)
        Like.appendRow(order_like)


        Comment = StandardItem("Comment", 16, set_bold = True)
        max_number_of_comments = StandardItem("max_number_of_comments", 14)
        tags_comment = StandardItem("tags", 14)
        delay_comment = StandardItem("delay", 14)
        skip_top_9_comment = StandardItem("delay", 14)
        order_comment = StandardItem("order", 14)

        Comment.appendRow(max_number_of_comments)
        Comment.appendRow(tags_comment)
        Comment.appendRow(delay_comment)
        Comment.appendRow(skip_top_9_comment)
        Comment.appendRow(order_comment)


        Dm = StandardItem("Dm", 16, set_bold=True)
        max_number_of_dms = StandardItem("max_number_of_dms", 14)
        tags_dm = StandardItem("tags", 14)
        delay_dm = StandardItem("delay", 14)
        dm_input = StandardItem("dm_input", 14)
        skip_top_9_dm = StandardItem("delay", 14)
        users_dm = StandardItem("users", 14)

        Dm.appendRow(max_number_of_dms)
        Dm.appendRow(tags_dm)
        Dm.appendRow(delay_dm)
        Dm.appendRow(dm_input)
        Dm.appendRow(skip_top_9_dm)
        Dm.appendRow(users_dm)


        Follow = StandardItem("Follow", 16, set_bold=True)
        accounts_to_follow = StandardItem("accounts_to_follow", 14)
        follow_followers = StandardItem("follow_followers", 14)
        follow_likers = StandardItem("follow_likers", 14)
        post_index = StandardItem("post_index", 14)
        hashtags_follow = StandardItem("hashtags", 14)
        delay_follow = StandardItem("delay", 14)
        skip_top_nine_follow = StandardItem("skip_top_nine", 14)

        Follow.appendRow(accounts_to_follow)
        Follow.appendRow(follow_followers)
        Follow.appendRow(follow_likers)
        Follow.appendRow(post_index)
        Follow.appendRow(hashtags_follow)
        Follow.appendRow(delay_follow)
        Follow.appendRow(skip_top_nine_follow)

        Unfollow = StandardItem("Unfollow", 16, set_bold=True)
        users_unfollow = StandardItem("users_unfollow", 14)
        whitelist = StandardItem("whitelist", 14)
        desired_unfollowing = StandardItem("desired_unfollowing", 14)
        delay_unfollow = StandardItem("delay", 14)

        Unfollow.appendRow(users_unfollow)
        Unfollow.appendRow(whitelist)
        Unfollow.appendRow(desired_unfollowing)
        Unfollow.appendRow(delay_unfollow)

        rootNode.appendRow(Like)
        rootNode.appendRow(Comment)
        rootNode.appendRow(Dm)
        rootNode.appendRow(Follow)
        rootNode.appendRow(Unfollow)

        collapsable.setModel(treeModel)
        collapsable.expandAll()
        collapsable.clicked.connect(self.getValue)


        self.setCentralWidget(collapsable)

    def getValue(self, val):
        print(val.data())
        print(val.row())
        print(val.column())


app = QApplication(sys.argv)

Launch = Expandable()
Launch.show()

sys.exit(app.exec_())
