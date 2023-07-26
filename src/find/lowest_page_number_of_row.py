from .column_titles import columns, columns_nested

def lowest_page_number_of_row(row):
    nested_rows = row[columns[2]]
    lowest_page_number = 10000000 # TODO: This is so goofy
    for nested_row in nested_rows:
        page_number = nested_row[columns_nested[1]]
        page_number_int = int(page_number)
        if page_number_int < lowest_page_number:
            lowest_page_number = page_number_int

    return str(lowest_page_number)