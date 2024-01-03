Feature: Task Management

  Scenario: Adding a task
    Given an empty task list
    When a task named "<task_name>" is added
    Then the task list should contain "<task_name>"

  Scenario: Listing all tasks
    Given a task list with tasks:
      | Task Name   |
      | Task 1       |
      | Task 2       |
    When I list all tasks
    Then I should see the following tasks in the list:
      | Task Name   |
      | Task 1       |
      | Task 2       |

  Scenario: Marking a task as completed
    Given a task list with tasks:
      | Task Name   |
      | Task 1       |
    When I mark task "<task_name>" as completed
    Then the status of task "<task_name>" should be "Completed"

  Scenario: Clearing completed tasks
    Given a task list with tasks:
      | Task Name   | Status      |
      | Task 1       | Completed   |
      | Task 2       | Pending     |
    When I clear completed tasks
    Then the task list should only contain tasks with status "Pending"

  Scenario: Clearing all tasks
    Given a task list with tasks:
      | Task Name   |
      | Task 1       |
      | Task 2       |
    When I clear all tasks
    Then the task list should be empty

  Scenario: Marking all tasks as completed
    Given a task list with tasks:
      | Task Name   | Status      |
      | Task 1       | Pending     |
      | Task 2       | Pending     |
    When I mark all tasks as completed
    Then all tasks in the list should have status "Completed"
