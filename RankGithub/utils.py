import requests, json
import re

class GithubClient(object):

    def __init__(self, url, gh_user, gh_pw):
        match_obj = re.match(".*\.com\/(.*)\/(.*)", url)
        user = match_obj.group(1)
        repo = match_obj.group(2)

        self.user = gh_user
        self.pw = gh_pw

        self.url = "https://api.github.com/repos/%s/%s"%(user, repo)

    def fetch(self):
        r = requests.get(self.url, auth=(self.user, self.pw))

        results = json.loads(r.text)
        
        return results