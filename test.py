from collections import Counter
import json


SAMPLE_FILE=''
THRESHOLD=7
OUTPUT_FILE=''
FILE_NAME='profile_matching_WeboAdobe-20170219.json'

french_stats = Counter()

def weboramaParser(cookie):
    cookie['id'] = cookie['id_adobe'].replace('\\n', '')
    del cookie['id_adobe']

def getStat(sample):


class Cookie(dict):
    
    def __init__(self, cookie, parser=None):

        if parser is not None:
            parser(cookie)

        assert 'id' in cookie

        for k, v in cookie.items():
            setattr(self, k, v)
        
        self.version = set((self.last_update, ))

    @property
    def nb_versions(self):
        return len(self.versions)

    @staticmethod
    def getLast(self, other):
        last = self if self.last_update > other.last_update else other
        last.versions = set.union(self.version, other.version)
        return last


class CookieSample(dict):

    def __init__(self, filename, cookie_parser=None):
        with open(filename) as f:
            for line in f:
                cookie = Cookie(json.loads(line), cookie_parser)
                self._addCookie(cookie)
                
    def _addCookie(self, cookie):
        id_ = cookie.id
        if id_ in self:
            current_version = self[id_]
            last_version = Cookie.getLast(self[id_], cookie)
            self[id_] = last_version
        else:
            self[id_] = cookie

sample = CookieSample(FILE_NAME, cookie_parser=weboramaParser)

# check:
# c = (Sm/SM) * 7 / Si
# Sm: score moyen usr
# SM: score moyen tout usr
# Si: Surf intensity

def get_usr(line):
    d = literal_eval(line)
    d = {k:d[k] for k in keys}
    usr = setup_categories(d)

#with open(SAMPLE_FILE) as f:
#    cookies = CookieSample(filename=FILE_NAME)
#    for line in f:
#        cookie = literal_eval(line)
#        categories, surf_intensity = parse(cookie)
#        stats.update(categories)

