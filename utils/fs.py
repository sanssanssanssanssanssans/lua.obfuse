from pathlib import Path
from typing import Iterable

def collect_lua_files(root: Path) -> Iterable[Path]:
    root = Path(root)
    if not root.exists(): return []
    return [p for p in root.rglob('*.lua') if p.is_file()]

def readtext(path : Path) -> str:
    return Path(path).read_text(encoding='utf-8')

def ensuredir(path : Path):
    Path(path).mkdir(parents = True, exist_ok = True)