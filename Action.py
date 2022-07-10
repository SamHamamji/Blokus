class Action:
    def __init__(self, commands: set[str], options: set[str], get_arguments: function) -> None:
        self.commands = commands
        self.options = options
        self.get_arguments = get_arguments

    def check_input_validity(self, input: str):
        if (input not in self.commands):
            return False


POSSIBLE_ACTION_TYPES = {
    "SHOW": Action(commands={"show"}, options={"a", "b"}),  # number | show num
    "SHOW_AVAILABLE_PIECES": Action(commands={"show"}),  # nothing | put
    "SHOW_BOARD": Action(commands={"show"}),  # nothing | put
    # number, x, y | put num x y
    "PUT": Action(commands={"put"}, options={"r"}),
    "ROTATE_PIECE": Action(commands={"rotate"})
    # piece, [directions] | rotate x y
}
# 1 b 5 f
