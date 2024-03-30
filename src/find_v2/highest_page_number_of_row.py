from .column_titles import columns, columns_nested

def highest_page_number_of_row(row):
    nested_rows = row[columns[2]]
    highest_page_number = 0
    for nested_row in nested_rows:
        page_number = nested_row[columns_nested[1]]
        page_number_int = int(page_number)
        if page_number_int > highest_page_number:
            highest_page_number = page_number_int

    return str(highest_page_number)