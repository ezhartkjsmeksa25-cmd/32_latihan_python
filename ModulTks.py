def text_converter(text):
    if text.lower() == 'x' or text.strip() == "":
        return None
    return {
        "uppercase": text.upper(),
        "lowercase": text.lower(),
        "titlecase": text.title()
    }

def count_words(text):
    if text.lower() == 'x' or text.strip() == "":
        return None
    return {
        "words": len(text.split()),
        "chars": len(text)
    }