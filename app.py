from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock dataset (simulating a database)
projects = [
    {"id": 1, "name": "Library Management System", "model": "Waterfall", "status": "Completed"},
    {"id": 2, "name": "E-commerce Website", "model": "Agile", "status": "In Progress"},
    {"id": 3, "name": "Hospital Management System", "model": "DevOps", "status": "Planning"}
]

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Software Engineering Project API!"})

# Get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    return jsonify(projects)

# Get project by ID
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = next((p for p in projects if p["id"] == project_id), None)
    if project:
        return jsonify(project)
    return jsonify({"error": "Project not found"}), 404

# Add a new project
@app.route('/projects', methods=['POST'])
def add_project():
    new_project = request.json
    new_project["id"] = len(projects) + 1
    projects.append(new_project)
    return jsonify(new_project), 201

# Update project
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    data = request.json
    project.update(data)
    return jsonify(project)

# Delete project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    global projects
    projects = [p for p in projects if p["id"] != project_id]
    return jsonify({"message": "Project deleted"})

if __name__ == '__main__':
    app.run(debug=True)
