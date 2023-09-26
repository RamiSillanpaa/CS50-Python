import twttr

def main():
    test_vowels()
    

def test_vowels():
    assert twttr.shorten("Cabbage") == "Cbbg"
    assert twttr.shorten("CABBAGE") == "CBBG"
    assert twttr.shorten(".Cabbage") == ".Cbbg"
    assert twttr.shorten("0Cabbage") == "0Cbbg"

if __name__ == "__main__":
    main()