import argparse
import sys

from rich.console import Console


def _json_mode_requested():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--json", action="store_true")
    args, _ = parser.parse_known_args()
    return args.json


# When --json is requested, route the rich console (banner, progress bar, errors,
# debug output) to stderr so it doesn't interleave with the NDJSON stream on stdout.
nxc_console = Console(
    soft_wrap=True,
    tab_size=4,
    file=sys.stderr if _json_mode_requested() else sys.stdout,
)
