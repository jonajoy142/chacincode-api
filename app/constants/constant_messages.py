"""
sample usage:
print(CustomMessages.not_found_message(data='looking data'))
"""


class CustomMessages:
    """
    class to store custom messages
    """
    @staticmethod
    def not_found_message(data: str = ' ') -> str:
        """
        return a not found message with data formatted to the string.
        Args:
            data (str, optional): data want to add to the message.
            Defaults to ' '.

        Returns:
            str: not found message
        """
        return f"Required data : {data} NOT FOUND"

    @staticmethod
    def user_not_found_message(id: str = ' ') -> str:
        """
        make user not found message
        Args:
            id (str, optional): id of the user checked. Defaults to ' '.

        Returns:
            str: error message
        """
        return f"User with id {id} is NOT FOUND"

    @staticmethod
    def user_already_exists_message(id: str = ' ') -> str:
        """
        make user already exists message
        Args:
            id (str, optional): id of the user checked. Defaults to ' '.

        Returns:
            str: error message
        """
        return f"User with id {id} already exists"
