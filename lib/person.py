#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    pass
    def __init__(self, name, job):
        self.name = name
        self.job = job
        self._name = None
        self._job = None

    def name(self):
        return self._name

    def name(self, value):
        if type(value) is not str or not (1 <= len(value) <= 25):
            print("Name must be a string under 25 characters.")
        else:
            self._name = value.title()      # title case.

    def job(self):
        return self._job

    def job(self, value):
        if value not in APPROVED_JOBS:
            print("Job must be in the list of approved jobs.")
        else:
            self._job = value

person_instance = Person(name="john doe", job="Admin")
print(person_instance.name)