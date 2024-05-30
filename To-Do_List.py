import streamlit as st

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

st.title('To-Do List')

st.write("""
Here you can add, mark as done, and delete your daily basic routine tasks:

- "Input widget" is for adding your new tasks.
- "Checkbox" for marking your tasks once you are done with it.
- "Delete option" to remove repetitive task added in the list.
""")

new_task = st.text_input('Add a new task')


if st.button('Add Task'):
    if new_task:
        st.session_state.tasks.append({'task': new_task, 'done': False})
        st.experimental_rerun()  

# Display the list of tasks
for i, task in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
    with col1:
        if st.checkbox('', key=f'done_{i}', value=task['done']):
            st.session_state.tasks[i]['done'] = not st.session_state.tasks[i]['done']
            st.experimental_rerun()  
    with col2:
        if task['done']:
            st.write(f"~~{task['task']}~~")
        else:
            st.write(task['task'])
    with col3:
        if st.button('Delete', key=f'delete_{i}'):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()
