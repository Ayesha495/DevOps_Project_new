from django.db import models


class Calculator(models.Model):
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"

    OPERATION_CHOICES = [
        (ADD, "Add"),
        (SUBTRACT, "Subtract"),
        (MULTIPLY, "Multiply"),
        (DIVIDE, "Divide"),
    ]

    num1 = models.FloatField()
    num2 = models.FloatField()
    operation = models.CharField(max_length=10, choices=OPERATION_CHOICES)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.num1} {self.operation} {self.num2} = {self.result}"
