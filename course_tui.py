# filename: canvas_terminal.py
from canvasapi import Canvas
from dotenv import load_dotenv
import os
from datetime import datetime

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


def create_assignment_preview(course, assignment_data):
    """Displays a preview of the assignment data before creation."""
    print("\nAssignment Preview:")
    for key, value in assignment_data.items():
        print(f"  {key}: {value}")
    confirmation = input("Confirm creation (y/n)? ").lower()
    if confirmation == 'y':
        return True
    else:
        return False


def create_assignment(course, assignment_data):
    """Creates an assignment using the provided data."""
    try:
        new_assignment = course.create_assignment(assignment_data)
        print(f"Assignment '{new_assignment.name}' created successfully.")
        return new_assignment
    except Exception as e:
        print(f"Error creating assignment: {e}")
        return None


def edit_assignment_preview(assignment, assignment_data):
    """Displays a preview of the assignment data before editing."""
    print("\nAssignment Edit Preview:")
    for key, value in assignment_data.items():
        print(f"  {key}: {value}")
    confirmation = input("Confirm edit (y/n)? ").lower()
    if confirmation == 'y':
        return True
    else:
        return False


def edit_assignment(assignment, assignment_data):
    """Edits an existing assignment using the provided data."""
    try:
        updated_assignment = assignment.edit(assignment_data)
        print(f"Assignment '{updated_assignment.name}' updated successfully.")
        return updated_assignment
    except Exception as e:
        print(f"Error updating assignment: {e}")
        return None


def main_menu():
    """Main menu for the Canvas API terminal interface."""
    while True:
        print("\nCanvas API Terminal Interface")
        print("1. List All Courses")
        print("2. View Assignments for a Course")
        print("3. Create Assignment")
        print("4. Edit Assignment")
        print("5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")

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
            courses = list_courses()
            if not courses:
                print("No courses found.")
                continue
            course_num = int(input("Enter course number: "))
            selected_course = courses[course_num - 1]

            assignment_data = {}
            assignment_data['name'] = input("Enter assignment name: ")
            assignment_data['points_possible'] = int(input("Enter points possible: "))
            assignment_data['due_at'] = input("Enter due date (YYYY-MM-DD HH:MM) : ")
            try:
                due_date = datetime.strptime(assignment_data['due_at'], '%Y-%m-%d %H:%M')
                assignment_data['due_at'] = due_date
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD HH:MM.")
                continue

            if create_assignment_preview(selected_course, assignment_data):
                new_assignment = create_assignment(selected_course, assignment_data)
            else:
                print("Assignment creation cancelled.")
            continue
        elif choice == '4':
            courses = list_courses()
            if not courses:
                print("No courses found.")
                continue
            course_num = int(input("Enter course number: "))
            selected_course = courses[course_num - 1]

            assignments = list_assignments(selected_course)
            if not assignments:
                print("No assignments found for this course.")
                continue

            print("\nAssignments:")
            for idx, assignment in enumerate(assignments, 1):
                print(f"{idx}. {assignment.name}")

            assignment_num = int(input("Enter assignment number to edit: "))
            assignment_to_edit = assignments[assignment_num - 1]

            assignment_data = {}
            print("Enter new values (leave blank to keep current value):")
            new_name = input("New name: ")
            if new_name:
                assignment_data['name'] = new_name
            new_points = input("New points possible: ")
            if new_points:
                try:
                    assignment_data['points_possible'] = int(new_points)
                except ValueError:
                    print("Invalid points value.  Keeping current value.")
            new_due_at = input("New due date (YYYY-MM-DD HH:MM): ")
            if new_due_at:
                try:
                    due_date = datetime.strptime(new_due_at, '%Y-%m-%d %H:%M')
                    assignment_data['due_at'] = due_date
                except ValueError:
                    print("Invalid date format. Keeping current value.")

            if edit_assignment_preview(assignment_to_edit, assignment_data):
                updated_assignment = edit_assignment(assignment_to_edit, assignment_data)
            else:
                print("Assignment edit cancelled.")
            continue
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
