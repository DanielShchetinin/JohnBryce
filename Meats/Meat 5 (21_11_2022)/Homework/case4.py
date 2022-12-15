alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def main():
    text = "The quick brown fox jumps over the lazy dog"
    result = result = isPangramText(text)
    
    print(result)
    return 1

def isPangramText(text: str) -> bool:
    
    for char in alphabet:
        if text.count(char) == 0:
            return False
    
    return True

if __name__ == '__main__':
    main()