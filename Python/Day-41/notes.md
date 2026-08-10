1. Dataclasses
Learn:
What is a dataclass?
Why dataclasses exist
@dataclass
Automatically generated methods
field()
Default values
default_factory
    - A dataclass is a class whose main job is to hold data, decorated with `@dataclass` from the `dataclasses` module so the boilerplate of a typical "data holder" class doesn't have to be written by hand. Without it, every such class needs a hand-written `__init__` that assigns each parameter to `self`, plus `__repr__` and `__eq__` if you want readable printing and value-based comparison - dataclasses exist to generate all of that automatically from the class body's type-annotated attributes. `@dataclass` inspects the annotated fields and generates `__init__`, `__repr__`, and `__eq__` (comparing all fields) automatically; other methods like `__lt__` can be added with `order=True`. `field()` customizes an individual attribute beyond a plain default - it can mark a field as excluded from `__repr__`/`__eq__`, or supply a factory for a default value. Default values work like normal parameter defaults (`cgpa: float = 0.0`), but a mutable default (a list or dict) can't be written directly as `= []` because it would be shared across all instances - `default_factory` (via `field(default_factory=list)`) tells the dataclass to call a zero-argument function to produce a fresh object per instance instead.

2. Enums
Understand:
What is an Enum?
Why enums exist
Enum
auto()
Iterating through enums
Comparing enum values
    - An `Enum` (enumeration) is a class that defines a fixed, named set of constant values, imported from the `enum` module and created by subclassing `Enum`. Enums exist to replace "magic strings" or magic numbers (e.g. `status = "shipped"`) with named, type-checked constants (`status = OrderStatus.SHIPPED`) - this catches typos at development time instead of silently comparing against a misspelled string at runtime, and makes the set of valid values self-documenting. Each member has a `.name` (the identifier, e.g. `"SHIPPED"`) and a `.value` (the underlying value assigned to it); `auto()` lets Python assign the value automatically (starting at 1, incrementing) when the specific number/string doesn't matter, only that each member is distinct. Enum classes are iterable - `for status in OrderStatus:` walks every member in definition order - and members compare by identity/equality (`OrderStatus.PENDING == OrderStatus.PENDING` is `True`, and different members are never equal to each other or to a plain string with the same text).

3. Type Hints
Study:
Why type hints exist
Function annotations
Variable annotations
Return types
Optional
List
Dict
Tuple
Any
    - Type hints are optional annotations that document the expected types of variables, function parameters, and return values, introduced to make code easier to read and to let external tools catch type-related bugs before the code ever runs. A function annotation looks like `def add(a: int, b: int) -> int:` - `a: int` and `b: int` document the parameter types, and `-> int` documents the return type. Variable annotations follow the same `name: type` pattern (`total: float = 0.0`). From `typing`, `List[int]` documents a list of ints, `Dict[int, str]` a dict mapping int keys to str values, `Tuple[int, int]` a fixed-size tuple of two ints, `Optional[str]` a value that is either `str` or `None` (shorthand for `Union[str, None]`), and `Any` opts a value out of type checking entirely when its type is genuinely unconstrained.
4. Static Type Checking
Learn:
What is static analysis?
Introduction to mypy
Benefits of type checking
(No installation required today.)
    - Static analysis examines source code without executing it, looking for issues that would otherwise only surface at runtime. `mypy` is Python's most widely used static type checker: it reads a file's type hints and flags any place a value's type doesn't match what a hint promises (e.g. passing a `str` to a parameter annotated `int`), run from the command line as `mypy filename.py`. The benefit is catching a whole class of bugs - wrong argument types, `None` used where a non-optional value was expected, mismatched return types - at review/CI time instead of as a production traceback, without changing how the program behaves at runtime.

5. Best Practices
Understand:
Use dataclasses for data models.
Use enums instead of magic strings.
Add type hints to public functions.
Type hints improve readability but do not enforce types at runtime.
    - Data models (records with named fields and no real behavior beyond holding values) should be dataclasses rather than hand-written classes - less boilerplate, and `__repr__`/`__eq__` come for free. Fixed sets of named options (statuses, categories, directions) should be enums instead of raw strings - a typo in an enum member name is caught immediately (`AttributeError`), while a typo in a string literal (`"Shiped"`) fails silently. Public functions - the ones other modules or people call - should carry type hints even if internal helper functions don't, since the signature is the first thing a caller reads to understand how to use it. It's worth remembering that Python's type hints are purely documentation and static-analysis input: nothing stops `add("a", "b")` from being called at runtime even though both parameters are annotated `int` - hints help humans and tools like mypy, they don't enforce anything while the program is running.
