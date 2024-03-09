
try:
    from web_hw_1.personal_assistant_bot.classes.record import Record
    from web_hw_1.personal_assistant_bot.classes.addressbook import AddressBook
    from web_hw_1.personal_assistant_bot.classes.notes import Notes
    from web_hw_1.personal_assistant_bot.functions.functions import make_menu
    from web_hw_1.personal_assistant_bot.functions.make_header import make_header
    from web_hw_1.personal_assistant_bot.functions.sort import sort
    from web_hw_1.personal_assistant_bot.settings.settings import addressbook_filename, notes_filename
except ModuleNotFoundError:
    from personal_assistant_bot.classes.record import Record
    from personal_assistant_bot.classes.addressbook import AddressBook
    from personal_assistant_bot.classes.notes import Notes
    from personal_assistant_bot.functions.functions import make_menu
    from personal_assistant_bot.functions.make_header import make_header
    from personal_assistant_bot.functions.sort import sort
    from personal_assistant_bot.settings.settings import addressbook_filename, notes_filename

from colorama import init, Fore
import abc_consol_chat

init(autoreset=True)


def main():

    while True:

        make_header("MAIN MENU")
        choice1 = input(abc_consol_chat.MainMenu.message())

        if choice1 == "1":

            abc_consol_chat.ChoiceOneOne.message()

        elif choice1 == "2":

            abc_consol_chat.ChoiceOneTwo.message()

        elif choice1 == "3":

            switcher = True

            while switcher:

                book = AddressBook()
                book = AddressBook.read_contacts_from_file(addressbook_filename)
                record_menu = abc_consol_chat.RecordMenu.message()

                make_header("ADDESSBOOK MENU")
                choice2 = input(record_menu)

                if choice2 == "1":

                    abc_consol_chat.ChoiceTwoOne.message()

                elif choice2 == "2":

                    abc_consol_chat.ChoiceTwoTwo.message()

                elif choice2 == "3":

                    abc_consol_chat.ChoiceTwoThree.message()

                elif choice2 == "4":

                    abc_consol_chat.ChoiceTwoFour.message()

                elif choice2 == "5":

                    abc_consol_chat.ChoiceTwoFive.message()

                elif choice2 == "6":

                    abc_consol_chat.ChoiceTwoSix.message()

                elif choice2 == "7":

                    abc_consol_chat.ChoiceTwoSeven.message()

                elif choice2 == "0":
                    switcher = False

        elif choice1 == "4":
            notes = Notes().load_from_file(notes_filename)
            make_menu(notes)

        elif choice1 == "5":

            abc_consol_chat.ChoiceOneFive.message()

        elif choice1 == "0":
            break


if __name__ == '__main__':
    main(debug=False, host='0.0.0.0')
