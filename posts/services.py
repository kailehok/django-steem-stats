# posts/services.py

from beem.blockchain import Blockchain
from beem.account import Account
from beem.comment import Comment
from beem import Steem
from beem.nodelist import NodeList
nodelist = NodeList()


# retrieve account blog history
def account_history(username):
    stm = Steem(node=nodelist .get_nodes())
    account = Account(username, steem_instance=stm)

    return account.blog_history(limit=25, reblogs=False)