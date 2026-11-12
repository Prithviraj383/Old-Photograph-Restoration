"""
Modular Presentation Components for PhotoRestore.
Implements the Vintage Studio layout sections with clean typography,
proper contrast in both Light and Dark themes, and robust navigation.
"""

import os
import base64
import streamlit as st
import cv2
import numpy as np


def _get_logo_base64() -> str:
    """Read the logo asset and encode as base64 data URI if available."""
    logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png")
    if os.path.exists(logo_path):
        try:
            with open(logo_path, "rb") as f:
                encoded = base64.b64encode(f.read()).decode("utf-8")
                return f"data:image/png;base64,{encoded}"
        except Exception:
            return ""
    return ""


def render_header(current_theme: str = "light"):
    """
    Section A: Brand navigation header.
    Features elegant typography, smooth scrolling without URL hash contamination,
    and no default blue underlines.
    """
    logo_src = _get_logo_base64()
    if logo_src:
        logo_html = f'<img src="{logo_src}" alt="PhotoRestore Logo" class="studio-brand-img" />'
    else:
        logo_html = '<div class="studio-brand-fallback">PR</div>'

    header_html = f"""
    <!-- Clean hash from URL so page never auto-scrolls down on reload -->
    <script>
        if (window.location.hash) {{
            window.history.replaceState(null, null, window.location.pathname);
        }}
    </script>
    <header class="studio-navbar">
        <a href="javascript:void(0)" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}}); return false;" class="studio-brand">
            {logo_html}
            <div>
                <div class="studio-brand-title">PhotoRestore</div>
                <div class="studio-brand-subtitle">Vintage Restoration Studio</div>
            </div>
        </a>
        <nav class="studio-nav-links">
            <a href="javascript:void(0)" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}}); return false;" class="studio-nav-link active">Studio</a>
            <a href="#about-section" onclick="var el = document.getElementById('about-section'); if(el) el.scrollIntoView({{behavior: 'smooth'}}); return false;" class="studio-nav-link">About</a>
        </nav>
    </header>
    """
    st.markdown(header_html, unsafe_allow_html=True)


def render_hero():
    """Section B: Vintage Studio hero section."""
    hero_html = """
    <section class="hero-container">
        <span class="hero-kicker">Digital Photo Restoration</span>
        <h1 class="hero-heading">Every Photograph Holds a Story.</h1>
        <p class="hero-subtext">
            Restore and preserve your old memories with traditional image processing techniques.
        </p>
    </section>
    """
    st.markdown(hero_html, unsafe_allow_html=True)


def render_metadata_card(filename: str, width: int, height: int, channels: int, size_bytes: int = None):
    """Render image metadata bar (dimensions, filename, channels, size)."""
    if size_bytes:
        if size_bytes > 1024 * 1024:
            size_str = f"{size_bytes / (1024 * 1024):.1f} MB"
        else:
            size_str = f"{size_bytes / 1024:.0f} KB"
    else:
        size_str = "Standard"

    meta_html = f"""
    <div class="meta-bar">
        <div class="meta-item">
            <span class="meta-label">File:</span>
            <span class="meta-value">{filename}</span>
        </div>
        <span class="meta-divider">•</span>
        <div class="meta-item">
            <span class="meta-label">Dimensions:</span>
            <span class="meta-value">{width} × {height} px</span>
        </div>
        <span class="meta-divider">•</span>
        <div class="meta-item">
            <span class="meta-label">Channels:</span>
            <span class="meta-value">{channels} ({'Color' if channels == 3 else 'Grayscale'})</span>
        </div>
        <span class="meta-divider">•</span>
        <div class="meta-item">
            <span class="meta-label">Size:</span>
            <span class="meta-value">{size_str}</span>
        </div>
    </div>
    """
    st.markdown(meta_html, unsafe_allow_html=True)


