import sys
from io import StringIO

def test(input_file):
    # function called on each individual file
    expected = '''1 \t 1 \t 1 \t 1
2 \t 4 \t 5 \t 5
3 \t 9 \t 14 \t 14
4 \t 16 \t 30 \t 30
5 \t 25 \t 55 \t 55
6 \t 36 \t 91 \t 91
7 \t 49 \t 140 \t 140
8 \t 64 \t 204 \t 204
9 \t 81 \t 285 \t 285
10 \t 100 \t 385 \t 385''' # could use a code
    
    def get_output():
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        with open(input_file, 'r') as f:
            code = f.read()
            exec(code)
        sys.stdout = old_stdout
        return redirected_output.getvalue()
    s = get_output()
    return 1 if expected in s else 0