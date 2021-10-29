from rich import print


def print_header(text):
    print(header(text))


def print_kv(k, v):
    print(kv(k, v))


def header(text):
    return f"[bold black on bright_white] { text } [/bold black on bright_white]"


def kv(k, v):
    return f"[bold cyan] { k } :[/bold cyan] { v } "
