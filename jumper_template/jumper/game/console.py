class Console:
    """
    Shows input and output.

    stereotype: Service provider
    
    """

    def write(self,message):
        """
        Gets the message and shows it to the user.
        """

        return(input(message))

    def show_word(self,message):
        print(' '.join(message))

    def show_message(self,message):
        print(message)



