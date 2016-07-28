# japanese_numbers

A parser for Japanese number (Kanji, arabic) in the natural language.

Japanese-numbers finds any numbers in the natural language, and convert to arabic.
The followings are an example patterns what can be parsed.

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

Function `to_arabic` is almost stable. It returns An array of *[japanese_numbers.result.ParsedResult]* is returned basically.

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

