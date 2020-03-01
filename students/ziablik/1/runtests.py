# -*- coding: utf-8 -*-

import os           # noqa: I001
import re           # noqa: I001
import subprocess   # noqa: S404,I001

tpl = 'test_(.)*.py'

for directory in os.walk('.', topdown=False):
    if '.idea' not in directory[0] and directory[2]:
        for file_name in directory[2]:
            if re.match(tpl, file_name) is not None:
                print(  # noqa: T001
                    '{0}/{1}'.format(directory[0], file_name),
                    end=' ... ',
                    flush=True,
                )
                subprocess.check_call('python {0}/{1}'.format(directory[0], file_name))    # noqa: S603,E501
