from rich.console import Console
import secrets
import string
import argparse

console = Console()

parser = argparse.ArgumentParser(prog="PasswordGen", description="A password generator", epilog="Password length must be larger than 8 and lower than 32.")
parser.add_argument("--length", "-len", help="The password length", type=int, required=True)
parser.add_argument("--digits", "-d",help=argparse.SUPPRESS, action='store_true', default=True)
parser.add_argument("--no-digits", help="Exclude digits from the password", action='store_false', dest='digits')
parser.add_argument("--letters", "-l", help=argparse.SUPPRESS, action='store_true', default=True)
parser.add_argument("--no-letters", help="Exclude letters from the password", action='store_false', dest='letters')
parser.add_argument("--symbols", "-s", help=argparse.SUPPRESS, action='store_true', default=True)
parser.add_argument("--no-symbols", help="Exclude symbols from the password", action='store_false', dest='symbols')
args = parser.parse_args()

if args.length < 8:
    console.print("[bold red]Password length is too low![/]")
elif args.length > 32:
    console.print("[bold red]Password length is too high![/]")
else:
    if not (args.digits or args.letters or args.symbols):
        console.print("[bold red]At least one character type must be specified (digits, letters, symbols)![/]")
    else:
        chars = []
        passwd = ""
        if args.digits:
            chars += list(string.digits)
        if args.letters:
            chars += list(string.ascii_letters)
        if args.symbols:
            chars += list(string.punctuation)

        for _ in range(args.length):
            passwd += secrets.choice(chars)

        console.print(f"[bold green]{passwd}[/]")