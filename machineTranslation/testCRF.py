import numpy as np
from crf import *
from arsenal.nlp.annotation import fromSGML, extract_contiguous
from arsenal.iterextras import partition, iterview
from arsenal.alphabet import Alphabet
from numpy import fromiter, int32
import re

def path_features(x, y):
    """
    Features of the assignment ``y`` to instance ``x``.
    Note: ``y`` should be a sequence of ``int``.
    """
    F = x.feature_table
    f = list(F[0, None, y[0]])
    f.extend(k for t in xrange(1, x.Length) for k in F[t, y[t-1], y[t]])
    return f

def preprocess(data, feature_alphabet, label_alphabet):
    """
    preprocessing hook which caches the ``feature_table`` and ``target_features``
    attributes of a Instance.
    """
    A = feature_alphabet
    L = label_alphabet

    for x in data:
        # cache feature_table
        if x.feature_table is None:
            x.feature_table = FeatureVectorSequence(x, A, L)
            # cache target_features
        if x.target_features is None:
            x.target_features = path_features(x, list(L.map(x.truth)))


class FeatureVectorSequence(object):
    def __init__(self, instance, A, L):
        self.sequence = [fromiter(A.map(t.attributes), dtype=int32) for t in instance.sequence]
        self.A = len(A)
        self.L = len(L)
    def __getitem__(self, item):
        (t,yp,y) = item
        token = self.sequence[t]
        if yp is not None:
            # todo: this is not perfect because the integer for `yp` was not assignment by the alphabet
            return np.append(token, yp) + y*self.A
        else:
            return token + y*self.A

def build_domain(data):
    """
    Do feature extraction to determine the set of *supported* featues, i.e.
    those active in the ground truth configuration and active labels. This
    function will each features and label an integer.
    """
    L = Alphabet()
    A = Alphabet()
    for x in data:
        L.add_many(x.truth)
        A.add_many(f for token in x.sequence for f in token.attributes)
    # domains are now ready
    L.freeze()
    A.stop_growth()
    return (L, A)

class Token(object):
    def __init__(self, form):
        self.form = form
        self.attributes = []
    def add(self, features):
        """ Add features to this Token. """
        self.attributes.extend(features)

def token_features(tk):
    """ very basic feature extraction. """
    w = tk.form
    yield 'word=' + w
    yield 'simplified=' + re.sub('[0-9]', '0', re.sub('[^a-zA-Z0-9()\.\,]', '', w.lower()))
    for c in re.findall('[^a-zA-Z0-9]', w):  # non-alpha-numeric
        yield 'contains(%r)' % c

def preprocessing(s):
    s[0].add(['first-token'])
    s[-1].add(['last-token'])
    for tk in s:
        tk.add(token_features(tk))
    if 1:
        # previous token features
        for t in xrange(1, len(s)):
            s[t].add(f + '@-1' for f in token_features(s[t-1]))
            # next token features
        for t in xrange(len(s) - 1):
            s[t].add(f + '@+1' for f in token_features(s[t+1]))
    return s

def get_data(f):
    for x in fromSGML(f, linegrouper="<NEW.*?>", bioencoding=False):
        x, y = zip(*[(Token(w), y) for y, w in x])
        preprocessing(x)
        yield Sample(x, truth=y)

proportion = [0.3, 0.7]
[train, test] = partition(get_data('/home/laboratory/github/crf/data/tagged_references.txt'), proportion)
(L, A) = build_domain(train)
preprocess(train, A, L)

crf = CRF(1, 1, 1, 1)
crf.SGA(train, iterations=20, a0=19, validate=None)
