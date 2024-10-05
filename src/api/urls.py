from django.urls import include, path

from apps.catalogue.urls import router as catalogue_router
from apps.feedback.urls import router as feedback_router
from apps.portfolio.urls import router as portfolio_router
from apps.settings.urls import router as settings_router
from apps.partials.urls import router as partials_router

urlpatterns = [
    path(r"catalogue/", include(catalogue_router.urls)),
    path(r"feedback/", include(feedback_router.urls)),
    path(r"portfolio/", include(portfolio_router.urls)),
    path(r"settings/", include(settings_router.urls)),
    path(r"partials/", include(partials_router.urls)),
]
