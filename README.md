# calcPy
Python api rest calculator project.

This calculator has Add, Subtract, Divide and Multiply functions, and is called by an API REST using JSON.

Example JSON POST:

{
    "operation": "add",
    "n1": "1",
    "n2": "5"
}

Endpoint:
http://localhost:4000/calculator

Operation codes:
"add", "subtract", "divide", "multiply"