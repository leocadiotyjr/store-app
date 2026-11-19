#!/usr/bin/env python3
"""Inline ../grm-showroom-scene.json into template.html.
Writes index.html (standalone page, opens from file://) and, with --fragment PATH,
a head-less copy for publishing as an Artifact."""
import json, sys, pathlib
here = pathlib.Path(__file__).parent
scene = json.dumps(json.load(open(here / '../grm-showroom-scene.json')), ensure_ascii=False).replace('</', '<\\/')
frag = (here / 'template.html').read_text().replace('__SCENE__', scene)
page = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>' + frag + '</body></html>')
(here / 'index.html').write_text(page)
if '--fragment' in sys.argv:
    pathlib.Path(sys.argv[sys.argv.index('--fragment') + 1]).write_text(frag)
print('built', len(page) // 1024, 'KB')
