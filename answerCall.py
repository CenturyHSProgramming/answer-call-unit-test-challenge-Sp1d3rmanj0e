# answerCall.py
# by Jason Pelkey

# For instructions on what to do, see README.md
# or visit (https://github.com/HundredVisionsGuy/answerCall)

# Write function defintion: answerCall()
def answerCall(caller_code, sameAreaCode, cur_time):
    # "U" "R" "F" "T"
    # True/False
    # "##:##"
    '''
    Check time first.  No matter what, <7:00 or >22:00 DON'T ANSWER PHONE.  Otherwise, CONTINUE
    Check caller_code Second.  If Friend or Relative, ANSWER PHONE.  If unknown, CONTINUE. Otherwise, DON'T ANSWER PHONE
    Check area code last.  If True, ANSWER PHONE.  Otherwise, CONTINUE

    '''

    # Remove the ":" from the military time
    cur_time_trimmed = cur_time.replace(":", "")

    # Change from String to Number (Ex. "900" -> 900)
    cur_time_num = int(cur_time_trimmed)

    # FIRST CHECK  >>> <700 or >2200, DON'T ANSWER
    if (cur_time_num < 700) or (cur_time_num > 2200): return False

    # SECOND CHECK >>> If Friend or Relative, ANSWER PHONE.  If unknown, CONTINUE. Otherwise, DON'T ANSWER PHONE
    if (caller_code == "F") or (caller_code == "R"): return True
    if (caller_code == "T"): return False

    # THIRD CHECK  >>> If area code known (TRUE), return True.  Otherwise, return False
    return sameAreaCode

if __name__ == '__main__':
    # Call the function in here if you want to test it
    print(answerCall("U", True, "09:00"))
    print(answerCall("U", False, "14:00"))
    print(answerCall("U", True, "23:50"))
    print(answerCall("T", True, "10:40"))
    print(answerCall("T", False, "23:00"))
    print(answerCall("F", False, "10:00"))
    print(answerCall("F", False, "23:00"))
    print(answerCall("R", True, "9:00"))
    print(answerCall("R", False, "4:00"))
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function

'''
* "U" True "09:00" => True
* "U" False "14:00" => False
* "U" True "23:50" => False
* "T" True "10:40" => False
* "T" False "23:00" => False
* "F" False "10:00' => True
* "F" False "23:00" => False
* "R" True "9:00" => True
* "R" False "4:00" => False
'''