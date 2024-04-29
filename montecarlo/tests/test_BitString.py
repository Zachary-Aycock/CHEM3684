"""
Test all functions in BitString.py
"""

import numpy as np
import math    
import montecarlo 


def test_BitString():
    bs = montecarlo.BitString(8) # initialize bitstring as object, most assertions test str()

    #verify length and proper intialization
    assert(len(bs) == 8)
    assert(str(bs) == "00000000")

    # verify flip_site, on, and off
    bs.flip_site(1)
    bs.flip_site(5)
    assert(bs.on() == 2)
    assert(bs.off() == 6)
    assert(str(bs) == "01000100")
    
    # verify set_config, set_int_config, and int
    bs.set_config([0,0,0,1,0,0,0,1])
    assert(str(bs) == "00010001")
    bs.set_int_config(4)
    assert(bs.int() == 4)

    # verify eq
    bs1 = montecarlo.BitString(4)
    bs2 = montecarlo.BitString(4)
    assert(bs1 == bs2)