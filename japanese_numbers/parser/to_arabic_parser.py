#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from japanese_numbers.result import ParsedResult
from japanese_numbers.token import Tokenized, NUMERICS
from japanese_numbers.kind import (  # noqa
  UNIT_KIND,
  NUMBERS_KIND,
  MULTIPLES_KIND,
  NUMERIC_KIND
)


def _collect_numerics(token):
  stack, pos_size, values = ([], 0, token.val[token.pos:])
  size = len(values)
  for i, c in enumerate(values):
    if c not in NUMERICS:
      comma = c == ','
      nc_org = token.origin_char_at(token.pos + i + 1) \
        if i + 1 < size else None
      if not comma or nc_org not in NUMERICS:
        break
    else:
      stack.append(c)
    pos_size += 1
  return int(''.join(stack)), pos_size


def to_arabic(val, encode='utf8'):
  stacks, numbers, texts, analyzing, index = ([], [], [], False, -1)
  results = []

  def _append_result():
    results.append(ParsedResult(text=''.join(texts),
                                number=sum(stacks) + sum(numbers),
                                index=index))

  decoded_val = val if isinstance(val, unicode) else val.decode(encode)
  token = Tokenized(decoded_val)

  while token.has_next():
    kind, num = (token.kind, token.num_of_kind)

    if kind == UNIT_KIND and token.last_kind != UNIT_KIND:
      ret = (numbers[-1] if numbers else 1) * num
      if numbers:
        numbers[-1] = ret
      else:
        numbers.append(ret)

    elif kind in (NUMBERS_KIND, UNIT_KIND):
      numbers.append(num)

    elif kind == MULTIPLES_KIND:
      stacks.append(sum(numbers) * num)
      numbers = []

    elif kind == NUMERIC_KIND:
      n, s = _collect_numerics(token)
      numbers.append(n)
      index = token.pos if index < 0 else index
      texts.append(''.join(token.origin_char_at(x)
                   for x in xrange(token.pos, token.pos + s)))
      token.next(incr=s)

    elif analyzing:
      _append_result()
      stacks, numbers, texts, analyzing, index = ([], [], [], False, -1)

    analyzing = kind is not None

    if analyzing:
      if kind != NUMERIC_KIND:
        texts.append(token.origin_char)
      if index < 0 and token.last_kind is None:  # 1st time:
        index = token.pos

    if kind != NUMERIC_KIND:
      token.next()

  if stacks or numbers:
    _append_result()

  return results


def to_arabic_numbers(val, encode='utf8'):
  return tuple(x.number for x in to_arabic(val, encode=encode))

