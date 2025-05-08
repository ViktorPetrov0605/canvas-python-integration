from canvasapi import Canvas
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_URL = os.getenv('CANVAS_DOMAIN')
API_KEY = os.getenv('CANVAS_API_TOKEN')

# Initialize Canvas API client
canvas = Canvas(API_URL, API_KEY)

# Search for specific course by name
target_course = "OL-OLPERS-I552795"
course = None

for c in canvas.get_courses():
    if c.name == target_course:
        course = c
        break

if course:
    print(f"Found course: {course.name}")
    
    # Retrieve all assignments
    assignments = course.get_assignments()
    
    if assignments:
        print("\nAssignments:")
        for assignment in assignments:
            print(f"- {assignment.name}")
            print(f"  Due: {assignment.due_at}")
            print(f"  Details: {assignment.description}\n")
    else:
        print("No assignments found for this course.")
else:
    print(f"Course '{target_course}' not found.")
    
