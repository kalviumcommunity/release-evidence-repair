import json,sys
from pathlib import Path
mode=sys.argv[1] if len(sys.argv)>1 else 'all'
try:
    if mode in ('version','all'):
        r=json.loads(Path('release.json').read_text())
        assert r=={'version':'v1.4.3','image':'parcelboard:v1.4.3','change_type':'PATCH'}, 'expected compatible next PATCH and matching image'
        print('VERSION PASS: static metadata only; not image provenance or deployment proof.')
    elif mode in ('notes','recovery'):
        print(Path('release-notes.md' if mode=='notes' else 'recovery-review.md').read_text())
        print('REPORT READY: prose requires human grading, not automated PASS.')
    else: raise AssertionError('unknown command')
except (AssertionError,KeyError) as e:
    print('CHECK FAIL:',e);sys.exit(1)
