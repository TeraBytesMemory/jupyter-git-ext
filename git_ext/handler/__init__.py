# coding: utf-8
from notebook.utils import url_path_join
from git_ext.handler.route import route


def add_git_ext_handelr(web_app):
    host_pattern = '.*$'
    route_pattern = [(url_path_join(web_app.settings['base_url'], k), v)
                     for k, v in route.items()]
    web_app.add_handlers(host_pattern, route_pattern)
