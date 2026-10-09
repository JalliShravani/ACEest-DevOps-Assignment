# ACEest Fitness & Gym — DevOps Assignment

## 1. Project Overview

ACEest Fitness & Gym is a Flask-based web application developed to demonstrate a DevOps workflow. The project integrates Git and GitHub for version control, Pytest for automated testing, Docker for containerization, Jenkins for continuous integration, and GitHub Actions for automated build and testing.

## 2. Technologies Used

- Python and Flask
- Pytest
- Flake8
- Git and GitHub
- Docker
- Jenkins
- GitHub Actions

## 3. Project Structure

```text
ACEest-DevOps-Assignment/
├── app.py
├── tests/
│   └── test_app.py
├── requirements.txt
├── Dockerfile
├── Jenkins.Dockerfile
├── .dockerignore
├── .gitignore
├── .github/
│   └── workflows/
│       └── main.yml
└── README.md
```

## 4. Run the Application Locally

### Prerequisites

Install Python, Git, and Visual Studio Code.

### Setup

Clone the repository:

```bash
git clone https://github.com/JalliShravani/ACEest-DevOps-Assignment.git
cd ACEest-DevOps-Assignment
```

Create and activate a virtual environment on macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
python -m pip install flake8
```

Start the Flask application:

```bash
python app.py
```

The application runs on port 5000.

## 5. Application Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns the application welcome response |
| GET | `/health` | Checks application health |
| GET | `/clients` | Retrieves the clients list |
| POST | `/clients` | Adds a client when the required fields are provided |

The POST `/clients` endpoint requires `name`, `age`, and `weight`.

### Manual API Testing

With the application running, open another terminal and execute:

```bash
curl http://localhost:5000/
curl http://localhost:5000/health
curl http://localhost:5000/clients
```

Test adding a client:

```bash
curl -X POST http://localhost:5000/clients \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Client","age":25,"weight":65}'
```

## 6. Automated Testing and Code Quality

Run the unit tests:

```bash
python -m pytest -v
```

Run Flake8:

```bash
python -m flake8 app.py tests/test_app.py --max-line-length=100
```

The test suite covers the home endpoint, health endpoint, client retrieval, adding a client, and handling a request with missing required fields.

## 7. Docker Containerization

Build the application image:

```bash
docker build -t aceest-fitness:latest .
```

Run the container:

```bash
docker run --rm -p 5000:5000 aceest-fitness:latest
```

Run the tests inside the Docker image:

```bash
docker run --rm aceest-fitness:latest pytest -v
```

The Dockerfile installs the Python dependencies, copies the application and tests into the image, and configures the application to run on port 5000.

## 8. Jenkins Continuous Integration

The project includes `Jenkins.Dockerfile`, which defines a Jenkins image with Python and Docker CLI tools installed.

The Jenkins job uses the GitHub repository as its source and runs these steps:

1. Checks out the latest code from the `main` branch.
2. Creates a Python virtual environment.
3. Installs project dependencies.
4. Runs Pytest.
5. Builds the Docker image.
6. Runs the automated tests inside the Docker container.

The Jenkins job was tested successfully in the local Jenkins environment.

## 9. GitHub Actions Continuous Integration

The workflow is located at `.github/workflows/main.yml` and runs on pushes and pull requests.

It contains three jobs:

1. **Build and Lint:** installs dependencies, checks Python syntax, runs Flake8, and executes unit tests.
2. **Docker Image Assembly:** builds the Docker image and uploads it as a workflow artifact.
3. **Automated Testing in Container:** downloads the Docker image, loads it, and runs the tests inside the container.

The Docker assembly and container testing jobs depend on the preceding jobs, helping prevent later stages from running when an earlier stage fails.

## 10. Version Control

The project is maintained in Git and hosted on GitHub.

Repository: https://github.com/JalliShravani/ACEest-DevOps-Assignment

The commit history records application development, Docker containerization, CI workflow configuration, and project documentation. A feature branch and pull request were used to integrate the CI configuration into `main`.

## 11. Current Validation Results

- Local Pytest suite: 5 tests passed.
- Flake8: completed without reported issues.
- Docker image build and container tests: previously successful.
- GitHub Actions: all three workflow jobs passed.
- Jenkins: build and Docker container tests previously completed successfully.

## 12. Limitations

Client data is stored in memory rather than a persistent database. The data may reset when the application restarts. This project demonstrates the requested development and CI workflow rather than a production-ready data-storage solution.
