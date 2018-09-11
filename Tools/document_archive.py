import datetime
import os
import re

from os.path import dirname, join, realpath

DOCUMENT_PATH = join(dirname(realpath(__file__)), '../', 'Document', 'Document_to_review.md')
STERM_REG = re.compile(r'^#+')
LTERM_REG = re.compile(r'^`([^`]+)`')
INTERST_REG = re.compile(r'\*\*([^\*]+)\*\*')
REVIEW_REG = re.compile(r'^_([^_]+)_')
FLIP_REG = re.compile(r'^~~([^~]+)~~')


def document_archive():
    reg = r'(?P<title>[^\n]+)\n+<(?P<url>https?://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|])>'
    pattern = re.compile(reg)

    with open(DOCUMENT_PATH, encoding='utf=8') as fh:
        docs = fh.read()
    result = []
    for title, url in pattern.findall(docs):
        data = _parse_title(title.strip())
        data['url'] = url
        result.append(data)
    return result


def _parse_title(title: str) -> dict:
    data = {'priority': 0}
    if title.startswith('#'):
        data['category'] = 'short_term'
        data['tags'] = ['to do']
        if title.startswith('##'):
            data['priority'] = 2
        else:
            data['priority'] = 3
        data['theme'] = STERM_REG.sub('', title).strip()
    elif title.startswith('`'):
        data['category'] = 'long_term'
        data['theme'] = LTERM_REG.findall(title)[0].strip()
    elif title.startswith('**'):
        data['category'] = 'short_term'
        high_light = INTERST_REG.findall(title)
        data['theme'] = high_light.pop(0).strip()
        data['tags'] = ['reviewed', 'impressive', 'cache']
        if high_light:
            data['comment'] = high_light
    elif title.startswith('_'):
        data['category'] = 'short_term'
        data['theme'] = REVIEW_REG.findall(title)[0].strip()
        high_light = INTERST_REG.findall(title)
        data['tags'] = ['reviewed', 'cache']
        if high_light:
            data['comment'] = high_light
    elif title.startswith('~~'):
        data['category'] = 'flip'
        data['theme'] = FLIP_REG.findall(title)[0].strip()
    else:
        data['category'] = 'short_term'
        data['priority'] = 0
        data['theme'] = title.strip()
    data['update_at'] = datetime.datetime.utcnow()
    return data
