PRODUCT_FILE_SMG = "products.txt"


def add_product_smg(product_smg):
    try:
        with open(PRODUCT_FILE_SMG, "a") as file_smg:
            file_smg.write(product_smg.get_product_info() + "\n")
    except Exception as error_smg:
        print("Error saving product:", error_smg)


def view_products_smg():
    try:
        with open(PRODUCT_FILE_SMG, "r") as file_smg:
            lines_smg = [line_smg.strip() for line_smg in file_smg if line_smg.strip()]

        if not lines_smg:
            print("No products found.")
            return

        for line_smg in lines_smg:
            print(line_smg)
    except FileNotFoundError:
        print("No products found.")


def search_product_smg(product_id_smg):
    try:
        with open(PRODUCT_FILE_SMG, "r") as file_smg:
            for line_smg in file_smg:
                data_smg = [field_smg.strip() for field_smg in line_smg.strip().split(",")]
                if len(data_smg) != 4:
                    continue
                if data_smg[0] == product_id_smg:
                    return data_smg
    except FileNotFoundError:
        pass
    return None


def update_product_quantity_smg(product_id_smg, new_quantity_smg):
    try:
        updated_smg = False
        lines_smg = []
        with open(PRODUCT_FILE_SMG, "r") as file_smg:
            for line_smg in file_smg:
                if not line_smg.strip():
                    continue
                data_smg = [field_smg.strip() for field_smg in line_smg.strip().split(",")]
                if len(data_smg) != 4:
                    lines_smg.append(line_smg)
                    continue
                if data_smg[0] == product_id_smg:
                    data_smg[3] = str(new_quantity_smg)
                    updated_smg = True
                lines_smg.append(",".join(data_smg) + "\n")

        if not updated_smg:
            return False

        with open(PRODUCT_FILE_SMG, "w") as file_smg:
            file_smg.writelines(lines_smg)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
