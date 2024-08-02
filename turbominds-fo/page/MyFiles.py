import streamlit as st
from streamlit_quill import st_quill
import requests
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Access environment variables
BACKEND_BASE_URL = os.getenv('BACKEND_BASE_URL', 'http://127.0.0.1:8000')

def list_blueprints(company_id):
    response = requests.get(f"{BACKEND_BASE_URL}/blueprint", headers={"company-id": company_id})
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching blueprints")
        return []

def get_blueprint(blueprint_id, company_id):
    response = requests.get(f"{BACKEND_BASE_URL}/blueprint/{blueprint_id}", headers={"company-id": company_id})
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching blueprint")
        return None

def update_blueprint(blueprint_id, data, company_id):
    response = requests.put(f"{BACKEND_BASE_URL}/blueprint/{blueprint_id}", json=data, headers={"company-id": company_id})
    if response.status_code == 200:
        st.success("Blueprint updated successfully")
    else:
        st.error("Error updating blueprint")

def download_blueprint(blueprint_id, company_id):
    response = requests.get(f"{BACKEND_BASE_URL}/blueprint/{blueprint_id}/download", headers={"company-id": company_id})
    if response.status_code == 200:
        return response.content
    else:
        st.error("Error downloading blueprint")
        return None

def display_blueprint_list(company_id):
    blueprints = list_blueprints(company_id)
    
    if blueprints:
        blueprint_names = [bp["id"] for bp in blueprints]
        selected_blueprint_id = st.selectbox("Select a Blueprint", blueprint_names)
        
        if st.button("View Details"):
            st.session_state.selected_blueprint_id = selected_blueprint_id
            st.session_state.active_section = "Blueprint Details"
            st.experimental_rerun()

def display_blueprint_details(selected_blueprint_id, company_id):
    blueprint = get_blueprint(selected_blueprint_id, company_id)
    
    if blueprint:
        if st.button("Back to List"):
            st.session_state.active_section = "List of Files"
            st.experimental_rerun()
        
        st.header(f"Editing Blueprint: {selected_blueprint_id}")
        final_brief = st_quill(value=blueprint["final_brief"], key=f"quill_{selected_blueprint_id}")
        
        if "images" not in st.session_state:
            st.session_state.images = blueprint["images"]

        st.subheader("Images")
        for image in st.session_state.images:
            st.image(image)
            if st.button(f"Remove {image}"):
                st.session_state.images.remove(image)
                st.experimental_rerun()

        if st.button("Save"):
            blueprint_data = {"final_brief": final_brief, "images": st.session_state.images}
            update_blueprint(selected_blueprint_id, blueprint_data, company_id)
        
        if st.button("Download"):
            content = download_blueprint(selected_blueprint_id, company_id)
            if content:
                st.download_button(label="Download Blueprint", data=content, file_name=f"{selected_blueprint_id}.doc", mime="application/msword")

def show():
    st.title("Blueprint Manager")
    company_id = st.text_input("Enter Company ID", value="")  # Replace with actual company ID 

    if company_id:
        if "active_section" not in st.session_state:
            st.session_state.active_section = "List of Files"

        if st.session_state.active_section == "List of Files":
            display_blueprint_list(company_id)
        elif st.session_state.active_section == "Blueprint Details":
            if "selected_blueprint_id" in st.session_state:
                display_blueprint_details(st.session_state.selected_blueprint_id, company_id)

if __name__ == "__main__":
    show()
