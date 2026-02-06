# Lua.obfuse

- Lua 프로젝트를 단일 압축/ 번들된 파일 ( `*.o.lua` )로 만들어 주는 도구입니다. 내부적으로 각각의 Lua 파일을 모듈 레지스트리에 등록하고 압축하고 인코딩해서 런타임에서 해제/실행할 수 있게 만듭니다. 

# 주요 기능

- target/target.lua에서 .lua 파일을 수집
- require('a.b') 호출을 런타임 __require('a.b')로 치환
- 각 파일을 특정한 형태로 등록
- 실행 템플릿을 포함한 단일 파일 생성

# 빠른 시작

- Python을 필요로 하며, 3.10+ 버전을 권장합니다.
- Lua 프로젝트를 targer/에 둡니다. entry arg로 다른 경로로 지정 가능합니다.
- bundle을 다음과 같이 실행합니다.
```python
python src/main.py --entry target/target.lua --output target/target.o.lua
```
- 생성된 bundle을 루아로 실행합니다.

# 주의사항

- 기본적으로 entry 파일이 번들 루트 내부에 있어야 한다고 가정합니다. 다른 위치의 파일을 번들링 하려면 Packager 생성 시에 루트를 변경하거나 --entry에 적절한 값을 주셔야합니다.
- 생성된 .o.lua는 패키저의 런타임 로더에만 의존합니다.