from options_menu import Option, OptionsHandler


def test_options():
    option_one = Option(
        "Option One",
        "This is option one.",
        lambda session, setting: print(f"session: {session}, setting: {setting}"),
        setting="setting"
    )
    option_two = Option(
        "Option Two",
        "This is option two.",
        lambda: print("Option Two")
    )
    option_three = Option(
        "Option Three",
        "This is option three.",
        lambda: print("Option Three")
    )

    options_list = [option_one, option_two, option_three]
    option_menu = OptionsHandler(options_list)

    running = True
    while running:
        for menu_item in option_menu.options_menu:
            print(menu_item)

        option_prompt = input("Select an option: ")
        if option_prompt.isdigit():
            option_prompt = int(option_prompt)
            if 0 < option_prompt <= len(option_menu.options):
                confirm_prompt = input(option_menu.get_confirm_statement(option_prompt))
                if confirm_prompt.lower() == "y":
                    option_menu.select_option(option_prompt, session="session")
                else:
                    print("Cancelled.")
            else:
                print("Invalid option.")

        continue_prompt = input("Continue? (y/n) ")
        running = continue_prompt.lower() == "y"


if __name__ == "__main__":
    test_options()