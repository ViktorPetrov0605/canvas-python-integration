# filename: canvas_terminal.py
# filename: canvas_terminal.py
from canvasapi import Canvas
from dotenv import load_dotenv
import os
from datetime import datetime
import requests

# Load environment variables from .env file
load_dotenv()
API_URL = os.getenv('CANVAS_DOMAIN')
API_KEY = os.getenv('CANVAS_API_TOKEN')

# Initialize Canvas API
canvas = Canvas(API_URL, API_KEY)

def call_ollama(prompt: str) -> dict:
    """Call Ollama running locally for confirmation or processing."""
    # Adjust URL and payload as needed by your local Ollama setup
    url = "http://localhost:11434/api/ollama"
    response = requests.post(url, json={"prompt": prompt})
    return response.json()

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
    """Displays a preview of the assignment data and gets confirmation from Ollama."""
    preview = "\nAssignment Preview:\n" + "\n".join([f"  {k}: {v}" for k, v in assignment_data.items()])
    # Call Ollama to decide whether to proceed
    prompt = f"{preview}\nApprove creation of this assignment? Respond with yes or no."
    ollama_response = call_ollama(prompt)
    if ollama_response.get("approval", "").lower() == "yes":
        return True
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
    """Displays a preview of the edited assignment data and gets confirmation from Ollama."""
    preview = "\nAssignment Edit Preview:\n" + "\n".join([f"  {k}: {v}" for k, v in assignment_data.items()])
    prompt = f"{preview}\nApprove edit of this assignment? Respond with yes or no."
    ollama_response = call_ollama(prompt)
    if ollama_response.get("approval", "").lower() == "yes":
        return True
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

# Functions are now intended to be called with necessary parameters,
# possibly orchestrated by external code or API endpoints.
