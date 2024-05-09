import os
from Speak import Say
from Listen import Listen

def handle_shutdown():

    try:
        # Ask the user to confirm the shutdown using voice input
        Say("Are you sure you want to shut down the system? Please speak Ok or Cancel.")
        response = Listen().lower()

        if "ok" in response:
            # Confirm the shutdown and provide feedback
            Say("Shutting down the system.")
            os.system("shutdown /s /t 1")
        elif "cancel" in response:
            # Provide feedback that shutdown was canceled
            Say("Shutdown canceled.")
    except:
        # Handle unrecognized responses
        Say("Sorry, I didn't understand your response. Shutdown canceled.")



# Example usage:
query = Listen()  # Retrieve the user query from a voice input function
handle_shutdown()
