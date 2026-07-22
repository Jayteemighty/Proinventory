# ProInventory Backend Design

## Vision

ProInventory is an enterprise Procurement, Inventory and Sales platform
for organizations that serve customers daily. It manages purchasing,
stock, sales, users, permissions, reporting and audit history.

## Core Principles

-   API-first backend (FastAPI)
-   Modular monolith architecture
-   Role-Based Access Control (RBAC)
-   Every stock movement is traceable
-   Every important action is auditable

## User Management

When creating a staff account, the administrator (typically the CEO)
provides:

-   Full name
-   Username
-   Password
-   Position (free text, e.g. Cashier, Store Manager)
-   Department
-   Active/Inactive status

Instead of hardcoding permissions by role, the administrator assigns
**permissions** directly during account creation.

Example permissions:

-   View Sales
-   Create Sales
-   Cancel Sales
-   Print Receipt
-   View Inventory
-   Update Inventory
-   Receive Stock
-   Transfer Stock
-   Create Purchase
-   Approve Purchase
-   View Reports
-   Manage Users
-   Manage Roles
-   Manage Settings

Permissions can later be:

-   Added
-   Removed
-   Edited

Staff accounts can also be:

-   Disabled
-   Re-enabled
-   Deleted (soft delete recommended)

### Roles

Roles act as templates (CEO, Manager, Cashier, Warehouse Staff,
Developer), but permissions remain individually editable.

## Business Modules

-   Authentication
-   Users
-   Permissions
-   Departments
-   Products
-   Categories
-   Units
-   Warehouses
-   Inventory
-   Suppliers
-   Purchases
-   Sales
-   Customers
-   Reports
-   Notifications
-   Audit Logs

## Product

Each product stores:

-   SKU
-   Barcode
-   Name
-   Category
-   Unit
-   Cost Price
-   Selling Price
-   Minimum Stock
-   Maximum Stock
-   Status

## Inventory

Inventory is tracked per warehouse/location.

Every inventory change creates a Stock Transaction.

Transaction types include:

-   Purchase
-   Sale
-   Return
-   Transfer
-   Adjustment
-   Damage
-   Expired

## Sales

Sales record:

-   Invoice Number
-   Staff
-   Department
-   Products
-   Quantity
-   Selling Price
-   Discounts
-   Payment Method
-   Receipt
-   Date & Time

## Purchases

Purchases record:

-   Supplier
-   Purchase Date
-   Received Date
-   Cost Price
-   Quantity
-   Staff
-   Purchase Receipt

## Audit Log

Every important action records:

-   User
-   Action
-   Entity
-   Previous Value
-   New Value
-   Date & Time

## Folder Structure

``` text
backend/
├── app/
│   ├── auth/
│   ├── users/
│   ├── permissions/
│   ├── departments/
│   ├── products/
│   ├── inventory/
│   ├── purchases/
│   ├── sales/
│   ├── reports/
│   ├── audit/
│   ├── api/
│   ├── config/
│   ├── core/
│   ├── db/
│   └── main.py
├── tests/
├── docs/
└── README.md
```

## Future Features

-   Barcode scanner support
-   Multiple warehouses
-   Desktop (Qt/C++)
-   Offline synchronization
-   Multi-company support
-   Real-time notifications
