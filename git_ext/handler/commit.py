# coding: utf-8

import subprocess
import json
import os.path
from notebook.base.handlers import IPythonHandler


class CommitHandler(IPythonHandler):
    def post(self):
        body = json.loads(self.request.body)
        try:
            cmd = ['git add {}'.format(filename)
                   if os.path.exists(filename)
                   else 'git rm {}'.format(filename)
                   for filename in body['files']]
            cmd += ['git commit -m "{}"'.format(body['commit_message'])]
            cmd = '; '.join(cmd)
            out = subprocess.run(cmd,
                                 stdout=subprocess.PIPE,
                                 shell=True, check=True).stdout

            self.finish({
                'body': {
                    'done_commit': True
                }
            })
        except subprocess.CalledProcessError as e:
            raise HTTPError(400)
