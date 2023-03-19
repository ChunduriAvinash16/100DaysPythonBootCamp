

def format_name(f_name,l_name):
    """
    :param f_name:
    :param l_name:
    :return: name
    """
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("avinash","Chunduri"))