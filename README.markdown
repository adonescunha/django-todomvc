# django-todomvc
[![PyPI version](https://badge.fury.io/py/django-todomvc.svg)](https://badge.fury.io/py/django-todomvc)
[![Build Status](https://travis-ci.org/adonescunha/django-todomvc.svg?branch=master)](https://travis-ci.org/adonescunha/django-todomvc) [![Coverage Status](https://coveralls.io/repos/adonescunha/django-todomvc/badge.svg?branch=master&service=github)](https://coveralls.io/github/adonescunha/django-todomvc?branch=master)
[![Requirements Status](https://requires.io/github/adonescunha/django-todomvc/requirements.svg?branch=master)](https://requires.io/github/adonescunha/django-todomvc/requirements/?branch=master)

[TodoMVC](http://todomvc.com/) backend built as a Django app.

## Installation

Install `todomvc` via `pip`:

```
$ pip install django-todomvc
```

Add `todomvc` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    # Other apps
    'todomvc'
)
```

At least, include `todomvc` URLs:

```python
# urls.py

urlpatterns = patterns(
    '',
    # Other patterns
    (r'^/todo', include('todomvc.urls'))
)
```

## Endpoints

### `GET /tasks/`

Lists tasks already created.

#### Response

```
Status: 200 OK

[
  {
    "id": 1,
    "title": "Buy groceries",
    "completed": false
  },
  {
    "id": 2,
    "title": "Do laundry",
    "completed": true
  }
]
```

### `POST /tasks/`

Creates a new task.

#### Request

```
{
  "title": "Buy groceries"
}
```

#### Response

```
Status: 201 Created

{
  "id": 1,
  "title": "Buy groceries",
  "completed": false
}
```

### `GET /tasks/:id/`

Retrieves a task.

#### Response

```
Status: 200 OK

{
  "id": 1,
  "title": "Buy groceries",
  "completed": false
}
```

### `PUT /tasks/:id/`

Allows a full update of a task. Both `title` and `completed` arguments must be provided.

#### Request

```
{
  "title": "Buy groceries",
  "completed": true
}
```

#### Response

```
Status: 200 OK

{
  "id": 1,
  "title": "Buy groceries",
  "completed": true
}
```

### `PATCH /tasks/:id/`

Allows a partial update of a task.

#### Request

```
{
  "completed": true
}
```

#### Response

```
Status: 200 OK

{
  "id": 1,
  "title": "Buy groceries",
  "completed": true
}
```

### `DELETE /tasks/:id/`

Removes a task.

#### Response

```
Status: 204 No content
```

## MIT Licensed

See the [LICENSE file](LICENSE) for details.

-----
[Adones Cunha](http://github.com/adonescunha)
