def format_hex(value):
    return f"0x{value:x}"

def format_dec(value):
    return str(value)

def format_bin(value):
    return f"0b{value:b}"

def is_valid_address(address):
    try:
        int(address, 16)
        return True
    except ValueError:
        return False

def is_valid_value(value):
    try:
        int(value, 10)
        return True
    except ValueError:
        return False

def convert_to_hex(value):
    return f"0x{value:x}"

def convert_to_dec(value):
    return int(value, 16)

def convert_to_bin(value):
    return f"0b{value:b}"