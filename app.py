"""
PhotoRestore - Old Photograph Restoration
A traditional computer vision application built with OpenCV and Streamlit.
Features the refined Vintage Studio UI with Light & Dark mode support.
"""

import os
import streamlit as st
import cv2
import numpy as np

from restoration import restore_image
from ui.styles import get_custom_css
from ui.components import (
    render_header,
    render_hero,
    render_metadata_card,
    render_original_preview,
    render_restoration_results,
    render_damage_mask,
    render_download_section,
    render_technology_section,
    render_footer
)

# Page configuration
st.set_page_config(
    page_title="PhotoRestore • Vintage Studio",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


def init_session_state():
    """Initialize persistent Streamlit session state keys."""
    if "theme" not in st.session_state:
        st.session_state.theme = "light"
    if "active_image_id" not in st.session_state:
        st.session_state.active_image_id = None
    if "image_bgr" not in st.session_state:
        st.session_state.image_bgr = None
    if "image_rgb" not in st.session_state:
        st.session_state.image_rgb = None
    if "image_name" not in st.session_state:
        st.session_state.image_name = None
    if "image_meta" not in st.session_state:
        st.session_state.image_meta = {}
    if "restored_data" not in st.session_state:
        st.session_state.restored_data = None


def load_image_from_bytes(file_bytes: bytes, filename: str, file_id: str):
    """Decode raw bytes into OpenCV BGR and RGB images, updating session state if changed."""
    if st.session_state.active_image_id != file_id:
        np_bytes = np.asarray(bytearray(file_bytes), dtype=np.uint8)
        decoded = cv2.imdecode(np_bytes, cv2.IMREAD_COLOR)

        if decoded is None:
            st.error("Could not read the uploaded image file. Please provide a valid JPG or PNG photograph.")
            return False

        # Reset any previous restoration results when a new image is loaded
        st.session_state.active_image_id = file_id
        st.session_state.image_bgr = decoded
        st.session_state.image_rgb = cv2.cvtColor(decoded, cv2.COLOR_BGR2RGB)
        st.session_state.image_name = filename
        st.session_state.restored_data = None

        h, w = decoded.shape[:2]
        c = decoded.shape[2] if len(decoded.shape) > 2 else 1
        st.session_state.image_meta = {
            "width": w,
            "height": h,
            "channels": c,
            "size": len(file_bytes)
        }
    return True


def get_available_samples():
    """Discover bundled sample images in assets/sample_images/."""
    sample_dir = os.path.join(os.path.dirname(__file__), "assets", "sample_images")
    if not os.path.isdir(sample_dir):
        return []
    valid_exts = {".jpg", ".jpeg", ".png"}
    samples = [
        f for f in sorted(os.listdir(sample_dir))
        if os.path.splitext(f)[1].lower() in valid_exts
    ]
    return samples


def main():
    init_session_state()

    # Inject Vintage Studio CSS with active theme (Light or Dark)
    st.markdown(get_custom_css(theme=st.session_state.theme), unsafe_allow_html=True)

    # Section A: Header Navigation with integrated Theme Switcher
    nav_col, theme_col = st.columns([5.2, 1.2], vertical_alignment="center")

    with nav_col:
        render_header(current_theme=st.session_state.theme)

    with theme_col:
        is_dark = st.session_state.theme == "dark"
        theme_label = "☀️ Light" if is_dark else "🌙 Dark"
        if st.button(
            theme_label,
            key="theme_toggle_btn",
            help="Toggle between Vintage Studio Light and Dark mode",
            use_container_width=True
        ):
            st.session_state.theme = "light" if is_dark else "dark"
            st.rerun()

    # Section B: Hero Section
    render_hero()

    # Section C: Photo Upload Workspace
    st.markdown(
        """
        <div class="section-header-block">
            <div class="section-kicker">Studio Workspace</div>
            <h3 class="section-heading">Photograph Input</h3>
            <p class="section-subtext">
                Upload a damaged vintage photograph or choose from our archival test samples.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    input_mode = st.radio(
        "Choose photo source:",
        options=["Upload Photograph", "Try Archival Sample"],
        horizontal=True,
        label_visibility="collapsed"
    )

    image_loaded = False

    if input_mode == "Upload Photograph":
        uploaded_file = st.file_uploader(
            "Upload your damaged photograph (JPG, JPEG, PNG)",
            type=["jpg", "jpeg", "png"],
            help="Select a photograph with scratches, tears, or bright surface damage."
        )

        if uploaded_file is not None:
            file_bytes = uploaded_file.read()
            file_id = f"upload_{uploaded_file.name}_{uploaded_file.size}"
            image_loaded = load_image_from_bytes(file_bytes, uploaded_file.name, file_id)
        else:
            if st.session_state.active_image_id and st.session_state.active_image_id.startswith("upload_"):
                st.session_state.active_image_id = None
                st.session_state.image_bgr = None
                st.session_state.image_rgb = None
                st.session_state.restored_data = None

    else:
        sample_files = get_available_samples()
        if sample_files:
            selected_sample = st.selectbox(
                "Select a vintage test photograph:",
                options=sample_files,
                index=0
            )
            sample_path = os.path.join(os.path.dirname(__file__), "assets", "sample_images", selected_sample)
            try:
                with open(sample_path, "rb") as sf:
                    sample_bytes = sf.read()
                file_id = f"sample_{selected_sample}_{len(sample_bytes)}"
                image_loaded = load_image_from_bytes(sample_bytes, selected_sample, file_id)
            except Exception as e:
                st.error(f"Error loading sample photograph: {e}")
        else:
            st.info("No sample photographs found in assets/sample_images/.")

    # If an image is successfully loaded and in session state
    if image_loaded and st.session_state.image_bgr is not None:
        meta = st.session_state.image_meta
        render_metadata_card(
            st.session_state.image_name,
            meta.get("width", 0),
            meta.get("height", 0),
            meta.get("channels", 3),
            meta.get("size", 0)
        )

        # Section E: Restoration Action Button
        btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
        with btn_col2:
            restore_clicked = st.button("Restore Photograph", use_container_width=True)

        if restore_clicked:
            with st.spinner("Restoring photograph with OpenCV Telea inpainting..."):
                try:
                    # Call existing, unmodified restoration function
                    results = restore_image(st.session_state.image_bgr)
                    st.session_state.restored_data = results
                except Exception as ex:
                    st.error(f"Restoration failed: {ex}")

        # If restoration results exist in state
        if st.session_state.restored_data is not None:
            st.markdown(
                """
                <div class="custom-success-banner">
                    ✓ Restoration completed successfully using OpenCV Telea Inpainting.
                </div>
                """,
                unsafe_allow_html=True
            )

            restored_bgr = st.session_state.restored_data["restored"]
            restored_rgb = cv2.cvtColor(restored_bgr, cv2.COLOR_BGR2RGB)
            mask = st.session_state.restored_data["mask"]

            # Section F: Before & After comparison workspace
            render_restoration_results(st.session_state.image_rgb, restored_rgb)

            # Section G: Detected Damage Mask (Expandable)
            render_damage_mask(mask)

            # Section H: Download Restored Image
            render_download_section(restored_bgr, st.session_state.image_name)

        else:
            # Section D: Original image preview before processing
            render_original_preview(st.session_state.image_rgb, st.session_state.image_name)

    # Section I: About the Technology
    render_technology_section()

    # Section J: Minimal Footer
    render_footer()


if __name__ == "__main__":
    main()