def render_original_preview(image_rgb: np.ndarray, filename: str):
    """Section D: Attractive archival preview card for the uploaded photograph."""
    st.markdown(
        """
        <div class="section-header-block">
            <div class="section-kicker">Input Preview</div>
            <h3 class="section-heading">Original Photograph</h3>
            <p class="section-subtext">Review the uploaded photograph before applying restoration inpainting.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="archival-frame">', unsafe_allow_html=True)
    st.image(
        image_rgb,
        caption=f"Source: {filename}",
        use_container_width=True
    )
    st.markdown('</div>', unsafe_allow_html=True)


def render_restoration_results(original_rgb: np.ndarray, restored_rgb: np.ndarray):
    """Section F: Professional two-panel comparison workspace."""
    st.markdown(
        """
        <div class="section-header-block">
            <div class="section-kicker">Restoration Workspace</div>
            <h3 class="section-heading">Before & After Comparison</h3>
            <p class="section-subtext">Compare the original damaged photograph with the reconstructed result.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown(
            """
            <div class="archival-frame">
                <div class="frame-badge frame-badge-original">Before • Original Photograph</div>
            """,
            unsafe_allow_html=True
        )
        st.image(
            original_rgb,
            caption="Original condition with detected surface damage",
            use_container_width=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown(
            """
            <div class="archival-frame">
                <div class="frame-badge frame-badge-restored">After • Restored Photograph</div>
            """,
            unsafe_allow_html=True
        )
        st.image(
            restored_rgb,
            caption="Restored with OpenCV Telea inpainting",
            use_container_width=True
        )
        st.markdown('</div>', unsafe_allow_html=True)


def render_damage_mask(mask: np.ndarray):
    """Section G: Damage mask inside an expandable container."""
    with st.expander("View Detected Damage Mask", expanded=False):
        st.markdown(
            """
            <p style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 0.8rem;">
                This binary mask highlights regions identified for inpainting. White pixels represent
                detected scratches and surface cracks exceeding the brightness threshold (195), expanded via 7×7 dilation.
            </p>
            """,
            unsafe_allow_html=True
        )
        st.image(
            mask,
            caption="Binary Damage Mask (White = Regions Inpainted)",
            use_container_width=True
        )


def render_download_section(restored_bgr: np.ndarray, original_filename: str):
    """Section H: Download restored photograph with OpenCV encoding."""
    st.markdown(
        """
        <div class="section-header-block" style="margin-top: 1.8rem; margin-bottom: 0.8rem;">
            <div class="section-kicker">Export</div>
            <h3 class="section-heading">Download Restored Photograph</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    success, encoded_image = cv2.imencode(".jpg", restored_bgr)
    if success:
        base_name = os.path.splitext(original_filename)[0]
        download_name = f"{base_name}_restored.jpg"

        st.download_button(
            label="Download Restored Photograph",
            data=encoded_image.tobytes(),
            file_name=download_name,
            mime="image/jpeg",
            help="Download the full-resolution restored image in JPEG format."
        )
    else:
        st.error("Failed to encode restored image for download.")


def render_technology_section():
    """Section I: Compact educational breakdown of the 5-step processing pipeline."""
    tech_html = """
    <div id="about-section"></div>
    <div class="section-header-block" style="margin-top: 3.2rem;">
        <span class="section-kicker">Academic Methodology</span>
        <h2 class="section-heading">Behind the Restoration</h2>
        <p class="section-subtext">
            Our traditional computer vision pipeline restores degraded photographs using five algorithmic steps:
        </p>
    </div>

    <div class="tech-grid">
        <div class="tech-card">
            <span class="tech-step-num">01</span>
            <div class="tech-step-title">Grayscale Conversion</div>
            <p class="tech-step-desc">
                Converts BGR color data into single-channel luminance (<code>cv2.COLOR_BGR2GRAY</code>) to analyze intensity independent of color fading.
            </p>
        </div>
        <div class="tech-card">
            <span class="tech-step-num">02</span>
            <div class="tech-step-title">Thresholding</div>
            <p class="tech-step-desc">
                Applies binary thresholding at intensity 195 (<code>cv2.THRESH_BINARY</code>) to isolate abnormally bright scratch and tear artifacts.
            </p>
        </div>
        <div class="tech-card">
            <span class="tech-step-num">03</span>
            <div class="tech-step-title">Damage Mask</div>
            <p class="tech-step-desc">
                Constructs a clean binary matrix where damage regions are flagged with pure white (255) against intact background (0).
            </p>
        </div>
        <div class="tech-card">
            <span class="tech-step-num">04</span>
            <div class="tech-step-title">Mask Dilation</div>
            <p class="tech-step-desc">
                Expands damaged boundaries using a 7×7 rectangular kernel (1 iteration) so scratch edges are fully encapsulated for repair.
            </p>
        </div>
        <div class="tech-card">
            <span class="tech-step-num">05</span>
            <div class="tech-step-title">TELEA Inpainting</div>
            <p class="tech-step-desc">
                Applies Alexandru Telea's Fast Marching Method (4px radius) to smoothly propagate neighboring textures into damaged regions.
            </p>
        </div>
    </div>

    <div class="tech-note-box">
        <strong>Technical Note:</strong> This application utilizes classic deterministic image processing (OpenCV Telea inpainting).
        It does not use generative AI or neural hallucination to synthesize missing facial features. Restoration fidelity depends directly
        on the photographic condition and contrast between damaged scratches and neighboring pixels.
    </div>
    """
    st.markdown(tech_html, unsafe_allow_html=True)


def render_footer():
    """Section J: Minimal vintage studio footer."""
    footer_html = """
    <footer class="studio-footer">
        <div class="footer-title">PhotoRestore</div>
        <div class="footer-tagline">Preserving memories through image processing.</div>
        <div class="footer-credits">
            Built with OpenCV & Streamlit • Academic Image Processing Project
        </div>
    </footer>
    """
    st.markdown(footer_html, unsafe_allow_html=True)
