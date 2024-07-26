import streamlit as st
from streamlit_quill import st_quill
from state.brief_session import Brief_State
from state.session_state import get_brief_class

def show(result):
    col1, col2 = st.columns([3, 1])  # Create two columns with ratio 3:1

    with col1:
        content = st_quill(value=result["final_research"])
        brief_class = get_brief_class()
        _col1, _col2 = st.columns([3, 1])
        with _col1:
            st.write(brief_class.title)
        with _col2:
            if st.button("Add to Brief", key="research_add_to_brief"):
                brief_class.add_to_brief(result['final_research'])
                brief_class.update_brief_result(result)
                st.session_state["selected_page"] = "My File"
                st.rerun()
    
    with col2:
        st.markdown(
            """
            <style>
            .question-box {
                background-color: #f0f0f0;
                padding: 10px;
                margin-bottom: 10px;
                border-radius: 5px;
                word-wrap: break-word;  /* Ensure long URLs break into multiple lines */
            }
            .source-title {
                font-weight: bold;
            }
            .source-link {
                word-wrap: break-word;  /* Ensure long URLs break into multiple lines */
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        for source in result['sources']:
            st.markdown(
                f"""
                <div class="question-box">
                    <div class="source-title">{source['title']}</div>
                    <div class="source-link"><a href="{source['url']}" target="_blank">{source['url']}</a></div>
                </div>
                """,
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    show()
