# coding: utf-8

from git_ext.handler.show_branches import ShowBranchesHandler
from git_ext.handler.checkout import CheckoutHandler
from git_ext.handler.commit import CommitHandler

route = {
    '/git_ext/api/branch': ShowBranchesHandler,
    '/git_ext/api/checkout': CheckoutHandler,
    '/git_ext/api/commit': CommitHandler
}
