from options_menu.option import Option


class OptionsHandler:
    """
    Options is to be used to create an option menu for the user.
    Describe and option and assign it an action.
    It will deliver a list of options to be plugged into your application.
    """
    OPTIONS_MAIN = [Option("Quit", "Return to the main menu.", lambda: print("Quit selected."))]

    def __init__(self, options_list: list[Option]):
        self.options = OptionsHandler.OPTIONS_MAIN + options_list
        self.options_menu = self.create_options_menu()

    def create_options_menu(self):
        """Create the options menu."""
        options_menu = []
        for idx, option in enumerate(self.options):
            options_menu.append(f"{idx}. {option.summary}")
        return options_menu

    def get_confirm_statement(self, idx: int):
        stmt = f"Confirm: {self.options[idx].description} (y/n) "
        return stmt

    def select_option(self, idx: int, **kwargs):
        """Select an option."""
        self.options[idx].execute_action(**kwargs)

    def __repr__(self):
        return f"<Option(description={self.description!r}, action={self.action!r})>"

