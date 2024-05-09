'''
#Function
def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm1.py")
      
    
     
    elif "set an alarm" in query:
            print("input time example:- 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :-")
            alarm(a)
            speak("Done,sir")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            # speak(f"Sir,the time is {strTime}")

'''

# from Speak import Say
# from Listen import Listen
# import datetime
# import os
#
#
#
#
# extractedtime = open("Alarmtext.txt", "rt")
# time = extractedtime.read()
# Time = str(time)
# extractedtime.close()
#
# deletetime = open("Alarmtext.txt", "r+")
# deletetime.truncate(0)
# deletetime.close()
#
#
# def ring(time):
#     timeset = str(time)
#     timenow = timeset.replace("jarvis", "")
#     timenow = timenow.replace("set an alarm", "")
#     timenow = timenow.replace(" and ", ":")
#     Alarmtime = str(timenow)
#     print(Alarmtime)
#     while True:
#         currenttime = datetime.datetime.now().strftime("%HH:%MM")
#         if currenttime == Alarmtime:
#             Say("Alarm ringing,sir")
#             os.startfile("AlarmNotification.mp3")  # You can choose any music or ringtone
#         elif currenttime + "00:00:30" == Alarmtime:
#             exit()
#
#
# ring(time)

import os
import time as time_module
import datetime
from Speak import Say
from Listen import Listen


# Function to handle alarm setup and ringing
def set_alarm():
    # Handle setting an alarm based on voice query
    # if "set an alarm" in query.lower():

        Say("Please specify the time for the alarm (e.g., '10:30').")
        # alarm_time = Listen().strip()
        alarm_time = input("Enter Time:")

        # Write the alarm time to the file
        with open("Alarmtext.txt", "w") as alarm_file:
            alarm_file.write(alarm_time)

        Say(f"Alarm set for {alarm_time}.")

    # # Handle checking the current time
    # elif "the time" in query.lower():
    #     current_time = datetime.datetime.now().strftime("%H:%M")
    #     Say(f"Sir, the current time is {current_time}.")


# Function to ring the alarm at the specified time
def ring_alarm():
    # Read the alarm time from the file
    with open("Alarmtext.txt", "r") as alarm_file:
        alarm_time = alarm_file.read().strip()

    Say(f"Waiting for alarm at {alarm_time}.")

    # Infinite loop to check the time and ring the alarm if it matches
    while True:
        # Get the current time
        current_time = datetime.datetime.now().strftime("%H:%M")

        # Check if the current time matches the alarm time
        if current_time == alarm_time:
            Say("Alarm ringing, sir.")
            os.startfile("AlarmNotification.mp3")  # Play alarm sound
            # Clear the alarm time in the file
            with open("Alarmtext.txt", "w") as alarm_file:
                alarm_file.write("")
            break  # Exit the loop after ringing the alarm

        # Sleep for a short duration to avoid busy-waiting
        time_module.sleep(1)


# Main function to handle queries and set the alarm
def handle_alarm():
    set_alarm()
    ring_alarm()



# handle_alarm()

