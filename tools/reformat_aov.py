import json
from pathlib import Path
p = Path(__file__).resolve().parents[1] / 'aov_heroes.json'
out = Path(__file__).resolve().parents[1] / 'formatted_aov_heroes.json'
with p.open('r', encoding='utf-8') as f:
    data = json.load(f)
lines = [json.dumps(obj, ensure_ascii=False) for obj in data]
with out.open('w', encoding='utf-8') as f:
    f.write('[\n' + ',\n'.join('  '+ln for ln in lines) + '\n]')
print('wrote', out)
