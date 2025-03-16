import sys

def minsik_sort(n, words):
    minsik_order = ["a", "b", "k", "d", "e", "g", "h", "i", "l", "m", "n", "ng", "o", "p", "r", "s", "t", "u", "w", "y"]
    order_dict = {char: idx for idx, char in enumerate(minsik_order)}
    
    def convert_key(word):
        converted = []
        i = 0
        while i < len(word):
            if i < len(word) - 1 and word[i:i+2] == "ng":
                converted.append(order_dict["ng"])
                i += 2
            else:
                converted.append(order_dict[word[i]])
                i += 1
        return converted
    
    words.sort(key=convert_key)
    
    return words

if __name__ == "__main__":
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]
    
    sorted_words = minsik_sort(n, words)
    print("\n".join(sorted_words))