# Ape

Algebraic Python Enums

Create Python enums with differently sized variants and transparently
relay type information to the language server using the `@AlgebraicEnum` macro.

## Design decisions
- All variants must be dataclasses, use the `@dataclass` decorator.
- Implementing static or class methods on variants is disallowed.
- Users should use `match..case` pattern to match enum variants and implement methods on the base enum class.

Check out the [IP address example](./examples/ip_address.py).
