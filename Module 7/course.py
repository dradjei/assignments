if __name__ == "__main__":
    room_numbers = {"CSC101": 3004, "CSC102": 4501, "CSC103": 6755, "NET110": 1244, "COM241": 1411}
    instructors = {"CSC101": "Haynes", "CSC102": "Alvarado", "CSC103": "Rich", "NET110": "Burke", "COM241": "Lee"}
    meeting_time = {"CSC101": "8:00 a.m.", "CSC102": "9:00 a.m.", "CSC103": "10:00 a.m.", "NET110": "11:00 a.m.",
                    "COM241": "1:00 p.m."}

    course_found = False
    while course_found is False:
        course_number = input("Enter Course Number: ")
        if course_number in room_numbers.keys():
            course_found = True
        if course_found is True:
            print(course_number, "|",
                  "Room Number:", room_numbers[course_number], "|",
                  "Instructor:", instructors[course_number], "|",
                  "Meeting Time:", meeting_time[course_number])
