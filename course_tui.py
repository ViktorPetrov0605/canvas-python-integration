from canvasapi import Canvas
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
API_URL = os.getenv('CANVAS_DOMAIN')
API_KEY = os.getenv('CANVAS_API_TOKEN')

# Initialize Canvas API
canvas = Canvas(API_URL, API_KEY)

def list_courses():
    """Retrieve all courses the user has access to"""
    courses = []
    for course in canvas.get_courses():
        courses.append(course)
    return courses

def list_assignments(course):
    """Retrieve all assignments for a specific course"""
    return course.get_assignments()

def main_menu():
    while True:
        print("\nCanvas API Terminal Interface")
        print("1. List All Courses")
        print("2. View Assignments for a Course")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")
        
        if choice == '1':
            courses = list_courses()
            print("\nCourses:")
            for idx, course in enumerate(courses, 1):
                print(f"{idx}. {course.name} ({course.course_code})")
            continue
            
        elif choice == '2':
            courses = list_courses()
            if not courses:
                print("No courses found.")
                continue
            course_num = int(input("Enter course number: "))
            selected_course = courses[course_num - 1]
            assignments = list_assignments(selected_course)
            print(f"\nAssignments for {selected_course.name}:")
            for assignment in assignments:
                print(f"- {assignment.name}")
                print(f"  Due: {assignment.due_at}")
                print(f"  Points: {assignment.points_possible}\n")
            continue
            
        elif choice == '3':
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
