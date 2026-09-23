from nltk.corpus import wordnet

def get_comparative_superlative(word):
    word = word.strip().lower()
    
    # 1. Các từ bất quy tắc phổ biến
    irregulars = {
        'good': ('better', 'best'),
        'bad': ('worse', 'worst'),
        'little': ('less', 'least'),
        'many': ('more', 'most'),
        'much': ('more', 'most'),
        'far': ('farther', 'farthest')
    }
    if word in irregulars:
        return irregulars[word]

    # 2. Quy tắc cho từ kết thúc bằng 'y' (happy -> happier / happiest)
    if word.endswith('y') and len(word) > 2:
        return word[:-1] + 'ier', word[:-1] + 'iest'

    # 3. Quy tắc Nguyên âm + Phụ âm ở từ 1 âm tiết (big -> bigger / biggest)
    vowels = 'aeiou'
    if len(word) >= 3 and word[-1] not in vowels and word[-2] in vowels and word[-3] not in vowels:
        if word[-1] not in ['w', 'x', 'y']:
            return word + word[-1] + 'er', word + word[-1] + 'est'

    # 4. Từ kết thúc bằng 'e' (large -> larger / largest)
    if word.endswith('e'):
        return word + 'r', word + 'st'

    # 5. Từ ngắn thông thường (fast -> faster / fastest)
    if len(word) <= 5:
        return word + 'er', word + 'est'

    # 6. Từ dài (thêm more / most)
    return f"more {word}", f"most {word}"

def main():
    adjs = input("Enter a list of adjectives (comma-separated): ").split(",")
    
    print("\n{:15} {:15} {:15}".format("Adjective", "Comparative", "Superlative"))
    print("-" * 45)
    
    for adj in adjs:
        adj = adj.strip()
        if adj:
            comp, sup = get_comparative_superlative(adj)
            print("{:15} {:15} {:15}".format(adj, comp, sup))

if __name__ == "__main__":
    main()