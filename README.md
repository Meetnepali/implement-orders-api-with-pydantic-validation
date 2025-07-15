# Guidance for Task

This project is a modular FastAPI backend service for collecting and managing product feedback from customers. You are expected to work on a real-world style backend API that supports basic CRUD operations for the feedback resource, using modern Python frameworks and techniques.

## Requirements
- Implement an organized FastAPI project for product feedback with modular routers, schemas, and database interaction.
- Ensure field validation for feedback, including that the rating is an integer between 1 and 5.
- Use SQLAlchemy with an in-memory SQLite database for storage.
- On successful feedback creation, simulate an asynchronous thank-you email using FastAPI's BackgroundTasks (no real emails are sent, simply log or print to simulate).
- Consistent, robust error handling: endpoints should respond with clear and appropriate HTTP error codes and custom error messages (e.g., resource not found).
- Simple app configuration must use environment variables or a .env file.
- The Dockerfile should enable rapid containerized startup. The provided install and run scripts must only build and run the container.
- Your code should be readable, modular, and maintainable, with all FastAPI application code inside the `app/` directory.

## Verifying Your Solution
- Ensure all endpoints for Creating, Reading (by id and all), and Deleting feedback are available.
- Confirm that invalid ratings (not 1-5) or other invalid input data are rejected with helpful error responses.
- Check that after feedback creation, a simulated background email action reliably occurs (e.g., visible in logs or output).
- Test that missing/nonexistent feedback IDs are handled with appropriate error messages and status codes.
- Review the project structure for modularity and separation: routers, schemas, db, background logic, error handlers, and main setup should be organized.

Use this guidance to complete, review, and improve the given code, following best practices and leveraging the structure provided.