import os
import re
import socket
from collections import Counter

def expand_contractions(text):
    text = re.sub(r"'s\b", " is", text)
    text = re.sub(r"n't\b", " not", text)
    text = re.sub(r"'re\b", " are", text)
    text = re.sub(r"'ve\b", " have", text)
    text = re.sub(r"'ll\b", " will", text)
    text = re.sub(r"'d\b", " would", text)
    text = re.sub(r"'m\b", " am", text)
    return text

def get_words(text, handle_contractions=False):
    if handle_contractions:
        text = expand_contractions(text)
    return re.findall(r"[a-zA-Z]+", text.lower())

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return socket.gethostbyname(socket.gethostname())

def main():
    data_dir = "/home/data"
    output_dir = "/home/data/output"
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(data_dir, "IF.txt"), "r") as f:
        if_text = f.read()
    with open(os.path.join(data_dir, "AlwaysRememberUsThisWay.txt"), "r") as f:
        always_text = f.read()

    if_words = get_words(if_text)
    always_words = get_words(always_text, handle_contractions=True)

    if_count = len(if_words)
    always_count = len(always_words)
    grand_total = if_count + always_count

    if_top3 = Counter(if_words).most_common(3)
    always_top3 = Counter(always_words).most_common(3)
    ip_address = get_ip_address()

    lines = [
        "=" * 50,
        "WORD COUNT RESULTS",
        "=" * 50,
        f"\nIF.txt word count: {if_count}",
        f"AlwaysRememberUsThisWay.txt word count: {always_count}",
        f"Grand total word count: {grand_total}",
        "\n--- Top 3 Most Frequent Words in IF.txt ---",
        *[f"  '{w}': {c}" for w, c in if_top3],
        "\n--- Top 3 Most Frequent Words in AlwaysRememberUsThisWay.txt ---",
        "  (Contractions expanded before counting)",
        *[f"  '{w}': {c}" for w, c in always_top3],
        f"\nContainer IP Address: {ip_address}",
        "=" * 50,
    ]

    result = "\n".join(lines)
    with open("/home/data/output/result.txt", "w") as f:
        f.write(result)
    print(result)
    print("\nResults saved to /home/data/output/result.txt")

if __name__ == "__main__":
    main()