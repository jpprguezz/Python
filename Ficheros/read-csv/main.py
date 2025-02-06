def run(datafile: str) -> list:
    data = []
    with open(datafile, "r") as f:
        data_types = f.readline().strip().split(",")
        for line in f:
            line_splitted = line.strip().split(",")
            dict_datafile = {}
            for data_type, item in zip(data_types, line_splitted):
                item_stripped = item.strip()
                if item_stripped == "":
                    dict_datafile[data_type] = None
                elif item_stripped == "True":
                    dict_datafile[data_type] = True
                elif item_stripped == "False":
                    dict_datafile[data_type] = False
                elif item_stripped.isnumeric():
                    dict_datafile[data_type] = int(item_stripped)
                else:
                    dict_datafile[data_type] = item_stripped
            data.append(dict_datafile)

    return data


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
