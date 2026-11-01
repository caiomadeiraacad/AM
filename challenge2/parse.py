import re

def parse_html_tags(text):
    text = re.sub(r"<[^>]*>", " ", text)
    text = text.replace("<", " ").replace(">", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def invert_html_labels(label):
    if label == "good":
        return "bad"
    else:
        return "good"