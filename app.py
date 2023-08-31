import streamlit as st

st.markdown("""
    # Artsy-FArtSci

    ## Fine Art with Data Science!

    Using the public [Artsy](https://www.artsy.net) database you can
    find new public domain artists to enjoy and learn about by inputting
    your own favorite piece of fine art. 
    Join us on an exploration of **Art**, with **Data Science**
    - bullet points
""")


img_file_buffer = st.camera_input("Upload an image of the Art you like:")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))

st.markdown("""
    ## Do you understand?
    """
direction = st.radio('Select a direction', ('Yes', 'A little', 'No'))

st.write(direction)

if direction == 'Yes':
    st.write('**Excellent!**')
elif direction == 'A little bit':
    st.write('please contact customer support')
elif direction == 'No':
    st.write('Read a book (or learn to read)')
else:
    st.write('please make a selection')
