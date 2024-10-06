# trace
A decorator to trace function calls and returns, suitable for educational use in a CS-1 course.

This repo contains just a single module, `tracer.py`, which students can copy into their projects.

Usage: 

```python
from tracer import trace

@trace()
def my_recursive_function(m, n):
      ...
```

Calls and returns of my_recursive_function will be written to the standard error stream.

Example: 
```python
@trace()
def fib(m: int) -> int:
    if m > 1:
        return fib(m-1) + fib(m-2)
    else:
        return m
```

prints on sys.stderr: 

```text
fib(4)
├───fib(3)
│   ├───fib(2)
│   │   ├───fib(1)
│   │   │   1
│   │   ├───fib(0)
│   │   │   0
│   │   1
│   ├───fib(1)
│   │   1
│   2
├───fib(2)
│   ├───fib(1)
│   │   1
│   ├───fib(0)
│   │   0
│   1
3
```

Limitations:  Intended for classroom use, not for professional developers. 
Traces only decorated functions, not everything called by them (unless those functions are
also decorated).
Not suitable for multi-threaded programs or anything else without a simple
call-return structure on a single stack.  For example, may be a mess with generators.
   
