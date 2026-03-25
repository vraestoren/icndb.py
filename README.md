# <img src="https://services.garmin.com/appsLibraryBusinessServices_v0/rest/apps/c7c2f609-3290-417a-a2b3-30b80ef78f2a/icon/1ee1fcf3-7e16-4bb0-b949-0418df7378ec" width="28" style="vertical-align:middle;" /> icndb.py

> Web-API for [ICNDB](https://www.icndb.com) the Internet Chuck Norris Database, serving thousands of Chuck Norris jokes with category filters and custom name support.

## Quick Start
```python
from icndb import IcnDb

icndb = IcnDb()

# Get a random joke
joke = icndb.get_random_joke()["value"]["joke"]
print(joke)
```

---

## Methods

| Method | Description |
|--------|-------------|
| `get_random_joke(count, first_name, last_name, limit_to, exclude)` | Get one or more random jokes |
| `get_specific_joke(joke_id)` | Get a joke by ID |
| `get_jokes_count()` | Get total number of jokes |
| `get_joke_categories()` | Get all available categories |
| `get_all_jokes()` | Get every joke in the database |

---

## Examples
```python
icndb = ICNDB()

# Get 5 random jokes
icndb.get_random_joke(count=5)

# Customize the name
icndb.get_random_joke(first_name="John", last_name="Doe")

# Filter by category
icndb.get_random_joke(limit_to="explicit")

# Exclude a category
icndb.get_random_joke(exclude="explicit")

# Get a specific joke
icndb.get_specific_joke(joke_id=42)

# Total joke count
print(icndb.get_jokes_count()["value"])
```

---

## Categories

| Category | Description |
|----------|-------------|
| `nerdy` | Tech and science jokes (default) |
| `explicit` | Adult jokes |
