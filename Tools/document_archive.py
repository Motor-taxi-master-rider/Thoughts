import json
import os
import re

DOCUMENT_PATH = 'Document/Document_to_review.md'


def document_archive():
    regx_url = r'''(?x)\A
                ([a-z][a-z0-9+\-.]*)://　　　　　　　　　　　　　# Scheme
                ([a-z0-9\-._~%]+　　　　　　　　　　　　　　　　　# IPv4 host
                |\[[a-z0-9\-._~%!$&'()*+,;=:]+\])　　　　　　　# IPv6 host
                (:[0-9]+)?　　　　　　　　　　　　　　　　　　　　　# Port number
                ([a-zA-Z0-9\-\/._~%!$&'()*+]+)?　　　　　　　　# path
                (\?[a-zA-Z0-9&=]+)?　　　　　　　　　　　　　　　　# query
                '''
    doc_path = os.path.realpath(os.path.join('../', DOCUMENT_PATH))

    with open(doc_path, encoding='utf=8') as fh:
        docs = fh.read()
    return docs
