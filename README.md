# PythonSnippits


A collection of interesting Python Snippits.


+ ### JsonParser
   Turns a Python Dict into a class where the keys are attributes. Works for nested Dicts too.
      Example:
  
        d = {'a': 'Apple', 'b': {'c': "Class"}}
        j = JsonParser(d)
        assert j.a == 'Apple'
        assert j.b.c == 'Class'
        assert j == d
    
