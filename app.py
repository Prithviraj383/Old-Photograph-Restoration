
import streamlit as st
import cv2
import numpy as np

from restoration import restore_image

st.set_page_config(
    page_title="PhotoRestore",
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ PhotoRestore")
st.write("Restore old and damaged photographs using OpenCV.")

uploaded_file = st.file_uploader(
    "Upload your damaged photograph",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Read uploaded image
    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if image is None:
        st.error("Could not read the uploaded image.")
    else:
        st.subheader("Original Photograph")
        st.image(
            cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
            use_container_width=True
        )

        if st.button("✨ Restore Photograph"):
            with st.spinner("Restoring your photograph..."):

                results = restore_image(image)

                restored = results["restored"]
                mask = results["mask"]

            st.success("Restoration completed!")

            # Before and after comparison
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Before Restoration")
                st.image(
                    cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
                    use_container_width=True
                )

            with col2:
                st.subheader("After Restoration")
                st.image(
                    cv2.cvtColor(restored, cv2.COLOR_BGR2RGB),
                    use_container_width=True
                )

            # Display detected damage mask
            with st.expander("View detected damage mask"):
                st.image(
                    mask,
                    caption="White = regions selected for restoration",
                    use_container_width=True
                )

            # Download restored photograph
            success, encoded_image = cv2.imencode(
                ".jpg", restored
            )

            if success:
                st.download_button(
                    "⬇️ Download Restored Photograph",
                    data=encoded_image.tobytes(),
                    file_name="restored_photo.jpg",
                    mime="image/jpeg"
                )
