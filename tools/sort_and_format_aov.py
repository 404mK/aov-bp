import json
from pathlib import Path

base = Path(__file__).resolve().parents[1]
src = base / 'aov_heroes.json'
out_formatted = base / 'formatted_aov_heroes.json'

def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write_single_line(path, data):
    lines = [json.dumps(obj, ensure_ascii=False) for obj in data]
    path.write_text('[\n' + ',\n'.join('  '+ln for ln in lines) + '\n]', encoding='utf-8')


data = load(src)
# sort by name, case-insensitive
sorted_data = sorted(data, key=lambda o: o.get('name','').casefold())
write_single_line(src, sorted_data)
write_single_line(out_formatted, sorted_data)
print('wrote', src)
print('wrote', out_formatted)
