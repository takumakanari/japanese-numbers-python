#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from unittest import TestCase
from nose.tools import eq_

from tests import compare_result

from japanese_numbers import to_arabic, to_arabic_numbers
from japanese_numbers.result import ParsedResult as R


class Test_to_arabic(TestCase):

  def test_no_hists(self):
    ret = to_arabic('no japanese numbers text')
    eq_(len(ret), 0)

  def test_single_kanji_word(self):
    ret = to_arabic('一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=1, text='一', index=0))

    ret = to_arabic('十')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=10, text='十', index=0))

    ret = to_arabic('百')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=100, text='百', index=0))

    ret = to_arabic('一を聞いて十を知る。')
    eq_(len(ret), 2)
    compare_result(ret[0], R(number=1, text='一', index=0))
    compare_result(ret[1], R(number=10, text='十', index=5))

  def test_numeric_only(self):
    ret = to_arabic('100000')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=100000, text='100000', index=0))

    ret = to_arabic('1を聞いて10を知る。')
    eq_(len(ret), 2)
    compare_result(ret[0], R(number=1, text='1', index=0))
    compare_result(ret[1], R(number=10, text='10', index=5))

  def test_numeric_with_comma(self):
    ret = to_arabic('10,000円')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=10000, text='10,000', index=0))

    ret = to_arabic('abc, 10,000,000,円, edf, 50,000,')
    eq_(len(ret), 2)
    compare_result(ret[0], R(number=10000000, text='10,000,000', index=5))
    compare_result(ret[1], R(number=50000, text='50,000', index=24))

  def test_kanji_with_comma(self):
    ret = to_arabic('二,三,四')
    eq_(len(ret), 3)
    compare_result(ret[0], R(number=2, text='二', index=0))
    compare_result(ret[1], R(number=3, text='三', index=2))
    compare_result(ret[2], R(number=4, text='四', index=4))

    ret = to_arabic('テスト、二三四,十一')
    eq_(len(ret), 2)
    compare_result(ret[0], R(number=234, text='二三四', index=4))
    compare_result(ret[1], R(number=11, text='十一', index=8))

  def test_kanji_only_10(self):
    ret = to_arabic('十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=11, text='十一', index=0))

    ret = to_arabic('八十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=81, text='八十一', index=0))

  def test_kanji_only_100(self):
    ret = to_arabic('百八十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=181, text='百八十一', index=0))

    ret = to_arabic('二百八十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=281, text='二百八十一', index=0))

  def test_kanji_only_1000(self):
    ret = to_arabic('千百八十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=1181, text='千百八十一', index=0))

    ret = to_arabic('二千百八十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=2181, text='二千百八十一', index=0))

  def test_kanji_only_10000(self):
    ret = to_arabic('一万二千百八十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=12181, text='一万二千百八十一', index=0))

  def test_kanji_only_100000(self):
    ret = to_arabic('十万二千百八十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=102181, text='十万二千百八十一', index=0))

    ret = to_arabic('十一万二千百八十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=112181, text='十一万二千百八十一', index=0))

  def test_kanji_only_1000000(self):
    ret = to_arabic('百十一万二千百八十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=1112181, text='百十一万二千百八十一', index=0))

    ret = to_arabic('五百十一万二千百八十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=5112181, text='五百十一万二千百八十一', index=0))

  def test_kanji_only_10000000(self):
    ret = to_arabic('千五百十一万二千百八十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=15112181, text='千五百十一万二千百八十一', index=0))

    ret = to_arabic('四千五百十一万二千百八十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=45112181, text='四千五百十一万二千百八十一', index=0))

  def test_kanji_only_100000000(self):
    ret = to_arabic('一億千五百十一万二千百八十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=115112181, text='一億千五百十一万二千百八十一', index=0))

  def test_kanji_only_1000000000(self):
    ret = to_arabic('五十億十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=5000000011, text='五十億十一', index=0))

    ret = to_arabic('二十一億千五百十一万二千百八十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=2115112181, text='二十一億千五百十一万二千百八十一', index=0))

  def test_kanji_only_10000000000(self):
    ret = to_arabic('五百億十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=50000000011, text='五百億十一', index=0))

    ret = to_arabic('三百二十一億千五百十一万二千百八十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=32115112181, text='三百二十一億千五百十一万二千百八十一', index=0))

  def test_kanji_only_100000000000(self):
    ret = to_arabic('千億十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=100000000011, text='千億十一', index=0))

    ret = to_arabic('六千三百二十一億千五百十一万二千百八十一')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=632115112181, text='六千三百二十一億千五百十一万二千百八十一', index=0))

  def test_mixed(self):
    ret = to_arabic('1万')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=10000, text='1万', index=0))

    ret = to_arabic('5百万')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=5000000, text='5百万', index=0))

    ret = to_arabic('1億2500万光年')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=125000000, text='1億2500万', index=0))

  def test_numeric_chain(self):
    ret = to_arabic('五〇五号室')
    eq_(len(ret), 1)
    compare_result(ret[0], R(number=505, text='五〇五', index=0))

  def test_parsing_text(self):
    ret = to_arabic('その形は3-50個ほどの銀河が集まった銀河群と呼ばれる小規模な集団に始まり、フラクタル状の階層的段階の集団を構成する。200万光年程度の狭い領域に纏まった銀河群はコンパクト銀河群と呼ばれる')
    eq_(len(ret), 3)
    compare_result(ret[0], R(number=3, text='3', index=4))
    compare_result(ret[1], R(number=50, text='50', index=6))
    compare_result(ret[2], R(number=2000000, text='200万', index=59))


class Test_to_arabic_numbers(TestCase):

  def test_parse_multiple_numbers(self):
    ret = to_arabic_numbers('一を聞いて十を知る。')
    eq_(len(ret), 2)
    eq_(ret[0], 1)
    eq_(ret[1], 10)
