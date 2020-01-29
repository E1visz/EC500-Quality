from ABtoRO import intToRoman

def test_one():
    assert intToRoman(1) == "I"
    assert intToRoman(2) == "II"
    assert intToRoman(3) == "III"
    assert intToRoman(50) == "L"
    assert intToRoman(125) == "CXXV"
    assert intToRoman(399) == "CCCXCIX"
    assert intToRoman(678) == "DCLXXVIII"
    assert intToRoman(1997) == "MCMXCVII"
    assert intToRoman(2020) == "MMXX"

def test_two():
    assert intToRoman(-1) == 0
    assert intToRoman(-2) == 0
    assert intToRoman(-3) == 0
    assert intToRoman(-50) == 0
    assert intToRoman(4000) == 0
    assert intToRoman(234422) == 0
    assert intToRoman(445223) == 2
