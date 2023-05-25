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

# Define a name property for your Person class. 
# The name must be of type str and between 1 and 25 characters. The name should be converted to title case before it is saved.
# If the name is invalid, the setter method should print() "Name must be string between 1 and 25 characters."


# Define a job property for your Person class.
# If the job is invalid, the setter method should print() 
# "Job must be in list of approved jobs." The job must be in the following list of APPROVED_JOBS
class Person:
    
    def __init__(self, name="Human Name", job="student"):
        self.name = name
        self.job = job

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if (isinstance(name, str)) and 0 <= len(name) <= 120:
            # name.title()
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_job(self):
        return self._job
    
    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")
    
    name = property(get_name, set_name)
    job = property(get_job, set_job)

elise = Person("elise", "makeup job")
#did not print anything because correct
# Job must be in list of approved jobs.

print(elise.name)
# Elise

chloe = Person
