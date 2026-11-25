#! /usr/bin/env python3

import sys

from bdpacakge.bdmodule import return_birthday



firstname = sys.argv[1]
lastname = sys.argv[2]

full_name = firstname + ' ' + lastname

return_birthday(full_name)
