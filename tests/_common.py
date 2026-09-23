# Copyright (c) 2018-2019 Robin Jarry
# SPDX-License-Identifier: MIT

import os

from _libyang import lib
from libyang.util import c2str


YANG_DIR = os.path.join(os.path.dirname(__file__), "yang")
CORE_MODULE_DIR = c2str(lib.ly_yang_module_dir())
SEARCH_DIRS = ":".join([YANG_DIR, CORE_MODULE_DIR])
