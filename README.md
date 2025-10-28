# Ape

Algebraic Python Enums

Create Python enums with differently sized variants and transparently
relay type information to the language server using the `@AlgebraicEnum` decorator.

## Example

Here's an example inspired by the one from [Rust By Example](https://doc.rust-lang.org/rust-by-example/custom_types/enum.html).

```python
from ape import AlgebraicEnum
from dataclasses import dataclass


@AlgebraicEnum
class WebEvent:

    # empty unit-like variants
    @dataclass
    class PageLoad:
      pass

    @dataclass
    class Keypress:
      key: str

    @dataclass
    class Click:
      x: int
      y: int
```

Also check out the [IP address example](./examples/ip_address.py).

## Design decisions
- All variants must be dataclasses, use the `@dataclass` decorator.
- Implementing static or class methods on variants is disallowed.
- Users should use `match..case` pattern to match enum variants and implement methods on the base enum class.

