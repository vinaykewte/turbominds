import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from streamlit_option_menu import option_menu
import warnings

def load_config():
    config_path = r'authenticator\config.yaml'
    with open(config_path) as file:
        return yaml.load(file, Loader=SafeLoader)
    
config = load_config()

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login(fields=['username', 'password'])

if authentication_status:
    st.empty()
    st.empty()
    st.empty()

    authenticator.logout('Logout', 'main')
    st.sidebar.success(f'Welcome {name}')

    with st.sidebar:
        selected = option_menu("Turbo Minds", ["Brief", 'Research', 'Strategy', 'Design', 'My File'], 
                               icons=['journal', 'search', 'calendar3-event', 'card-image', 'palette-fill'], menu_icon="fire", default_index=0)
    
    def load_page(selected_option):
        if selected_option == "Brief":
            import page.Brief as page
        elif selected_option == "Research":
            import page.research as page
        elif selected_option == "Strategy":
            import page.strategy as page
        elif selected_option == "Design":
            import page.design as page
        elif selected_option == "My File":
            import page.MyFiles as page
        else:
            st.error("Page not found")
            return
        page.show()

    load_page(selected)

else:
    if st.session_state.get("authentication_status") is False:
        st.error('Username/password is incorrect')
    else:
        st.warning('Please enter your username and password')

    try:
        if authenticator.register_user(fields=['username', 'password'] , preauthorization=False):
            st.success('User registered successfully')
    except Exception as e:
        st.error(str(e))
