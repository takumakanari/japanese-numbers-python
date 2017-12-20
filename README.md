# japanese_numbers

A parser for Japanese number (Kanji, arabic) in the natural language.

The module **japanese_numbers** finds any numbers in the natural language, and converts to arabic numerals.
The followings are example patterns what can be parsed.

- 二千万百一円
- 5百万
- 一を聞いて十を知る
- 五〇六号室


### Installation

Currently, you can install from PYPI by using pip:

    pip install japanses-numbers-python

Or installing github directly:

    pip install git+git://github.com/takumakanari/japanses-numbers-python.git


## Usage

Function `to_arabic` and `to_arabic_numbers` are almost stable.

`to_arabic` returns An array of *[japanese_numbers.result.ParsedResult]*.

```python
import japanese_numbers

japanese_numbers.to_arabic('銀河の向こう、六千三百二十一億千五百十一万二千百八十一光年彼方。')
# => [<ParsedResult 632115112181 : "六千三百二十一億千五百十一万二千百八十一" index=7>]

japanese_numbers.to_arabic('一を聞いて十を知る。')
# => [<ParsedResult 1 : "一" index=0>, <ParsedResult 10 : "十" index=5>]

```


Then you can see a numeric value (and others) in the instance of *ParsedResult* like as follows:

```python
result = japanese_numbers.to_arabic('一を聞いて十を知る。')

result[0].number # => 1
result[0].text   # => '一'
result[0].index  # => 0 as position that number was found

result[1].number # => 10
result[1].text   # => '十'
result[1].index  # => 5

```

`to_arabic_numbers` returns a tuple of numbers directly.

```python
import japanese_numbers

japanese_numbers.to_arabic_numbers('一を聞いて十を知る。')
# => (1, 10)
```

### Charsets

Both `to_arabic_numbers`, `to_arabic` get `encode` option to specify encode of input.

It's *utf8* by default, if you put non-unicode string into functions, it will be converted to unicode by using its encode first.

```python
japanese_numbers.to_arabic_numbers('一を聞いて十を知る。')  # utf8 by default
japanese_numbers.to_arabic('一を聞いて十を知る。', encode='eucjp')  # set another charset
```

### TODO

- support float/double types
- support negative types


### Patch

Welcome!
