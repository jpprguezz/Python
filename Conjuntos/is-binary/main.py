def run(number: str) -> bool:
    for digit in number:
        if digit == '0' or digit == '1':
            binary = True
        else:
            binary = False
            break
    return binary


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
