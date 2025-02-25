import tokenize
from io import StringIO
"""
    Returns 'source' minus comments and docstrings.
    referenced from: https://stackoverflow.com/questions/1769332/script-to-remove-python-comments-docstrings
"""
def remove_comments_and_docstrings(source):    
    io_obj = StringIO(source)
    out = ""
    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0
    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok[0]
        token_string = tok[1]
        start_line, start_col = tok[2]
        end_line, end_col = tok[3]
        #ltext = tok[4]
        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            out += (" " * (start_col - last_col))
        if token_type == tokenize.COMMENT:
            # Comment
            pass
        # elif token_type == tokenize.STRING and prev_toktype == tokenize.INDENT:
        #     # Docstring
        #     pass
        elif token_type == tokenize.STRING:
            if prev_toktype != tokenize.INDENT:
                #if prev_toktype != tokenize.NEWLINE:
                    if start_col > 0:
                        out += token_string
        else:
            out += token_string
        prev_toktype = token_type
        last_col = end_col
        last_lineno = end_line
    out = '\n'.join(l for l in out.splitlines() if l.strip())
    return out