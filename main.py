def count_words(text):
    txt_to_count = text.split()
    total_words = len(txt_to_count)
    return total_words


def count_characters(text):
    chr_counts = {}
    text = text.lower()
    for chr in text:
        if chr not in chr_counts:
            chr_counts[chr] = text.count(chr)
    return chr_counts


def main():
    with open("books/frankenstein.txt") as f:
            file_contents = f.read()
    total_words = count_words(file_contents)
    chr_counts = count_characters(file_contents)
    print(f"{total_words} words found in the document")
    for chr in chr_counts:
        if chr.isalpha():
            print(f"The '{chr}' character was found {chr_counts[chr]} times")
    
    
if __name__ == "__main__":
    main()