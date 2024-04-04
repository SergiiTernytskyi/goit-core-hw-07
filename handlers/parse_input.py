from handlers.input_error import input_error

@input_error
def parse_input(user_input):
    cmd, *args = user_input.strip().lower().split()
    cmd = cmd.strip().lower()
    return cmd, *args
