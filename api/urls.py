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

from organisations.views import (
    OrganisationViewSet,
    OrganisationTypeViewSet
)

from users.views import (
    CustomUserViewSet,
    UserOccupationViewSet
)

class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass

router = NestedDefaultRouter()

organisations_router = router.register(
    'organisations', OrganisationViewSet
)

organisation_types_router = router.register(
    'organisation-types', OrganisationTypeViewSet
)

users_router = router.register(
    'users', CustomUserViewSet
)

user_occupations_router = router.register(
    'user-occupations', UserOccupationViewSet
)

from applications.views import (
    ApplicationViewSet,
    ApplicationAssessmentViewSet,
    ApplicationEvaluationViewSet,
    ApplicationEvaluationAssessmentViewSet,
    ApplicationEvaluationScheduleViewSet
)

applications_router = router.register(
    'applications', ApplicationViewSet
)

application_assessments_router = router.register(
    'application-assessments', ApplicationAssessmentViewSet
)

application_evaluations_router = router.register(
    'application-evaluations', ApplicationEvaluationViewSet
)

application_evaluation_assessments_router = router.register(
    'application-evaluation-assessments', ApplicationEvaluationAssessmentViewSet
)

application_evaluation_schedules_router = router.register(
    'application-evaluation-schedules', ApplicationEvaluationScheduleViewSet
)

from houses.views import (
    HouseViewSet
)

houses_router = router.register(
    'houses', HouseViewSet
)

from rebates.views import (
    RebateViewSet      
)

rebates_router = router.register(
    'rebates', RebateViewSet
)

urlpatterns = [

    url(r'v1/', include(router.urls)),
    url(r'auth/', include('rest_auth.urls')),
    url(r'auth/registration/', include('rest_auth.registration.urls')),

    url('auth/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]