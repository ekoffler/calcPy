# calcPy
Python api rest calculator project.

This calculator has Add, Subtract, Divide and Multiply functions, and is called by an API REST using JSON.

Example JSON POST:

{
    "operation": "plus",
    "n1": "1",
    "n2": "5"
}

Endpoint:
http://localhost:8000/calculator

Operation codes:
"plus", "minus", "div", "mul"