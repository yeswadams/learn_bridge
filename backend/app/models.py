# Import every model so SQLAlchemy registers them
# with the same declarative registry.

from app.features.auth.models import User
from app.features.categories.models import Category
from app.features.courses.models import Course
from app.features.lessons.models import Lesson
from app.features.enrollments.models import Enrollment
from app.features.progress.models import Progress
from app.features.quiz.models import Quiz
from app.features.certificates.models import Certificate