


from django.urls import path, re_path
from apps.dashboard import views as DashboardView

urlpatterns = [
    # The home page
    #path(r'^', DashboardView.index, name = 'index'),
    re_path(r'^dashboard/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', DashboardView.DashboardView.as_view(), name='dashboard'),
    #re_path(r'^.*\.*', DashboardView.pages, name='pages'),
]

