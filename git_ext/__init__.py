# coding: utf-8
from git_ext.handler import add_git_ext_handelr

def _jupyter_server_extension_paths():
    return [{
        "module": "git_ext"
    }]

def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        src="static",
        dest="git_ext",
        require="git_ext/index"
    )]

def load_jupyter_server_extension(nbapp):
    add_git_ext_handelr(nbapp.web_app)
