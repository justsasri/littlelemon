from rest_framework.test import APILiveServerTestCase
from django.contrib.auth import get_user_model


class CommunitiesApiClubTest(APILiveServerTestCase):
    BASE_URL = "/api"

    def setUp(self) -> None:
        User = get_user_model()
        self.user = User.objects.create_user(
            username="test",
            email="test@yopmail.com",
            password="testpassword",
        )
        self.user.save()

    def test_menu_list(self):
        self.client.force_login(self.user)
        resp = self.client.get(self.BASE_URL + "/menu/")
        self.assertEqual(resp.status_code, 200)
