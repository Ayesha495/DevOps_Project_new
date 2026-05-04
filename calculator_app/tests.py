from django.test import TestCase
from django.urls import reverse

from .models import Calculator


class CalculatorViewTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Calculator")

    def test_addition_is_saved_to_database(self):
        response = self.client.post(
            reverse("home"),
            {"num1": "8", "num2": "4", "operation": Calculator.ADD},
        )

        self.assertEqual(response.status_code, 200)
        calculation = Calculator.objects.get()
        self.assertEqual(calculation.result, 12)
        self.assertContains(response, "12.000000")

    def test_division_by_zero_is_not_saved(self):
        response = self.client.post(
            reverse("home"),
            {"num1": "8", "num2": "0", "operation": Calculator.DIVIDE},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Division by zero is not allowed.")
        self.assertEqual(Calculator.objects.count(), 0)
