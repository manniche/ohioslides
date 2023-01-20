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

Alternatively, you can also have multiple slides **saved** in variables which then can
be called from the Python interactive in a presentation mode, like David did. 
For example, have below code snippet saved in a file, say test1.py.

```python
from slides import Slide

text1 = '''some text111111111111 with *ordinary* _markup_
spanning multiple lines spanning multiple lines spanning multiple lines spanning multiple lines spanning multiple lines spanning multiple 

and with paragraphs'''
slide1 = Slide('A header', text1)

text2 = '''some text2222222222222 with *ordinary* _markup_
spanning multiple lines spanning multiple lines spanning multiple lines spanning multiple lines spanning multiple lines spanning multiple 

and with paragraphs'''
slide2 = Slide('A header', text2)

```

In Python interactive shell, enter
```python
>>> from test1 import *
```

Then enter,
```python
>>> slide1
```

You will find slide1 displayed.


Then enter,
```python
>>> slide2
```

You will find slide2 displayed.




