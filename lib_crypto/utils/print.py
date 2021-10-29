from rich import print


def print_header(text):
    print(f"[bold black on bright_white] { text } [/bold black on bright_white]")


def print_kv(k, v):
    print(f"[bold cyan] { k } :[/bold cyan] { v } ")
