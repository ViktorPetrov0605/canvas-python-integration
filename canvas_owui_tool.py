"""
title: Canvas Course Tool
author: VP
description: Interact with assignments in a per-course basis inside the canvas LMS
required_open_webui_version: 0.5.0
requirements: canvasapi, pydantic, typing
version: 0.1.0
license: MIT
"""

import canvasapi
from pydantic import BaseModel, Field
from typing import Any, List, Dict, Optional


def _module_to_dict(module: Any) -> Dict[str, Any]:
    """
    Convert a Module object to a dictionary with structured data.
    Args:
        module (Any): A Canvas Module object.
    Returns:
        Dictionary with module details.
    """
    return {
        "id": module.id,
        "name": module.name,
        "position": module.position,
        "unlock_at": module.unlock_at,
        "require_sequential_progress": module.require_sequential_progress,
        "requirement_type": module.requirement_type,
        "publish_final_grade": module.publish_final_grade,
        "prerequisite_module_ids": module.prerequisite_module_ids,
        "state": module.state,
        "completed_at": module.completed_at,
        "published": module.published,
        "items_count": module.items_count,
        "items_url": module.items_url,
    }


def _detailed_assignment_to_dict(assignment: Any) -> Dict[str, Any]:
    """
    Convert an Assignment object to a dictionary with structured data.
    Handles null/missing fields using getattr with default None.
    Args:
        assignment (Any): A Canvas Assignment object.
    Returns:
        Dictionary with assignment details.
    """
    return {
        "id": getattr(assignment, "id", None),
        "name": getattr(assignment, "name", None),
        "description": getattr(assignment, "description", None),
        "created_at": getattr(assignment, "created_at", None),
        "updated_at": getattr(assignment, "updated_at", None),
        "due_at": getattr(assignment, "due_at", None),
        "lock_at": getattr(assignment, "lock_at", None),
        "unlock_at": getattr(assignment, "unlock_at", None),
        "has_overrides": getattr(assignment, "has_overrides", None),
        "all_dates": getattr(assignment, "all_dates", None),
        "course_id": getattr(assignment, "course_id", None),
        "html_url": getattr(assignment, "html_url", None),
        "submissions_download_url": getattr(
            assignment, "submissions_download_url", None
        ),
        "assignment_group_id": getattr(assignment, "assignment_group_id", None),
        "due_date_required": getattr(assignment, "due_date_required", None),
        "allowed_extensions": getattr(assignment, "allowed_extensions", None),
        "max_name_length": getattr(assignment, "max_name_length", None),
        "turnitin_enabled": getattr(assignment, "turnitin_enabled", None),
        "vericite_enabled": getattr(assignment, "vericite_enabled", None),
        "turnitin_settings": getattr(assignment, "turnitin_settings", None),
        "grade_group_students_individually": getattr(
            assignment, "grade_group_students_individually", None
        ),
        "external_tool_tag_attributes": getattr(
            assignment, "external_tool_tag_attributes", None
        ),
        "peer_reviews": getattr(assignment, "peer_reviews", None),
        "automatic_peer_reviews": getattr(assignment, "automatic_peer_reviews", None),
        "peer_review_count": getattr(assignment, "peer_review_count", None),
        "peer_reviews_assign_at": getattr(assignment, "peer_reviews_assign_at", None),
        "intra_group_peer_reviews": getattr(
            assignment, "intra_group_peer_reviews", None
        ),
        "group_category_id": getattr(assignment, "group_category_id", None),
        "needs_grading_count": getattr(assignment, "needs_grading_count", None),
        "needs_grading_count_by_section": getattr(
            assignment, "needs_grading_count_by_section", None
        ),
        "position": getattr(assignment, "position", None),
        "post_to_sis": getattr(assignment, "post_to_sis", None),
        "integration_id": getattr(assignment, "integration_id", None),
        "integration_data": getattr(assignment, "integration_data", None),
        "points_possible": getattr(assignment, "points_possible", None),
        "submission_types": getattr(assignment, "submission_types", None),
        "has_submitted_submissions": getattr(
            assignment, "has_submitted_submissions", None
        ),
        "grading_type": getattr(assignment, "grading_type", None),
        "grading_standard_id": getattr(assignment, "grading_standard_id", None),
        "published": getattr(assignment, "published", None),
        "unpublishable": getattr(assignment, "unpublishable", None),
        "only_visible_to_overrides": getattr(
            assignment, "only_visible_to_overrides", None
        ),
        "locked_for_user": getattr(assignment, "locked_for_user", None),
        "lock_info": getattr(assignment, "lock_info", None),
        "lock_explanation": getattr(assignment, "lock_explanation", None),
        "quiz_id": getattr(assignment, "quiz_id", None),
        "anonymous_submissions": getattr(assignment, "anonymous_submissions", None),
        "discussion_topic": getattr(assignment, "discussion_topic", None),
        "freeze_on_copy": getattr(assignment, "freeze_on_copy", None),
        "frozen": getattr(assignment, "frozen", None),
        "frozen_attributes": getattr(assignment, "frozen_attributes", None),
        "submission": getattr(assignment, "submission", None),
        "use_rubric_for_grading": getattr(assignment, "use_rubric_for_grading", None),
        "rubric_settings": getattr(assignment, "rubric_settings", None),
        "rubric": getattr(assignment, "rubric", None),
        "assignment_visibility": getattr(assignment, "assignment_visibility", None),
        "overrides": getattr(assignment, "overrides", None),
        "omit_from_final_grade": getattr(assignment, "omit_from_final_grade", None),
        "hide_in_gradebook": getattr(assignment, "hide_in_gradebook", None),
        "moderated_grading": getattr(assignment, "moderated_grading", None),
        "grader_count": getattr(assignment, "grader_count", None),
        "final_grader_id": getattr(assignment, "final_grader_id", None),
        "grader_comments_visible_to_graders": getattr(
            assignment, "grader_comments_visible_to_graders", None
        ),
        "graders_anonymous_to_graders": getattr(
            assignment, "graders_anonymous_to_graders", None
        ),
        "grader_names_visible_to_final_grader": getattr(
            assignment, "grader_names_visible_to_final_grader", None
        ),
        "anonymous_grading": getattr(assignment, "anonymous_grading", None),
        "allowed_attempts": getattr(assignment, "allowed_attempts", None),
        "post_manually": getattr(assignment, "post_manually", None),
        "score_statistics": getattr(assignment, "score_statistics", None),
        "can_submit": getattr(assignment, "can_submit", None),
        "ab_guid": getattr(assignment, "ab_guid", None),
        "annotatable_attachment_id": getattr(
            assignment, "annotatable_attachment_id", None
        ),
        "anonymize_students": getattr(assignment, "anonymize_students", None),
        "require_lockdown_browser": getattr(
            assignment, "require_lockdown_browser", None
        ),
        "important_dates": getattr(assignment, "important_dates", None),
        "muted": getattr(assignment, "muted", None),
        "anonymous_peer_reviews": getattr(assignment, "anonymous_peer_reviews", None),
        "anonymous_instructor_annotations": getattr(
            assignment, "anonymous_instructor_annotations", None
        ),
        "graded_submissions_exist": getattr(
            assignment, "graded_submissions_exist", None
        ),
        "is_quiz_assignment": getattr(assignment, "is_quiz_assignment", None),
        "in_closed_grading_period": getattr(
            assignment, "in_closed_grading_period", None
        ),
        "can_duplicate": getattr(assignment, "can_duplicate", None),
        "original_course_id": getattr(assignment, "original_course_id", None),
        "original_assignment_id": getattr(assignment, "original_assignment_id", None),
        "original_lti_resource_link_id": getattr(
            assignment, "original_lti_resource_link_id", None
        ),
        "original_assignment_name": getattr(
            assignment, "original_assignment_name", None
        ),
        "original_quiz_id": getattr(assignment, "original_quiz_id", None),
        "workflow_state": getattr(assignment, "workflow_state", None),
    }


