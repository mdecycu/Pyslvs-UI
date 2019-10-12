# -*- coding: utf-8 -*-

"""'slvs' module contains IO support functions of Solvespace format."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2019"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from .read import SlvsParser2
from .frame import slvs2_frame
from .part import slvs2_part, boundary_loop

__all__ = [
    'SlvsParser2',
    'slvs2_frame',
    'slvs2_part',
    'boundary_loop',
]
