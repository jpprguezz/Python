def run(input_path: str, output_path: str) -> None:
    f_input = open(input_path, "r")
    f_output = open(output_path, "w")

    for month in f_input:
        days = month.strip().split(",")
        int_days = []
        for day in days:
            int_days.append(int(day))
        calc = sum(int_days) / len(int_days)
        calc_rounded = round(calc, 2)
        f_output.write(f"{calc_rounded:.2f}\n")


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
