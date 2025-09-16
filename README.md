# Earth Man 
## Waste Collection automation


earth man  is a cloud-based, distributed,web service to collect information on waste, Determine collection points and efficiently route for the collector transport.


## Why Need earth man?
In existing System, 
- categorization of Waste are static, as decompisble/non-Decomposible , wet/ dry , e-waste.
- collection points are on busy streets where Waste accumalates weekly.Collecting waste from events/Functions are not possible.
- Collection points are defined by juridictions or city boards. Intra  inter zone collections are not possible in existing system.
 - Transports round trip often endsup with low collection or with over weight. transports need to make multiple round trips if acummalated wastes are high in quantity.
- Users often misses waste trucks as it comes only in timezones. No way to track Trucks on the run.
- Users unable to update type of waste or as k queries on waste management.


High-Level Requirements for a Waste Collection System
This document outlines the high-level requirements for a software system designed to optimize waste collection. The system will primarily serve three types of users: administrators, dispatchers, and drivers.

1. Functional Requirements
User Management: The system must allow for the creation, editing, and deletion of user accounts with different roles (administrator, dispatcher, driver).

Dynamic Agregation of Load: User might be able to provide current amount of waste and Type to get Fleet information.

Customer & Location Management: The system must maintain a database of customers, their addresses, and service schedules. It should be able to handle both residential and commercial customers.

Vehicle & Fleet Management: The system must track vehicle information, including capacity, type (e.g., front-loader, side-loader), and maintenance schedules.

Route Optimization: The core of the system should be a module that generates the most efficient routes for waste collection based on customer locations, vehicle capacity, and time constraints.

Real-time Tracking: The system must provide real-time GPS tracking of waste collection vehicles. Dispatchers should be able to see the live location and status of each truck on a map.

Job & Task Management: The system must allow dispatchers to assign routes and specific tasks to drivers. Drivers should be able to receive these assignments on a mobile device.

Data & Analytics: The system must collect data on completed routes, service times, and fill levels of bins (if smart bins are used). It should generate reports and dashboards to provide insights into operational efficiency.

Notifications: The system should send automated notifications to customers regarding their scheduled collection times and any delays.

Reporting: The system must generate reports on key performance indicators (KPIs) such as routes completed, total waste collected, and fuel consumption.

Waste Segregation and Aggreagtion: categorization of Waste are static, as decompisble/non-Decomposible , wet/ dry , e-waste.

2. Non-Functional Requirements
Performance: The system must be highly responsive, with a maximum load time of 2 seconds for all key functions. The route optimization algorithm should run within 5 minutes for a typical service area.

Scalability: The system must be able to handle an increase in the number of customers, vehicles, and users without a significant degradation in performance.

Security: The system must protect sensitive user and customer data through strong authentication, authorization, and data encryption.

Usability: The user interface for the dispatcher and administrator dashboards should be intuitive and easy to use. The mobile application for drivers must be simple and require minimal training.

Availability: The system must have an uptime of at least 99.5%.

Integration: The system should have the capability to integrate with third-party software like accounting systems, mapping services (e.g., Google Maps API), and potentially smart bin sensors.

Maintainability: The system should be designed with modularity in mind, allowing for easy updates, bug fixes, and the addition of new features.

3. User Requirements
Administrator: Requires a comprehensive dashboard to manage users, customers, and fleet. Needs to access high-level analytics and reports.

Dispatcher: Needs a real-time view of all vehicles and routes. The primary user of the route optimization and job assignment features.

Driver: Requires a simple, mobile-friendly interface to view their assigned route, get turn-by-turn directions, and update the status of each collection (e.g., "completed," "skipped"). Needs to be able to work offline and sync data later.
