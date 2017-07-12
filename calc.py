#!/usr/bin/env python
"""The main calculator command-line interface"""

from __future__ import print_function

BANNER = """
                           _     A Simple
                          /  _.| _   | _._|_ _ ._
                          \_(_||(_|_||(_| |_(_)|

                       
"""

import os
import sys

from functools import partial
stderr = partial(print, file=sys.stderr)

import calclib

def main():
    stderr(BANNER)
    try:
        while True:
            try:
                expr = raw_input('calc> ').strip()
                if expr:
                    expr = calclib.tokenize(expr)
                    expr = calclib.implicit_multiplication(expr)
                    expr = calclib.to_rpn(expr)
                    res = calclib.eval_rpn(expr)
                    print('%g' % res)
            except ValueError, ex:
                stderr('error:', ex)
    except EOFError:
        stderr('\ncaught EOF')
    except KeyboardInterrupt:
        stderr('\ninterrupted')

if __name__ == '__main__':
    main()
