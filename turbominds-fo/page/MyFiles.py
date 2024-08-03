import streamlit as st
from streamlit_quill import st_quill
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
import pandas as pd
from dotenv import load_dotenv
import os
import requests
from authenticator.login import x_company_id

# Load environment variables from a .env file
load_dotenv()

# Access environment variables
BACKEND_BASE_URL = os.getenv('BACKEND_BASE_URL', 'http://127.0.0.1:8000')


def list_blueprints(x_company_id):
    response = requests.get(f"{BACKEND_BASE_URL}/blueprint", headers={"x-company-id": x_company_id})
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching blueprints")
        return []

def get_blueprint(blueprint_id, x_company_id):
    
    response = requests.get(f"{BACKEND_BASE_URL}/blueprint/{blueprint_id}", headers={"x-company-id": x_company_id})
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching blueprint")
        return None

def update_blueprint(blueprint_id, data, x_company_id):
    response = requests.put(f"{BACKEND_BASE_URL}/blueprint/{blueprint_id}", json=data, headers={"x-company-id": x_company_id})
    if response.status_code == 200:
        st.success("Blueprint updated successfully")
    else:
        st.error("Error updating blueprint")

def download_blueprint(blueprint_id, x_company_id):
    response = requests.get(f"{BACKEND_BASE_URL}/blueprint/{blueprint_id}/download", headers={"x-company-id": x_company_id})
    if response.status_code == 200:
        return response.content
    else:
        st.error("Error downloading blueprint")
        return None

def display_blueprint_list(x_company_id):
    blueprints = list_blueprints(x_company_id)
    st.title("Recently Created Briefs")
    if blueprints:
        st.write("Select a Brief:")
        
        col2, col3, col4 = st.columns([4, 2, 2])
        col2.write("Title")
        col3.write("Updated Time")
        col4.write("Action")
        
        for blueprint in blueprints:
            col2, col3, col4 = st.columns([4, 2, 2])
            col2.write(blueprint['title'])
            col3.write(blueprint['updated_time'])
            if col4.button('View Details', key=blueprint['id']):
                st.session_state.selected_blueprint_id = blueprint['id']
                st.session_state.active_section = "Blueprint Details"
                st.rerun()

def display_blueprint_details(selected_blueprint_id, x_company_id):
    blueprint = get_blueprint(selected_blueprint_id, x_company_id)
    st.empty()
    st.empty()
    
    if blueprint:
        if st.button("Back to List"):
            st.session_state.active_section = "List of Files"
            st.rerun()
        
        st.title(f"Editing Brief: {selected_blueprint_id}")
        final_brief = st_quill(value=blueprint["final_brief"], key=f"quill_{selected_blueprint_id}")
        
        if "images" not in st.session_state:
            st.session_state.images = blueprint["images"]

        st.subheader("Images")
        for image in st.session_state.images:
            st.image(image)
            if st.button(f"Remove {image}"):
                st.session_state.images.remove(image)
                st.rerun()

        if st.button("Save"):
            blueprint_data = {"final_brief": final_brief, "images": st.session_state.images}
            update_blueprint(selected_blueprint_id, blueprint_data, x_company_id)
        
        if st.button("Download"):
            file_content = download_blueprint(selected_blueprint_id, x_company_id)
            # if file_content:
            #     st.download_button(label="Download Blueprint", data=file_content, file_name=f"{selected_blueprint_id}.pdf")

def show():
    x_company_id = st.session_state.get(x_company_id)
    # st.write("Logged in as / Company ID: " + x_company_id)
    
    if "active_section" not in st.session_state:
        st.session_state.active_section = "List of Files"
        
    if st.session_state.active_section == "List of Files":
        display_blueprint_list(x_company_id)
    elif st.session_state.active_section == "Blueprint Details":
        if "selected_blueprint_id" in st.session_state:
            display_blueprint_details(st.session_state.selected_blueprint_id, x_company_id)

if __name__ == "__main__":
    show()
