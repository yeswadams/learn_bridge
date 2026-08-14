from typing import List, Optional, Dict, Any
from enum import Enum

class Role(str, Enum):
    INSTRUCTOR = "instructor"
    STUDENT = "student"
    ADMIN = "admin"

class CourseService:
    def __init__(self, db_session, course_repository):
        """Inject the db session and repo to keep methods testable"""
        self.db = db_session
        self.repo = course_repository

    def create_course(self, instructor_user: Any, course_data: Dict[str, Any]) -> Dict[str, Any]:
        """Creates a new course draft. Verifies the user has instructor role"""
        if getattr(instructor_user, "role", None) != Role.ADMIN:
            raise UnauthorizedCourseActionError("Only Admin can create course.")

        course_payload ={
            "title": course_data['title'],
            "description": course_data.get("description", ""),
            "instructor_id": instructor_user.id,
            "is_published": False   
        }

        course = self.repo.create(course_payload)
        self.db.commit()
        return course

    def get_course_by_id(self, course_id: int) -> Dict[str, Any]:
        """Fetches a single course by ID or raises an error if missing"""
        course = self.repo.find_by_id(course_id)
        if not course:
            raise CourseNotFoundError(f"Course with ID {course_id} does not exist.")

        return course

    def get_instructor_courses(self, instructor_id: int) -> List[Dict[str, Any]]:
        """Retrive all courses created by a specific instructor"""

        return self.repo.find_by_instructor(instructor_id)

    def update_course(
            self,
            course_id: int,
            current_user: Any,
            update_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Updates course details after ensuring the current user us the course owner
        """
        course = self.get_course_by_id(course_id)

        if course["instructor_id"] != current_user.id:
            raise UnauthorizedCourseActionError("You do not have persmission to modify this course")

        self.update_course = self.repo.update(course_id, update_data)
        self.db.commit()
        return self.update_course

    def publish_course(self, course_id: int, current_user: Any) -> Dict[str, Any]:
        """Publish a course draft to make it live for students"""

        return self.update_course(
            course_id=course_id,
            current_user=current_user,
            update_data={"is_publisjhed": True}
        )
            