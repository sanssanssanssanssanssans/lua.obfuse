import sys
from pathlib import Path
import argparse

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0, str(HERE))

def parse_args():
    p = argparse.ArgumentParser(description="Lua submit packager")
    p.add_argument("--entry", "-e", default = "target/target.lua", help = "제출화할 파일을 넣어주세요. default는 target/main.lua입니다.")
    p.add_argument("--output", "-o", default = "target/target.o.lua", help = "제출화 된 코드를 넣을 파일을 넣어주세요. default는 target/main.o.lua 입니다.")
    return p.parse_args()

def main():
    args = parse_args()
    from core.packager import Packager
    pack = Packager()
    out_path, payload_bytes = pack.build(entry = args.entry, output = args.output)
    print(f"{out_path}이 생성되었어요. ({len(payload_bytes)} 바이트)")
if __name__ == '__main__':
    main()