# Standalone helper function to convert Assignment objects to dictionaries
def _assignment_to_dict(assignment: Any) -> Dict[str, Any]:
    """
    Convert an Assignment object to a dictionary with structured data.

    Args:
        assignment (Any): A Canvas Assignment object.

    Returns:
        Dictionary with assignment details.
    """
    return {
        "id": assignment.id,
        "name": assignment.name,
        # "description": assignment.description,
        "created_at": assignment.created_at,
        "updated_at": assignment.updated_at,
        "due_at": assignment.due_at,
    }


class Tools:
    class Valves(BaseModel):
        """Configuration for the Canvas API."""

        api_token: str = Field(default="NONE", description="Your CANVAS API token here")
        canvas_domain: str = Field(
            default="https://fhict.instructure.com",
            description="Your CANVAS DOMAIN address here",
        )

    def __init__(self):
        """Initialize the Canvas Course Maker tool."""
        self.valves = self.Valves()
        self.canvas = canvasapi.Canvas(
            "https://fhict.instructure.com",
            "2464~xTDWAKexVeazXxKJu2mFyhhNNmkca3Lm2GncGm8hM64aB6Ry6W23vTnRGeMVUtEn",
        )
        # self.canvas = canvasapi.Canvas(self.valves.canvas_domain, self.valves.api_token)
        self.citation = True

    # class Valves(BaseModel):
    #    """Configuration for the Canvas API."""
    #
    #    api_token: str = Field(default="", description="Your CANVAS API token here")
    #    canvas_domain: str = Field(
    #        default="", description="Your CANVAS DOMAIN address here"
    #    )

    def list_courses(self) -> List[Dict[str, Any]]:
        """
        Retrieve all courses the user has access to.

        Returns:
            List of Course objects (or PaginatedList from canvasapi)
        """
        courses = []
        for course in self.canvas.get_courses():
            courses.append({"name": course.name, "id": course.id})
        return courses

    def list_assignments(self, course_id: int) -> List[Dict[str, Any]]:
        """
        Retrieve all assignments for a specific course.

        Args:
            course_id (int): The ID of the course to fetch assignments from.

        Returns:
            List of dictionaries with assignment details.
        """
        try:
            course = self.canvas.get_course(course_id)
            assignments = course.get_assignments()
            return [_assignment_to_dict(assignment) for assignment in assignments]
        except Exception as e:
            return [{"error": f"Failed to fetch assignments: {str(e)}"}]

    def get_assignment_details(self, assignment_id: int) -> Dict[str, Any]:
        """
        Retrieve detailed assignment data by ID.
        Args:
            assignment_id (int): The ID of the assignment.
        Returns:
            Dictionary with all assignment details or error message.
        """
        try:
            assignment = self.canvas.get_assignment(assignment_id)
            return self._assignment_to_dict(assignment)
        except Exception as e:
            return {"error": f"Failed to fetch assignment details: {str(e)}"}

    def list_modules(self, course_id: int) -> List[Dict[str, Any]]:
        """
        Retrieve all modules for a specific course.
        Args:
            course_id (int): The ID of the course to fetch modules from.
        Returns:
            List of dictionaries with module details.
        """
        try:
            course = self.canvas.get_course(course_id)
            modules = course.get_modules()
            return [_module_to_dict(module) for module in modules]
        except Exception as e:
            return [{"error": f"Failed to fetch modules: {str(e)}"}]
