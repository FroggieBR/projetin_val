from rest_framework.routers import DefaultRouter
from .views import PlayerViewSet, TeamViewSet, TournamentViewSet

router = DefaultRouter()
router.register(r'player', PlayerViewSet, 'player')
router.register(r'team', TeamViewSet, 'team')
router.register(r'tournament', TournamentViewSet, 'tournament')

urlpatterns = router.urls
