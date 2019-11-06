# posts/services.py

from beem.blockchain import Blockchain
from beem.account import Account
from beem.comment import Comment
from beem import Steem


# retrieve account blog history
def account_history(username):
    stm = Steem("https://steemd.minnowsupportproject.org")
    account = Account(username, steem_instance=stm)

    return account.blog_history(limit=25, reblogs=False)