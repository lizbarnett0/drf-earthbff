from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet, basename='quiz')
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'responses', ResponseViewSet, basename='response')
router.register(r'quiztakers', QuizTakerViewSet, basename='quiztaker')
router.register(r'usersresponses', UsersResponseViewSet, basename='usersresponse')
urlpatterns = router.urls
