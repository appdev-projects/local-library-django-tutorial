# local-library-tutorial

This is a companion repository to [Mozilla's Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django).

## Introduction to Django

From: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction

## About Django

- Python
- High-level web framework
- Rapid development
- Secure
- Maintainable
- Scalable
- Free and open source
- Batteries included
- Somewhat opinionated

## Model View Template

Django uses the Model View Template (MVT) architecture, similar to the Model View Controller architecture.

## URL mapper

- User requests go to `urls.py`, which maps the request to a view.

## View

- The request handler function in `views.py` processes the request and may interact with models.
- Django views are similar to controllers and actions in Rails.

## Models

- Python objects that model data
- Provides an API to interact with the database

## Templates

- Define the structure of any type of file
- Placeholders populated with data from a model
- Renders HTML and other file types
- The rendered template is sent back as the response to the user.
