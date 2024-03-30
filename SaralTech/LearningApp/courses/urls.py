from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, ModuleViewSet, SectionViewSet, AnswerViewSet,VideoViewSet, AssignmentViewSet, QuestionViewSet, TestViewSet, TestQuestionViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'tests', TestViewSet)
router.register(r'testquestions', TestQuestionViewSet)
router.register(r'answers', AnswerViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
