from behave import given, when, then
from todo_list import *

@given('an empty task list')
def empty_task_list(context):
    tasks_list.clear()

@given('a task list with tasks:')
def task_list_with_tasks(context):
    for row in context.table:
        task_name = row['Task Name']
        task = Task(task_name)
        tasks_list.append(task)

@when('a task named "{task_name}" is added')
def add_task(context, task_name):
    add_task(task_name)

@when('I list all tasks')
def list_all_tasks(context):
    list_all_task()

@when('I mark task "{task_name}" as completed')
def mark_task_as_completed(context, task_name):
    task = find_task_by_name(task_name)
    mark_completed(task)

@when('I clear completed tasks')
def clear_completed_tasks(context):
    clear_completed()

@when('I clear all tasks')
def clear_all_tasks(context):
    clear_all_task()

@when('I mark all tasks as completed')
def mark_all_tasks_as_completed(context):
    mark_all_completed()

@then('the task list should contain "{task_name}"')
def assert_task_in_list(context, task_name):
    task = find_task_by_name(task_name)
    assert task is not None, f'Task "{task_name}" not found in the list'

@then('I should see the following tasks in the list:')
def assert_tasks_in_list(context):
    expected_tasks = [row['Task Name'] for row in context.table]
    actual_tasks = [task.nombre for task in tasks_list]
    assert actual_tasks == expected_tasks, f'Expected tasks: {expected_tasks}, Actual tasks: {actual_tasks}'

@then('the status of task "{task_name}" should be "{status}"')
def assert_task_status(context, task_name, status):
    task = find_task_by_name(task_name)
    assert task is not None, f'Task "{task_name}" not found in the list'
    assert task.estado == status, f'Expected status: {status}, Actual status: {task.estado}'

@then('the task list should only contain tasks with status "{status}"')
def assert_tasks_with_status(context, status):
    for task in tasks_list:
        assert task.estado == status, f'Task "{task.nombre}" has unexpected status: {task.estado}'

@then('the task list should be empty')
def assert_empty_task_list(context):
    assert not tasks_list, 'Task list is not empty'

@then('all tasks in the list should have status "{status}"')
def assert_all_tasks_status(context, status):
    for task in tasks_list:
        assert task.estado == status, f'Task "{task.nombre}" has unexpected status: {task.estado}'

def find_task_by_name(task_name):
    for task in tasks_list:
        if task.nombre == task_name:
            return task
    return None
