from django.shortcuts import render
from django.http import HttpResponse

from .models import Calculator


OPERATORS = {
    Calculator.ADD: "+",
    Calculator.SUBTRACT: "-",
    Calculator.MULTIPLY: "x",
    Calculator.DIVIDE: "/",
}


def home(request):
    result = None
    error = None
    selected_operation = Calculator.ADD
    num1 = ""
    num2 = ""

    if request.method == "POST":
        num1 = request.POST.get("num1", "").strip()
        num2 = request.POST.get("num2", "").strip()
        selected_operation = request.POST.get("operation", Calculator.ADD)

        try:
            first_number = float(num1)
            second_number = float(num2)

            if selected_operation == Calculator.ADD:
                result = first_number + second_number
            elif selected_operation == Calculator.SUBTRACT:
                result = first_number - second_number
            elif selected_operation == Calculator.MULTIPLY:
                result = first_number * second_number
            elif selected_operation == Calculator.DIVIDE:
                if second_number == 0:
                    raise ZeroDivisionError
                result = first_number / second_number
            else:
                error = "Choose a valid operation."

            if error is None:
                Calculator.objects.create(
                    num1=first_number,
                    num2=second_number,
                    operation=selected_operation,
                    result=result,
                )
        except ValueError:
            error = "Enter valid numbers in both fields."
        except ZeroDivisionError:
            error = "Division by zero is not allowed."

    history = Calculator.objects.all()[:8]
    return render(
        request,
        "calculator_app/home.html",
        {
            "error": error,
            "history": history,
            "num1": num1,
            "num2": num2,
            "operations": Calculator.OPERATION_CHOICES,
            "operators": OPERATORS,
            "result": result,
            "selected_operation": selected_operation,
        },
    )


def bug(request):
    #BUG ALERT: the line below should be return HttpResponse("this is not a buggy code.")
    return HttpResponse("This is not a buggy code")

def enhancement(request):
    return HttpResponse("This is an enhancement code added by Jannat.")
