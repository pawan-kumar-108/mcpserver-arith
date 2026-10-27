from fastmcp import FastMCP

mcp = FastMCP("myArithmetic Server")


def _as_number(x):
    if isinstance(x, (int, float)):
        return x

    if isinstance(x, str):
        return float(x.strip())

    raise TypeError("Expected a number or numeric string")


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return _as_number(a) + _as_number(b)


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return _as_number(a) - _as_number(b)


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return _as_number(a) * _as_number(b)


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b."""
    a = _as_number(a)
    b = _as_number(b)

    if b == 0:
        raise ValueError("Division by zero is not allowed.")

    return a / b


@mcp.tool()
def power(a: float, b: float) -> float:
    """Raise a to the power b."""
    return _as_number(a) ** _as_number(b)


@mcp.tool()
def modulus(a: float, b: float) -> float:
    """Calculate the remainder when a is divided by b."""
    a = _as_number(a)
    b = _as_number(b)

    if b == 0:
        raise ValueError("Modulus by zero is not allowed.")

    return a % b