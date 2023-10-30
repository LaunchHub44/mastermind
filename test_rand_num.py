import pytest
import rand_num

def testRandNum():
    trn = rand_num.randomNumber()
    assert trn != 0
    assert len(trn) == 3
    assert rand_num.randomNumber() != rand_num.randomNumber()

def testConvert():
    assert rand_num.convertGuess('a') == None
    assert rand_num.convertGuess('123') == (1,2,3)
    assert rand_num.convertGuess('12') == None
    assert rand_num.convertGuess('1234') == None

def testCheck():
    assert rand_num.checkAnswer((1, 2, 3), (4, 5, 6)) == (0, 0)
    assert rand_num.checkAnswer((1,2,3), (1,2,3)) == (3, 0)
    assert rand_num.checkAnswer((2,1,5), (1,3,5)) == (1, 1)