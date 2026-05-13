# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build RESTful web APIs using the FastAPI framework. You'll create endpoints that handle HTTP requests and responses, work with path and query parameters, and use data validation with Pydantic models. By completing this assignment, you'll understand the fundamentals of API design and how to structure scalable web services.

## 📝 Tasks

### 🛠️ Set Up FastAPI and Create Your First Endpoint

#### Description
Initialize a FastAPI application and create a basic GET endpoint that returns JSON data. This is your foundation for building REST APIs.

#### Requirements
Completed program should:

- Import and instantiate a FastAPI app
- Create a GET endpoint at `/` that returns a welcome message in JSON format
- Run the app using `uvicorn` on localhost:8000
- Verify the endpoint works by visiting or requesting the URL

### 🛠️ Build Endpoints with Path and Query Parameters

#### Description
Extend your API with dynamic endpoints that accept parameters from the URL path and query string. Create endpoints to retrieve data based on user input.

#### Requirements
Completed program should:

- Create a GET endpoint with a path parameter (e.g., `/items/{item_id}`) that returns data based on the parameter
- Create a GET endpoint with query parameters (e.g., `/search?name=value`) to filter or search results
- Return appropriate JSON responses with the requested data
- Handle multiple query parameters in a single endpoint

### 🛠️ Implement POST Endpoints with Data Validation

#### Description
Create endpoints that accept POST requests with JSON payloads. Use Pydantic models to validate incoming data before processing.

#### Requirements
Completed program should:

- Define a Pydantic model for request data validation
- Create a POST endpoint that accepts JSON data matching the model
- Store or process the received data (e.g., add to a list or dictionary)
- Return a success response with the created or processed data
- Automatically validate input and return error messages for invalid data

### 🛠️ Create a Complete CRUD-like API (Stretch Goal)

#### Description
Combine previous tasks to build an API with multiple operations. Implement endpoints for creating, reading, and managing a collection of resources.

#### Requirements
Completed program should:

- Create endpoints for multiple HTTP methods (GET, POST, PUT/PATCH, DELETE)
- Support filtering and pagination on list endpoints (e.g., `/items?skip=0&limit=10`)
- Maintain data in memory across requests
- Include proper HTTP status codes (200, 201, 404, etc.)
- Provide meaningful error messages for invalid requests
