import json
import os
import re

DOCUMENT_PATH = 'Document/Document_to_review.md'


def document_archive():
    reg = r'(?P<title>[^\n]+)\n+<(?P<url>https?://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|])>'
    pattern = re.compile(reg)
    doc_path = os.path.realpath(os.path.join('../', DOCUMENT_PATH))

    with open(doc_path, encoding='utf=8') as fh:
        docs = fh.read()
    for title, url in pattern.findall(docs):
        data = _parse_title(title)
        data['url'] = url
    return docs


def _parse_title(title: str) -> dict:
    data = {}
    if title.startswith('#'):
        data['category'] = 'TODO'
        if title.startswith('##'):
            data['priority'] = 2
        else:
            data['priority'] = 3
    elif title.startswith('`'):
        pass
    elif title.startswith('**'):
        pass
    elif title.startswith('_'):
        pass
    elif title.startswith('~~'):
        pass
    else:
        data['category'] = 'TODO'
        data['priority'] = 1
    return data
