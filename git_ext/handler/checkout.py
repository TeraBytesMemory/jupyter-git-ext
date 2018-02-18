# coding: utf-8

import subprocess
import json
from git_ext.api_handler import APIHandler, HTTPError


class CheckoutHandler(APIHandler):
    def post(self):
        body = json.loads(self.request.body)

        try:
            cmd = 'git checkout -b {}'.format(body['branch']) \
                if body['new_branch'] \
                else 'git checkout {}'.format(body['branch'])
            out = subprocess.run(cmd.split(),
                                 stdout=subprocess.PIPE,
                                 check=True).stdout
            out = out.decode('utf-8')

            self.finish({
                'body': {
                    'do_checkout': True,
                    'output': out
                }
            })
        except subprocess.CalledProcessError as e:
            raise HTTPError(400)
