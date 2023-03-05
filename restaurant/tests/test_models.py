from django.test import TestCase
from django.utils import timezone
from restaurant import models


class BookModelTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_create_book(self):
        book = models.Booking(
            name="jhon",
            no_of_guests=2,
            booking_date=timezone.now(),
        )
        book.save()
        book_count = models.Booking.objects.count()
        self.assertEqual(book_count, 1)
