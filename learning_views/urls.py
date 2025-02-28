from django.urls import path

# FBV (Function-Based Views)
from learning_views.views.fn_index import index
from learning_views.views.fn_list_test import list_tests
from learning_views.views.fn_retrive_test import retrive_test
from learning_views.views.fn_create_test import create_test
from learning_views.views.fn_update_test import update_test
from learning_views.views.fn_delete_test import delete_test

# usually CBV — Class-Based Views
from learning_views.views.view_index import MyView
from learning_views.views.usu_list_view_tests import ListTestsView1
from learning_views.views.usu_retrieve_view_test import RetriveTestView1
from learning_views.views.usu_create_test import CreateTestView1
from learning_views.views.usu_update_test import UpdateTestView1
from learning_views.views.usu_delete_test import DeleteTestView1


from learning_views.views.list_view_index import ListTestsView
from learning_views.views.retrieve_view_test import RetrieveTestView
from learning_views.views.create_view_test import CreateTestView
from learning_views.views.update_view_test import UpdateTestView
from learning_views.views.delete_view_test import DeleteTestView

urlpatterns = [
    # FBV (Function-Based Views)
    path("st_fun_home/", index, name="fn_index"),
    path("fn_list_test/", list_tests, name="fn_list"),
    path("fn_retrive_test/<slug:slug>/", retrive_test, name="fn_test"),
    path("fn_create/", create_test, name="create_test"),
    path("fn_update/<slug:slug>/", update_test, name="fn_update"),
    path("fn_delete_test/<slug:slug>/", delete_test, name="delete"),


    # usually CBV — Class-Based Views
    path("view_index/", MyView.as_view(), name="view_index"),
    path("usu_list_tests/", ListTestsView1.as_view(), name="usu_list"),
    path("usu_retrieve_test/<slug:slug>/", RetriveTestView1.as_view(), name="usu_retrive"),
    path("usu_create_test/", CreateTestView1.as_view(), name="usu_create"),
    path("usu_update_test/<slug:slug>/", UpdateTestView1.as_view(), name="usu_update"),
    path("usu_delete_test/<slug:slug>/", DeleteTestView1.as_view(), name="usu_delete"),


    # generic
    path("generic_index/", ListTestsView.as_view(), name="generic_index"),
    path("retrievetestview/<slug:slug>/", RetrieveTestView.as_view(), name="retrieve_test_view"),
    path("createtestview/", CreateTestView.as_view(), name="create_test_view"),
    path("test/<slug:slug>/update/", UpdateTestView.as_view(), name="update_test"),
    path("test/<slug:slug>/delete/", DeleteTestView.as_view(), name="delete_test"),
]