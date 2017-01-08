# ohioslides
An implementation of the Slide program used by dbeazley in his 2016 PyOhio talk: 
https://www.youtube.com/watch?v=E-1Y4kSsAFc

Thank you to [@petrposik](https://twitter.com/petrposik) for asking
[this question](https://twitter.com/dabeaz/status/760123044660711424)

# Usage

```python
from slides import Slide
a_text = '''some text with *ordinary* _markup_
spanning multiple lines spanning multiple lines spanning multiple lines spanning multiple lines spanning multiple lines spanning multiple 

and with paragraphs'''
a = Slide('A header', a_text)

print(a)
```

Which will clear the terminal and print

```
+--------------------------------------------------------------------------------+
| \33[7mA header\33[0m                                                           |
|                                                                                |
| some text with \33[1mordinary\33[0m \33[4mmarkup\33[0m                         |
| spanning multiple lines spanning multiple lines spanning multiple lines spanni |
| ng multiple lines spanning multiple lines spanning multiple                    |
| and with paragraphs                                                            |
+--------------------------------------------------------------------------------+

In [2]: 
```
