# -*- coding: utf-8 -*-
#Copyright (c) 2009,10 Walter Bender

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

from constants import SWIDTH, SHEIGHT, OFFSET, SCALE, HTOP1, HTOP2, HTOP3
from C import header, footer, slide1, slide2, slide3, slide_offset1, \
    slide_offset2, slide_offset3
import math


def mark(offset, height3, height2, height1, string=None, flip=False,
         scale=1.0):
    """ Plot marks in a range from 1 to 10 along the length of the slide """
    svg = ''
    scale *= float(SWIDTH - 2 * OFFSET) / SCALE
    if flip:
        ln = float((log10 - offset) * SCALE + OFFSET)
    else:
        ln = offset * SCALE * scale + OFFSET
    if string is not None:
        svg += '  <text style="font-size:12px;fill:#000000;">\n'
        svg += '      <tspan\n'
        svg += '       x="%0.2f"\n' % (ln)
        svg += '       y="%d"\n' % (height3)
        svg += '       style="font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans;">%0.4f</tspan></text>\n' % (string)
    svg += '  <path\n'
    svg += '       d="M %0.2f,%d,%0.2f,%d"\n' % (ln, height1, ln, height2)
    svg += '       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:square;stroke-linejoin:miter;stroke-opacity:1" />\n'
    print svg


def make_slide(label, offset_function, label_function, x=None):
    """ Generate marks along a slide using passed functions """

    if x is None:
        header(label)
    else:
        header(label, x)

    for i in range(100, 200):
        if int((i / 10) * 10) == i:
            mark(offset_function(i / 100.), slide3, slide2, slide1,
                 label_function(i / 100.))
        elif int((i / 5) * 5) == i:
            mark(offset_function(i / 100.), slide3, slide2,
                 slide1 + slide_offset1)
        else:
            mark(offset_function(i / 100.), slide3, slide2,
                 slide1 + slide_offset2)

    for i in range(200, 400, 2):
        if int((i / 20) * 20) == i:
            mark(offset_function(i / 100.), slide3, slide2, slide1,
                 label_function(i / 100.))
        elif int((i / 10) * 10) == i:
            mark(offset_function(i / 100.), slide3, slide2, slide1)
        else:
            mark(math.log(i/100., 10), slide3, slide2, slide1 + slide_offset1)

    for i in range(400, 1005, 5):
        if int((i / 50) * 50) == i:
            mark(offset_function(i / 100.), slide3, slide2, slide1,
                 label_function(i / 100.))
        elif int((i / 10) * 10) == i:
            mark(offset_function(i / 100.), slide3, slide2, slide1)
        else:
            mark(offset_function(i / 100.), slide3, slide2,
                 slide1 + slide_offset1)

    footer()


def main():
    """ Log Log scale for slide (top scale) """

    def offset_function(x):
        return math.log(x, 10)

    def label_function(x):
        return math.exp(x / 1000.)

    make_slide('LL0', offset_function, label_function, x=10)
    return 0


if __name__ == "__main__":
    main()