def run(data: dict, target_keys: tuple) -> dict:
    pdata = {}
    for subject, grade in data.items():
        for target_key in target_keys:
            if subject == target_key:
                pdata[subject] = grade
    return pdata


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
