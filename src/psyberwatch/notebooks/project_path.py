# Source - https://stackoverflow.com/a
# Posted by Gerges
# Retrieved 2025-12-13, License - CC BY-SA 4.0

import sys
import os

module_path = os.path.abspath(os.path.join(os.pardir, os.pardir))
if module_path not in sys.path:
    sys.path.append(module_path)
