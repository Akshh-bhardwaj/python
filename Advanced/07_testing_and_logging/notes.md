# Topic 7: Testing, Logging & Exception Handling in Python

Writing production-grade Python code requires a solid strategy for error reporting, validation, diagnostic logs, and test verification.

---

## 1. Advanced Unit Testing & Mocking

Python's standard library provides the `unittest` framework, while the community widely uses `pytest`.

### Mocking (`unittest.mock`)
Mocking allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.
- `Mock`: A flexible mock object.
- `MagicMock`: A subclass of `Mock` that implements all default magic methods.
- `patch`: A decorator or context manager that temporarily replaces a module or class attribute with a mock.

```python
from unittest.mock import patch

@patch('requests.get')
def test_api_call(mock_get):
    mock_get.return_value.status_code = 200
```

---

## 2. Structured Logging

Never use `print()` statements for diagnostic information in production. Instead, use Python's built-in `logging` module.

### Core Logger Components:
1. **Logger**: Exposes the interface that application code directly calls.
2. **Handler**: Sends the log records (created by loggers) to the appropriate destination (Console, File, Socket).
3. **Formatter**: Specifies the layout/format of the output log records.
4. **Filter**: Provides fine-grained control to determine which log records to output.

### Log Levels:
- `DEBUG`: Detailed information (diagnostic).
- `INFO`: Confirmation that things are working as expected.
- `WARNING`: An indication that something unexpected happened (default level).
- `ERROR`: A serious problem (software was unable to perform some function).
- `CRITICAL`: A serious error, indicating that the program itself may be unable to continue running.

---

## 3. Advanced Exceptions

Python permits designing custom exception hierarchies to cleanly segment domain-specific errors.

- Inherit custom exceptions from `Exception` (not `BaseException`).
- Implement the `__str__` method to provide useful context.
- Use **Exception Chaining** (`raise ... from ...`) to preserve stack traces when re-raising wrapped exceptions.

```python
class DatabaseError(Exception):
    """Custom exception class for Database operations."""
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code
```
