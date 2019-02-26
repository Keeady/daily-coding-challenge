from Matrix import zigzag_letter


def test_zigzag():
    assert 'PAHNAPLSIIGYIR' == zigzag_letter.zigzag('PAYPALISHIRING', 3)
    assert 'PINALSIGYAHRPI' == zigzag_letter.zigzag('PAYPALISHIRING', 4)