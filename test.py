from pycparserext.ext_c_parser import GnuCParser
p = GnuCParser()
src="""
typedef int wchar_t;
extern wchar_t *wcscpy (wchar_t *restrict __dest,
const wchar_t *__restrict __src) __attribute ((nothrow , leaf));

"""
p.parse(src).show()
