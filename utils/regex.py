import re
REQUIRE_RE = re.compile(r"require\s*\(?['\"]([^'\"]+)['\"]\)?")
LOCAL_ASSIGN_RE = re.compile(r"\s*local\s+(\w+)\s*=")