def cipher(text):
    text = [chr(219-ord(w)) if 97 <= ord(w) <= 122 else w for w in text]
    return "".join(text)


if __name__ == "__main__":
    text = 'this is a message'
    ans = cipher(text)
    print(ans)
    ans = cipher(ans)
    print(ans)
