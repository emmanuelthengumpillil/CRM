
FUNCTIONS IN CRM



STORAGE.PY
----------
read_csv(file)
write_csv(file,row_dict)
rewrite_csv(file,rows,header)
get_next_id(file)
find_row_by_id(file,id)
load_all(file)


VALID.PY
--------
valid_name(name)
valid_phone(phone)
valid_email(email)
valid_dict(dict,header)


INPUTS.PY
---------
get_name()
get_phone()
get_email()
get_id()


FUNCTIONS.PY
------------
add_person(file, row)
remove_person(file, row)
update_person(file, old_row, new_row)
search_person(file, criteria)
display_all(file)
is_duplicate(file,row_dict)


