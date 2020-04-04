#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from past.builtins import xrange

from japanese_numbers.kind import (  # noqa
  UNIT_KIND,
  NUMBERS_KIND,
  MULTIPLES_KIND,
  NUMERIC_KIND
)


UNITS = {  # noqa
  '十': 10,
  '百': 100,
  '千': 1000
}

MULTIPLES = {  # noqa
  '万': 10000,
  '億': 100000000,
  '兆': 1000000000000
}

NUMBERS = {  # noqa
  x[1]: x[0] + 1
  for x in enumerate(('一', '二', '三', '四', '五', '六', '七', '八', '九', '十'))
}

NUMERICS = list(map(str, xrange(0, 10)))

KANJI_NUMBER_MAP = {  # noqa
  x[1]: x[0]
  for x in enumerate(('〇', '一', '二', '三', '四', '五', '六', '七', '八', '九'))
}

MULTIBYTE_NUMBER_MAP = {  # noqa
  x[1]: x[0]
  for x in enumerate(('０', '１', '２', '３', '４', '５', '６', '７', '８', '９'))
}


class Tokenized(object):

  def __init__(self, val):
    self.origin = val
    self.val = self._convert_kanji_to_arabic(val)
    self._size = len(self.val)
    self.kind = None
    self.num_of_kind = None
    self.char = None
    self.pos = -1
    self.last_kind = None

  def next(self, incr=1):
    self.pos += incr
    if self.has_next():
      self.char = self.val[self.pos]
      self.last_kind = self.kind
      self.kind, self.num_of_kind = self._kind_of(self.char)

  def has_next(self):
    return self.pos <= self._size - 1

  @property
  def origin_char(self):
    return self.origin[self.pos]

  def origin_char_at(self, pos):
    return self.origin[pos]

  @classmethod
  def _kind_of(cls, c):
    if c in UNITS:
      return UNIT_KIND, UNITS[c]
    elif c in NUMBERS:
      return NUMBERS_KIND, NUMBERS[c]
    elif c in MULTIPLES:
      return MULTIPLES_KIND, MULTIPLES[c]
    elif c in NUMERICS:
      return NUMERIC_KIND, None
    return None, None

  @classmethod
  def _convert_kanji_to_arabic(cls, val):
    val_ = val
    for src, dest in KANJI_NUMBER_MAP.items():
      val_ = val_.replace(src, str(dest))
    for src, dest in MULTIBYTE_NUMBER_MAP.items():
      val_ = val_.replace(src, str(dest))
    return val_

