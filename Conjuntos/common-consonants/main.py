def run(text1: str, text2: str) -> str:
    VOWELS = 'aeiou'
    common_letters = ''
    text1 = text1.replace(' ', '').lower()
    text2 = text2.replace(' ', '').lower()
    for letter1 in set(text1):
        if letter1 in set(text2):
                if letter1 not in VOWELS:
                    common_letters += letter1.lower()
    cconst = ''.join(sorted(common_letters))

    return cconst


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
