import re

change_groups = ["FM", "TEMPO", "PROB", "BECMG"]


def taf_format(taf: str):
    """Format and return a TAF output
    """
    formatted_taf = re.sub(rf"({'|'.join(change_groups)})", r"\n\1", taf)
    print(formatted_taf)

