def make_ascii(s):
    """
    Convert text to ASCII
    """
    return "".join(i for i in s if ord(i) < 128)
