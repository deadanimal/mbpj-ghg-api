from datetime import datetime, timedelta

from django.conf import settings
from django.conf.urls import include, url
from django.contrib.gis import admin

from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from users.views import (
    MyTokenObtainPairView
)

class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass

router = NestedDefaultRouter()

from applications.views import (
    ApplicationViewSet,
    ApplicationAssessmentViewSet,
    AssessmentAspectViewSet,
    EvaluationViewSet,
    EvaluationScheduleViewSet,
    ApplicationEventViewSet
)

applications_router = router.register(
    'applications', ApplicationViewSet
)

application_assessments_router = router.register(
    'application-assessments', ApplicationAssessmentViewSet
)

assessment_aspects_router = router.register(
    'assessment-aspects', AssessmentAspectViewSet
)

evaluations_router = router.register(
    'evaluations', EvaluationViewSet
)

evaluation_schedules_router = router.register(
    'evaluation-schedules', EvaluationScheduleViewSet
)

application_events_router = router.register(
    'application-events', ApplicationEventViewSet
)

from faqs.views import (
    FaqViewSet
)

faqs_router = router.register(
    'faqs', FaqViewSet
)

from houses.views import (
    HouseViewSet,
    HouseEventViewSet
)

houses_router = router.register(
    'houses', HouseViewSet
)

house_events_router = router.register(
    'house-events', HouseEventViewSet
)


from medias.views import (
    MediaViewSet
)

medias_router = router.register(
    'medias', MediaViewSet
)

from organisations.views import (
    OrganisationViewSet,
    OrganisationTypeViewSet
)

organisations_router = router.register(
    'organisations', OrganisationViewSet
)

organisation_types_router = router.register(
    'organisation-types', OrganisationTypeViewSet
)


from rebates.views import (
    RebateViewSet      
)

rebates_router = router.register(
    'rebates', RebateViewSet
)

from reports.views import (
    ReportViewSet
)

reports_router = router.register(
    'reports', ReportViewSet
)

from tickets.views import (
    TicketAnswerViewSet,
    TicketQuestionViewSet,
    TicketEventViewSet
)

ticket_answers_router = router.register(
    'ticket-answers', TicketAnswerViewSet
)

ticket_questions_router = router.register(
    'ticket-questions', TicketQuestionViewSet
)

ticket_events_router = router.register(
    'ticket-events', TicketEventViewSet
)

from users.views import (
    CustomUserViewSet,
    UserOccupationViewSet,
    UserEventViewSet
)

users_router = router.register(
    'users', CustomUserViewSet
)

user_occupations_router = router.register(
    'user-occupations', UserOccupationViewSet
)

user_events_router = router.register(
    'user-events', UserEventViewSet
)


urlpatterns = [
    url(r'v1/', include(router.urls)),
    url(r'auth/', include('rest_auth.urls')),
    url(r'auth/registration/', include('rest_auth.registration.urls')),

    url('auth/obtain/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('auth/verify/', TokenVerifyView.as_view(), name='token_verify'),
]