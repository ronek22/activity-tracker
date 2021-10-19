# Create your tests here.
import datetime

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from activity.models import Activity

User = get_user_model()

users = [
    {"username": "test1", "email": "test1@test.com", "password": "testPass12"},
    {"username": "test2", "email": "test2@test.com", "password": "testPass12"},
]


class ActivityViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.first_user = User.objects.create_user(**users[0])
        self.second_user = User.objects.create_user(**users[1])
        self.example_activity = Activity.objects.create(type="Running", effort="Easy", name="Example Run",
                                                        duration=datetime.timedelta(minutes=40),
                                                        distance=10, user=self.first_user)

    def test_list_activities_first_user_should_return_one_activity(self):
        self.client.login(**users[0])
        response = self.client.get(reverse("activity:list"))
        self.assertEquals(response.context_data["object_list"].count(), 1)

    def test_list_activities_second_user_should_return_none_activity(self):
        self.client.login(**users[1])
        response = self.client.get(reverse("activity:list"))
        self.assertEquals(response.context_data["object_list"].count(), 0)

    def test_create_view(self):
        self.client.login(**users[1])
        response = self.client.post(reverse("activity:create"),
                                    {"type":     "Running", "effort": "Easy", "name": "Test run", "duration": "00:15:00",
                                     "distance": 5})

        from_db: Activity = Activity.objects.last()
        self.assertEquals(response.status_code, 302)
        self.assertEquals(reverse("activity:detail", args=[from_db.id]), response.url)
        self.assertEquals(from_db.name, "Test run")
        self.assertEquals(from_db.distance, 5)

    def test_detail_view(self):
        activity = Activity.objects.create(type="Cycling", effort="Moderate", name="Hard Cycling",
                                           duration=datetime.timedelta(hours=3, minutes=40),
                                           distance=140, user=self.first_user)
        self.client.login(**users[1])
        response = self.client.get(reverse("activity:detail", args=[activity.id]))
        response_activity: Activity = response.context_data["object"]

        self.assertEquals(response_activity.name, "Hard Cycling")
        self.assertEquals(response_activity.distance, 140)
