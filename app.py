import streamlit as st
import json
import os

# Load dataset if exists, else create sample data
DATA_FILE = "dataset.json"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        projects = json.load(f)
else:
    projects = [
        {"id": 1, "name": "Library Management System", "model": "Waterfall", "status": "Completed"},
        {"id": 2, "name": "E-commerce Website", "model": "Agile", "status": "In Progress"},
        {"id": 3, "name": "Hospital Management System", "model": "DevOps", "status": "Planning"}
    ]

# Title
st.title("📌 Software Engineering Project Manager")

# Display projects
st.subheader("All Projects")
st.table(projects)

# Add new project
st.subheader("➕ Add New Project")
with st.form("add_project_form"):
    name = st.text_input("Project Name")
    model = st.selectbox("Model", ["Waterfall", "Agile", "DevOps"])
    status = st.selectbox("Status", ["Planning", "In Progress", "Completed"])
    submitted = st.form_submit_button("Add Project")

    if submitted:
        new_id = max([p["id"] for p in projects]) + 1 if projects else 1
        new_project = {"id": new_id, "name": name, "model": model, "status": status}
        projects.append(new_project)

        # Save updated dataset
        with open(DATA_FILE, "w") as f:
            json.dump(projects, f, indent=4)

        st.success(f"✅ Project '{name}' added successfully!")

# Update project status
st.subheader("✏️ Update Project Status")
project_ids = [p["id"] for p in projects]
if project_ids:
    selected_id = st.selectbox("Select Project ID", project_ids)
    new_status = st.selectbox("New Status", ["Planning", "In Progress", "Completed"])
    if st.button("Update Status"):
        for p in projects:
            if p["id"] == selected_id:
                p["status"] = new_status
        with open(DATA_FILE, "w") as f:
            json.dump(projects, f, indent=4)
        st.success(f"✅ Project {selected_id} updated to '{new_status}'!")

# Delete project
st.subheader("🗑️ Delete Project")
if project_ids:
    delete_id = st.selectbox("Select Project ID to Delete", project_ids, key="delete")
    if st.button("Delete Project"):
        projects = [p for p in projects if p["id"] != delete_id]
        with open(DATA_FILE, "w") as f:
            json.dump(projects, f, indent=4)
        st.error(f"❌ Project {delete_id} deleted!")
