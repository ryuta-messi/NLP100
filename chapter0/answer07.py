def generate_sentence(x: int, y: str, z: int) -> str:
    return f"{x}時の{y}は{z}"


if __name__ == "__main__":
    x = 12
    y = "気温"
    z = 22.4

print(generate_sentence(x, y, z))
