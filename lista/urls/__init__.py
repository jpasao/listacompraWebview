from .ingredient_urls import ingredient_urlpatterns
from .meal_urls import meal_urlpatterns
from .other_urls import other_urlpatterns

urlpatterns = ingredient_urlpatterns + meal_urlpatterns + other_urlpatterns