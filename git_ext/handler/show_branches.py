# coding: utf-8

import re
import subprocess
import json
from git_ext.api_handler import APIHandler, HTTPError


class ShowBranchesHandler(APIHandler):
    def get(self):
        try:
            proc = subprocess.run('git branch'.split(),
                                  stdout=subprocess.PIPE)
            proc.check_returncode()
            out = proc.stdout

            out = out.decode('utf-8')
            branches = re.sub(r'[* ]+', '', out).split('\n')[:-1]
            current_branch = next(filter(lambda x: x.startswith('*'),
                                         out.split('\n')[:-1]))
            current_branch = re.sub(r'[* ]+', '', current_branch)

            self.finish({
                'body': {
                    'branches': branches,
                    'current_branch': current_branch
                }
            })
        except subprocess.CalledProcessError as e:
            raise HTTPError(400)
