import sys
import pycparser

from pycparserext.ext_c_parser import GnuCParser
p = GnuCParser()
if len(sys.argv) > 1:
    src = sys.argv[1]

    text =  pycparser.preprocess_file(src, 'cpp')

    #print text
    ast = p.parse(text)
    ast.show()
