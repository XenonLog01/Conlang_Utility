def clean_line(line):
    last_was_ws = False
    in_comment = False
    out = ''
    for t in line:
        if t in ' \t':
            if last_was_ws:
                continue
            else:
                last_was_ws = True
        else:
            last_was_ws = False

        if in_comment:
            continue
        else:
            if t == '#':
                in_comment = True
            else:
                out += t

    return out
