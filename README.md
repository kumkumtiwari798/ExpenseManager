# Expense Management System
ExpenseManager is an application built on the Frappe framework to streamline the management of employee expenses within an organization. It allows employees to submit expense claims, managers to review them, and provides role-based permissions for efficient workflow.

## Features
  Expense Claim DocType: Captures essential details for each expense claim, including:
    Employee: The name of the employee submitting the claim.
    Expense Type: Type of expense (e.g., travel, meals).
    Date: Date of the expense.
    Amount: Amount for the claim.

## Approval Workflow:
    Employees submit claims, which start with a "Submitted" status.
    Managers review claims, updating the status to "Under Review".
    Managers can either approve or reject claims, setting the final status to "Approved" or "Rejected".

## Role-Based Permissions:
    Employees can only submit claims.
    Managers have access to review, approve, or reject claims.

## Installation
  Clone the repository from GitHub:
    git clone https://github.com/yourusername/ExpenseManager.git

  Navigate to the cloned directory:
    cd ExpenseManager

  Install the app in your Frappe site:
    bench --site your-site-name install-app ExpenseManager

## Start the Frappe server:
  bench start

## Usage
  Submit an Expense Claim: Employees can submit a new expense claim through the Expense Claim form.
  Review and Approve Claims: Managers review submitted claims, updating the status as per the workflow.
  Permissions: Role-based permissions ensure that employees and managers have the correct access levels for their roles.

## Directory Structure
  ExpenseManager/
    doctype/: Contains the Doctype configurations for Expense Claim.
    config/: Holds module configurations.
    workflow/: Defines workflows for expense approvals.
    permissions/: Specifies role-based permissions.
    
## Contributing
  Fork the repository.
  Create a new branch:
    git checkout -b feature-branch-name
  Commit your changes:
    git commit -m 'Add new feature'
  Push to the branch:
    git push origin feature-branch-name
  Create a pull request on GitHub.

## License
  This project is licensed under the MIT License.

