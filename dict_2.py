import csv

knowledge = {
    "FUNCTION": ("""a series of statements which returns some value to a caller. It can also be passed zero or more arguments which may be used in the execution of the body.""", """https://docs.python.org/3/reference/compound_stmts.html#function """),
    "PARAMETER": ("""a named entity in a function (or method) definition that specifies an argument (or in some cases, arguments) that the function can accept. """, """https://docs.python.org/3/glossary.html#term-parameter """),
    "VARIABLE": ("""is a label for a location in memory. It can be used to hold a value. In Python, we may reuse the same variable to store values of any type.""", """http://python-textbok.readthedocs.io/en/1.0/Variables_and_Scope.html"""),
    "ARGUMENT": ("""a value passed to a function (or method) when calling the function""", """https://docs.python.org/3/glossary.html#term-argument """),
    "DICTIONARY": ("""are unordered bags of key-value pair. When you add a key to a dictionary, you must also add a value for that key. There are optimized for retrieving the value when you know the key, but not the other way around.""", """ http://www.diveintopython3.net/native-datatypes.html"""),
    "TUPLE": ("""immutable sequence operation. Tuples implement all of the common sequence operations. May be constructed in a number of ways e.g. using a trailing comma  "a," or parentheses "(a,)" """, """ https://docs.python.org/3/library/stdtypes.html#tuple"""),
    "ASCII": ("""is a character encoding standard. ASCII encodes 128 specified characters. The characters encoded are numbers 0 to 9, lowercase letters a to z, uppercase letters A to Z, basic punctuation symbols, control codes that originated with Teletype machines and a space.""", """ https://en.wikipedia.org/wiki/ASCII"""),
    "MODULE": ("""An object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of importing. """, """https://docs.python.org/3/glossary.html#term-module """),
    "STRING": (""" textual data in Python, immutable sequences of Unicode code points. There are written by single, double or triple quotes""", """https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range"""),
    "SCOPE": ("the part of a program where a variable is accessible ", """http://python-textbok.readthedocs.io/en/1.0/Variables_and_Scope.html"""),
    "LIST": ("""are mutable sequences, typically used to store collections of homogeneous items. Lists may be constructed e.g. using square brackets, separating items with commas: [a], [a, b, c]""", """https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range"""),
    "BOOLEAN": ("""are either true or false. Python has two constants, cleverly named True and False,which can be used to assign boolean values directly """, """http://www.diveintopython3.net/native-datatypes.html """),
    "IMMUTABLE": ("""an object with a fixed value. Immutable objects include numbers, strings and tuples. Such an object cannot be altered. A new object has to be created if a different value has to be stored. They play an important role in places where a constant hash value is needed, for example as a key in a dictionary """, """https://docs.python.org/3/glossary.html#term-function"""),
    "ITERABLE": ("""an object capable of returning its members one at a time. Examples of iterables include all sequence types (such as list, str, and tuple) and some non-sequence types like dict, file objects. """, """https://docs.python.org/3/glossary.html#term-function"""),
    "NUMBERS": ("""Python supports integers, floating point numbers and complex numbers. They are defined as int, float and complex class in Python.""", """https://www.programiz.com/python-programming/numbers""")

}

with open('my_dict.csv', "w") as csvfile:
    writer = csv.writer(csvfile)

    for key, value in knowledge.items():
        writer.writerow([key, value])
    csvfile.close()

with open('my_dict.csv') as csvfile:
    reader = csv.reader(csvfile)
    knowledge_2 = dict(reader)
    csvfile.close()

print(knowledge_2)
