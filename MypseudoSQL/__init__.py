import sys

major = sys.version_info.major

if major == 2:
    from .pseudoSQL import Table

elif major == 3:
    from .pseudoSQL3 import Table
