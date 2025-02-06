def run(input_path: str, line_no: int) -> str | None:
    with open(input_path, "r", encoding='utf-8') as f:
        line = None
        for f_num, f_line in enumerate(f, 1):
            if f_num == line_no:
                line = f_line.strip()

    return line


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
