# -*- coding: utf-8 -*-
"""
Пример 5.4
Программа для демонстрации, используется в Примере 5.3
"""

import os
import sys

if len(sys.argv) > 1:
    print('Hello from child', os.getpid(), sys.argv[1])
else:
    print('Not argument')
