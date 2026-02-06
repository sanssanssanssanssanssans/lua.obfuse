# require('core.foo')는 runtime에서 __require('core.foo')가 되게 만들기
from pathlib import Path
import re
from typing import Dict,Tuple
from core.compressor import LZSS
from core.template import template
from utils.regex import REQUIRE_RE
from utils.fs import readtext, collect_lua_files
from utils.misc import b64encode_bytes

class Packager:
    def __init__(self, root: str = "target"):
        self.srcroot = Path(root).resolve()
        self.compressor = LZSS()
    
    def _module_name_from_path(self, p: Path) -> str:
        p = p.resolve()
        rel = p.relative_to(self.srcroot.parent).with_suffix('')
        return '.'.join(rel.parts)

    def collect_modules(self) -> Dict[str, str]:
        modules : Dict[str,str] = {}
        for f in sorted(collect_lua_files(self.srcroot)):
            name = self._module_name_from_path(f)
            src = readtext(f)
            src = re.sub(r'--\\[.*?\\]','',src,flags=re.S)
            src = REQUIRE_RE.sub(lambda m : "__require('"+m.group(1)+"')",src)
            modules[name] = src
        return modules

    def build_regit(self, entry : str) -> str:
        modules = self.collect_modules()
        parts = []
        parts.append("-- LuaSubmitPackager에 의해 생성됨.")
        parts.append("local __MODULES = {}")
        parts.append("local __CACHE = {}")
        parts.append("""local function __require(name)
  if __CACHE[name] then return __CACHE[name] end
  local f = __MODULES[name]
  if not f then error('모듈이 발견되지 않았어요.: '..tostring(name)) end
  local res = f()
  __CACHE[name] = res
  return res
end""")
        
        for name,src in modules.items():
            func = "function()\n" + src + "\nend"
            parts.append(f"__MODULES['{name}'] = {func}")
        
        entry_path = Path(entry).resolve()
        entry_name = self._module_name_from_path(entry_path)
        parts.append(f"-- 실행 엔트리 : {entry_name}\n__require('{entry_name}')")
        merged = "\n\n".join(parts) + "\n"
        return merged

    def build(self, entry: str = 'tests/main.lua', output : str = 'tests/main.o.lua') -> Tuple[str, bytes]:
        entry = str(entry)
        lua = self.build_regit(entry)
        payload = lua.encode('utf-8')
        comp = self.compressor.compress(payload)
        b64 = b64encode_bytes(comp)
        final = template.replace("%s", b64)
        out_path = Path(output)
        out_path.write_text(final, encoding='utf-8')
        return str(out_path), comp