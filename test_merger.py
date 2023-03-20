# -*- coding: utf-8 -*-

import merger


def test_merge_tuples():
    
    #test pro vyslednou funkci merge tuples
    
    line_a = ((1, 3), (3, 4), (10, 2))
    line_b = ((1, 2), (2, 4), (5, 2))
    line_c = ((1, 5), (3, 2), (7, 3))

    expected_result = {1: [3, 2, 5],
                       2: [0, 4, 0],
                       3: [4, 0, 2],
                       5: [0, 2, 0],
                       7: [0, 0, 3],
                       10: [2, 0, 0]}

    result = merger.merge_tuples(line_a, line_b, line_c)                    
    assert type(expected_result) == type(result)
    assert expected_result == result
    

def test_merge_tuples_dif_len():
    
    #test pro vyslednou funkci merge tuples
    
    line_a = ((1, 3), (3, 4), (10, 2))
    line_b = ((1, 2), (2, 4), (5, 2), (15, 2), (25, 2))
    line_c = ((1, 5), (3, 2), (7, 3))

    expected_result = {1: [3, 2, 5],
                       2: [0, 4, 0],
                       3: [4, 0, 2],
                       5: [0, 2, 0],
                       7: [0, 0, 3],
                       10: [2, 0, 0],
                       15: [0, 2, 0],
                       25: [0, 2, 0]}

    assert expected_result == merger.merge_tuples(line_a, line_b, line_c)

