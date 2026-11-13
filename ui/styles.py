
"""
Vintage Studio Styling for PhotoRestore.
Defines centralized theme variables (Light & Dark), design tokens,
and robust CSS rules without breaking native Streamlit icon ligatures.
"""

# Palette Constants (Light Theme)
LIGHT_PALETTE = {
    "bg_primary": "#F7F4EE",
    "bg_secondary": "#EFE9DF",
    "bg_card": "#FFFFFF",
    "bg_hover": "#F0EAE0",
    "text_primary": "#302A24",
    "text_secondary": "#817568",
    "accent": "#806343",
    "accent_hover": "#654C35",
    "border": "#E2D9CC",
    "border_focus": "#806343",
    "btn_primary_bg": "#806343",
    "btn_primary_text": "#FFFFFF",
    "btn_primary_hover": "#654C35",
    "btn_secondary_bg": "#302A24",
    "btn_secondary_text": "#FAF7F2",
    "btn_secondary_hover": "#4A423B",
    "success_bg": "#F3F7F4",
    "success_text": "#4E7A58",
    "success_border": "rgba(78, 122, 88, 0.3)",
    "shadow": "0 4px 18px rgba(48, 42, 36, 0.05)",
    "nav_bg": "#FFFFFF",
    "nav_border": "#E2D9CC",
    "badge_orig_bg": "#EFE9DF",
    "badge_orig_text": "#302A24",
    "badge_rest_bg": "rgba(78, 122, 88, 0.12)",
    "badge_rest_text": "#4E7A58",
}

# Palette Constants (Dark Theme)
DARK_PALETTE = {
    "bg_primary": "#211F1D",
    "bg_secondary": "#2C2926",
    "bg_card": "#302C28",
    "bg_hover": "#383430",
    "text_primary": "#F3EBDD",
    "text_secondary": "#B5A89A",
    "accent": "#C29A6B",
    "accent_hover": "#D4AF82",
    "border": "#494139",
    "border_focus": "#C29A6B",
    "btn_primary_bg": "#C29A6B",
    "btn_primary_text": "#1C1814",
    "btn_primary_hover": "#D4AF82",
    "btn_secondary_bg": "#3E3933",
    "btn_secondary_text": "#F3EBDD",
    "btn_secondary_hover": "#4D4740",
    "success_bg": "#232B25",
    "success_text": "#78B087",
    "success_border": "rgba(120, 176, 135, 0.35)",
    "shadow": "0 4px 18px rgba(0, 0, 0, 0.35)",
    "nav_bg": "#2A2622",
    "nav_border": "#494139",
    "badge_orig_bg": "#2C2926",
    "badge_orig_text": "#F3EBDD",
    "badge_rest_bg": "rgba(120, 176, 135, 0.18)",
    "badge_rest_text": "#78B087",
}


def get_custom_css(theme: str = "light") -> str:
    """
    Return the complete custom CSS stylesheet for PhotoRestore.
    Uses centralized CSS variables for theme switching and protects native
    Streamlit icon fonts from ligature breakage.
    """
    palette = DARK_PALETTE if theme == "dark" else LIGHT_PALETTE

    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    /* Centralized Theme CSS Variables */
    :root {{
        --bg-primary: {palette["bg_primary"]};
        --bg-secondary: {palette["bg_secondary"]};
        --bg-card: {palette["bg_card"]};
        --bg-hover: {palette["bg_hover"]};
        --text-primary: {palette["text_primary"]};
        --text-secondary: {palette["text_secondary"]};
        --accent: {palette["accent"]};
        --accent-hover: {palette["accent_hover"]};
        --border: {palette["border"]};
        --border-focus: {palette["border_focus"]};
        --btn-primary-bg: {palette["btn_primary_bg"]};
        --btn-primary-text: {palette["btn_primary_text"]};
        --btn-primary-hover: {palette["btn_primary_hover"]};
        --btn-secondary-bg: {palette["btn_secondary_bg"]};
        --btn-secondary-text: {palette["btn_secondary_text"]};
        --btn-secondary-hover: {palette["btn_secondary_hover"]};
        --success-bg: {palette["success_bg"]};
        --success-text: {palette["success_text"]};
        --success-border: {palette["success_border"]};
        --shadow: {palette["shadow"]};
        --nav-bg: {palette["nav_bg"]};
        --nav-border: {palette["nav_border"]};
        --badge-orig-bg: {palette["badge_orig_bg"]};
        --badge-orig-text: {palette["badge_orig_text"]};
        --badge-rest-bg: {palette["badge_rest_bg"]};
        --badge-rest-text: {palette["badge_rest_text"]};
    }}

    /* Base Application Styling - scoped to html, body, and stApp */
    html, body, .stApp {{
        background-color: var(--bg-primary) !important;
        color: var(--text-primary) !important;
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        scroll-behavior: smooth;
    }}

    /* Explicitly preserve and lock Material Symbols icon fonts on Streamlit icons */
    [data-testid="stIconMaterial"],
    .material-symbols-rounded,
    .material-symbols-outlined,
    [class*="material-symbols"],
    [data-testid="stExpanderToggleIcon"] {{
        font-family: 'Material Symbols Rounded', 'Material Symbols Outlined' !important;
        font-style: normal !important;
        font-weight: normal !important;
        letter-spacing: normal !important;
        text-transform: none !important;
        display: inline-block !important;
        white-space: nowrap !important;
        word-wrap: normal !important;
        direction: ltr !important;
    }}

    /* Hide default Streamlit header bar & footer decorations */
    header[data-testid="stHeader"] {{
        background: transparent !important;
    }}
    footer {{
        display: none !important;
    }}

    /* Main container constraint */
    .block-container {{
        max-width: 1080px !important;
        padding-top: 1.2rem !important;
        padding-bottom: 3.5rem !important;
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
    }}

    /* Top Brand Navigation Bar */
    .studio-navbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.8rem 1.4rem;
        background: var(--nav-bg);
        border: 1px solid var(--nav-border);
        border-radius: 10px;
        box-shadow: var(--shadow);
        margin-bottom: 1.8rem;
    }}

    .studio-brand {{
        display: flex;
        align-items: center;
        gap: 0.85rem;
        text-decoration: none !important;
    }}

    .studio-brand-img {{
        width: 36px;
        height: 36px;
        object-fit: contain;
    }}

    .studio-brand-fallback {{
        width: 36px;
        height: 36px;
        border-radius: 8px;
        background: var(--bg-secondary);
        border: 1px solid var(--border);
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: 'Cinzel', serif;
        font-size: 1.1rem;
        font-weight: 700;
        color: var(--accent);
    }}

    .studio-brand-title {{
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.35rem;
        font-weight: 700;
        color: var(--text-primary);
        letter-spacing: -0.01em;
        line-height: 1.1;
    }}

    .studio-brand-subtitle {{
        font-size: 0.65rem;
        font-weight: 600;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: var(--accent);
        margin-top: 0.15rem;
    }}

    .studio-nav-links {{
        display: flex;
        gap: 1rem;
        align-items: center;
    }}

    /* Navigation Links: Remove default blue underlines and style cleanly */
    div[data-testid="stMarkdownContainer"] .studio-nav-link,
    div[data-testid="stMarkdownContainer"] .studio-nav-link:link,
    div[data-testid="stMarkdownContainer"] .studio-nav-link:visited,
    .studio-nav-link,
    .studio-nav-link:link,
    .studio-nav-link:visited {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 0.88rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.03em !important;
        color: var(--text-secondary) !important;
        text-decoration: none !important;
        border-bottom: none !important;
        padding: 0.35rem 0.75rem;
        border-radius: 6px;
        transition: all 0.15s ease-in-out;
        cursor: pointer;
    }}

    div[data-testid="stMarkdownContainer"] .studio-nav-link:hover,
    .studio-nav-link:hover {{
        color: var(--accent) !important;
        background-color: var(--bg-secondary) !important;
        text-decoration: none !important;
    }}

    div[data-testid="stMarkdownContainer"] .studio-nav-link.active,
    .studio-nav-link.active {{
        color: var(--accent) !important;
        font-weight: 700 !important;
        text-decoration: none !important;
    }}

    /* Theme Toggle Button */
    .st-key-theme_toggle_btn button {{
        background-color: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border) !important;
        border-radius: 20px !important;
        padding: 0.35rem 0.9rem !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 0.82rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.04em !important;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08) !important;
        transition: all 0.18s ease-in-out !important;
        width: 100% !important;
        height: 38px !important;
    }}

    .st-key-theme_toggle_btn button:hover {{
        background-color: var(--bg-hover) !important;
        border-color: var(--accent) !important;
        color: var(--accent) !important;
        transform: translateY(-1px);
    }}

    /* Hero Section */
    .hero-container {{
        text-align: center;
        padding: 1.8rem 1.2rem 1.6rem 1.2rem;
        margin-bottom: 2rem;
        border-bottom: 1px solid var(--border);
    }}

    .hero-kicker {{
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--accent);
        margin-bottom: 0.7rem;
        display: inline-block;
    }}

    .hero-heading {{
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--text-primary);
        line-height: 1.2;
        letter-spacing: -0.02em;
        margin: 0 auto 0.8rem auto;
        max-width: 760px;
    }}

    .hero-subtext {{
        font-size: 1.02rem;
        color: var(--text-secondary);
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
        font-weight: 400;
    }}

    /* Section Headings */
    .section-header-block {{
        margin-top: 1.8rem;
        margin-bottom: 1.1rem;
    }}

    .section-kicker {{
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: var(--accent);
        margin-bottom: 0.35rem;
    }}

    .section-heading {{
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.55rem;
        font-weight: 600;
        color: var(--text-primary);
        letter-spacing: -0.01em;
        margin: 0;
    }}

    .section-subtext {{
        font-size: 0.9rem;
        color: var(--text-secondary);
        margin-top: 0.25rem;
        line-height: 1.5;
    }}

    /* Workspace / Upload Card */
    .workspace-card {{
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1.6rem;
        box-shadow: var(--shadow);
        margin-bottom: 1.8rem;
    }}

    /* Streamlit File Uploader Override - Clean single dashed dropzone */
    div[data-testid="stFileUploader"] {{
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
    }}

    [data-testid="stFileUploaderDropzone"] {{
        background-color: var(--bg-secondary) !important;
        border: 2px dashed var(--border) !important;
        border-radius: 10px !important;
        padding: 1.6rem 1.2rem !important;
        transition: all 0.2s ease-in-out !important;
    }}

    [data-testid="stFileUploaderDropzone"]:hover {{
        border-color: var(--accent) !important;
        background-color: var(--bg-hover) !important;
    }}

    [data-testid="stFileUploaderDropzone"] div,
    [data-testid="stFileUploaderDropzone"] span,
    [data-testid="stFileUploaderDropzone"] small {{
        color: var(--text-secondary) !important;
    }}

    [data-testid="stFileUploaderDropzone"] button {{
        background-color: var(--bg-card) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border) !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        padding: 0.45rem 1rem !important;
        transition: all 0.15s ease !important;
    }}

    [data-testid="stFileUploaderDropzone"] button:hover {{
        background-color: var(--accent) !important;
        color: var(--btn-primary-text) !important;
        border-color: var(--accent-hover) !important;
    }}

    /* Streamlit Radio & Selectbox Styling */
    div[data-testid="stRadio"] label,
    div[data-testid="stRadio"] [data-testid="stMarkdownContainer"] p {{
        color: var(--text-primary) !important;
        font-weight: 500 !important;
    }}

    div[data-testid="stSelectbox"] label {{
        color: var(--text-secondary) !important;
        font-size: 0.82rem !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
    }}

    div[data-testid="stSelectbox"] > div > div {{
        background-color: var(--bg-card) !important;
        border-color: var(--border) !important;
        color: var(--text-primary) !important;
        border-radius: 8px !important;
    }}

    div[data-testid="stSelectbox"] svg {{
        fill: var(--text-secondary) !important;
    }}

    /* Metadata Badge Bar */
    .meta-bar {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.8rem;
        align-items: center;
        background: var(--bg-secondary);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 0.7rem 1.1rem;
        margin: 1.2rem 0;
    }}

    .meta-item {{
        display: flex;
        align-items: center;
        gap: 0.4rem;
        font-size: 0.83rem;
        color: var(--text-primary);
    }}

    .meta-label {{
        font-weight: 700;
        color: var(--text-secondary);
        text-transform: uppercase;
        font-size: 0.7rem;
        letter-spacing: 0.06em;
    }}

    .meta-value {{
        font-weight: 600;
        color: var(--text-primary);
    }}

    .meta-divider {{
        color: var(--border);
    }}

    /* Archival Photo Card Frame */
    .archival-frame {{
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 1.1rem;
        box-shadow: var(--shadow);
        display: flex;
        flex-direction: column;
        height: 100%;
    }}

    .frame-badge {{
        display: inline-block;
        align-self: flex-start;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        padding: 0.28rem 0.7rem;
        border-radius: 4px;
        margin-bottom: 0.8rem;
    }}

    .frame-badge-original {{
        background: var(--badge-orig-bg);
        color: var(--badge-orig-text);
        border: 1px solid var(--border);
    }}

    .frame-badge-restored {{
        background: var(--badge-rest-bg);
        color: var(--badge-rest-text);
        border: 1px solid var(--badge-rest-text);
    }}

    /* Streamlit Image inside comparison frames */
    div[data-testid="stImage"] img {{
        border-radius: 6px;
        border: 1px solid var(--border);
    }}

    div[data-testid="stImage"] figcaption {{
        color: var(--text-secondary) !important;
        font-size: 0.82rem !important;
        margin-top: 0.5rem !important;
        text-align: center !important;
    }}

    /* Primary Action Button (Restore Photograph) */
    div.stButton:not(.st-key-theme_toggle_btn) > button {{
        background-color: var(--btn-primary-bg) !important;
        color: var(--btn-primary-text) !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 0.98rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.04em !important;
        border: 1px solid var(--btn-primary-hover) !important;
        border-radius: 8px !important;
        padding: 0.7rem 2rem !important;
        box-shadow: 0 3px 12px rgba(0, 0, 0, 0.12) !important;
        transition: all 0.18s ease-in-out !important;
        width: 100%;
    }}

    div.stButton:not(.st-key-theme_toggle_btn) > button:hover {{
        background-color: var(--btn-primary-hover) !important;
        box-shadow: 0 5px 16px rgba(0, 0, 0, 0.2) !important;
        transform: translateY(-1px);
    }}

    div.stButton:not(.st-key-theme_toggle_btn) > button:active {{
        transform: translateY(0px);
    }}

    /* Secondary Action Button (Download Restored Photograph) */
    div.stDownloadButton > button {{
        background-color: var(--btn-secondary-bg) !important;
        color: var(--btn-secondary-text) !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 0.98rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.04em !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        padding: 0.72rem 2rem !important;
        box-shadow: 0 3px 12px rgba(0, 0, 0, 0.12) !important;
        transition: all 0.18s ease-in-out !important;
        width: 100%;
    }}

    div.stDownloadButton > button:hover {{
        background-color: var(--btn-secondary-hover) !important;
        border-color: var(--accent) !important;
        box-shadow: 0 5px 16px rgba(0, 0, 0, 0.22) !important;
        transform: translateY(-1px);
    }}

    /* Success Banner */
    .custom-success-banner {{
        background: var(--success-bg);
        border: 1px solid var(--success-border);
        border-radius: 8px;
        padding: 0.85rem 1.2rem;
        color: var(--success-text);
        font-size: 0.92rem;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin: 1.2rem 0;
    }}

    /* Damage Mask Expander Styling */
    details[data-testid="stExpander"] {{
        background-color: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        box-shadow: var(--shadow) !important;
        margin-top: 1.4rem !important;
        overflow: hidden !important;
    }}

    details[data-testid="stExpander"] summary {{
        background-color: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
        font-family: 'Playfair Display', Georgia, serif !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        padding: 0.85rem 1.2rem !important;
        transition: background 0.15s ease, color 0.15s ease !important;
    }}

    details[data-testid="stExpander"][open] summary {{
        border-bottom: 1px solid var(--border) !important;
    }}

    details[data-testid="stExpander"] summary:hover {{
        color: var(--accent) !important;
        background-color: var(--bg-hover) !important;
    }}

    div[data-testid="stExpanderDetails"] {{
        background-color: var(--bg-card) !important;
        padding: 1.2rem !important;
    }}

    /* Technology Step Cards */
    .tech-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 1rem;
        margin: 1.4rem 0;
    }}

    .tech-card {{
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 1.3rem 1.1rem;
        box-shadow: var(--shadow);
        position: relative;
        transition: transform 0.15s ease, border-color 0.15s ease;
    }}

    .tech-card:hover {{
        border-color: var(--accent);
        transform: translateY(-2px);
    }}

    .tech-step-num {{
        font-family: 'Cinzel', serif;
        font-size: 1.1rem;
        font-weight: 700;
        color: var(--accent);
        margin-bottom: 0.5rem;
        display: block;
    }}

    .tech-step-title {{
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.05rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.4rem;
        line-height: 1.25;
    }}

    .tech-step-desc {{
        font-size: 0.82rem;
        color: var(--text-secondary);
        line-height: 1.5;
        margin: 0;
    }}

    .tech-note-box {{
        background: var(--bg-secondary);
        border: 1px solid var(--border);
        border-left: 4px solid var(--accent);
        border-radius: 6px;
        padding: 0.9rem 1.2rem;
        margin-top: 1.2rem;
        font-size: 0.86rem;
        color: var(--text-primary);
        line-height: 1.55;
    }}

    /* Footer */
    .studio-footer {{
        border-top: 1px solid var(--border);
        margin-top: 3.5rem;
        padding-top: 2rem;
        padding-bottom: 1.5rem;
        text-align: center;
    }}

    .footer-title {{
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.35rem;
    }}

    .footer-tagline {{
        font-size: 0.88rem;
        color: var(--text-secondary);
        margin-bottom: 0.8rem;
    }}

    .footer-credits {{
        font-size: 0.78rem;
        color: var(--text-secondary);
        letter-spacing: 0.04em;
    }}
    /* Targeted contrast fixes for Streamlit download and uploader widgets */
    [data-testid="stDownloadButton"] button,
    div.stDownloadButton button {{
        background-color: var(--btn-secondary-bg) !important;
        color: var(--btn-secondary-text) !important;
        border-color: var(--border) !important;
    }}

    [data-testid="stDownloadButton"] button *,
    div.stDownloadButton button * {{
        color: var(--btn-secondary-text) !important;
        fill: var(--btn-secondary-text) !important;
    }}

    [data-testid="stDownloadButton"] button:hover,
    div.stDownloadButton button:hover {{
        background-color: var(--btn-secondary-hover) !important;
        color: var(--text-primary) !important;
        border-color: var(--accent) !important;
    }}

    [data-testid="stDownloadButton"] button:hover *,
    div.stDownloadButton button:hover * {{
        color: var(--text-primary) !important;
        fill: var(--text-primary) !important;
    }}

    /* The uploader instruction label sits outside the dropzone itself. */
    div[data-testid="stFileUploader"] label,
    div[data-testid="stFileUploader"] [data-testid="stWidgetLabel"],
    div[data-testid="stFileUploader"] [data-testid="stWidgetLabel"] p {{
        color: var(--text-primary) !important;
    }}

    div[data-testid="stFileUploader"] [data-testid="stFileUploaderDropzone"] {{
        background-color: var(--bg-secondary) !important;
        border-color: var(--border) !important;
    }}

    div[data-testid="stFileUploader"] [data-testid="stFileUploaderDropzone"] > div,
    div[data-testid="stFileUploader"] [data-testid="stFileUploaderDropzone"] span,
    div[data-testid="stFileUploader"] [data-testid="stFileUploaderDropzone"] small,
    div[data-testid="stFileUploader"] [data-testid="stFileUploaderDropzone"] p {{
        color: var(--text-secondary) !important;
    }}

    div[data-testid="stFileUploader"] [data-testid="stFileUploaderDropzone"] button {{
        background-color: var(--btn-secondary-bg) !important;
        color: var(--btn-secondary-text) !important;
        border: 1px solid var(--border) !important;
    }}

    div[data-testid="stFileUploader"] [data-testid="stFileUploaderDropzone"] button *,
    div[data-testid="stFileUploader"] [data-testid="stFileUploaderDropzone"] button span {{
        color: var(--btn-secondary-text) !important;
        fill: var(--btn-secondary-text) !important;
    }}

    div[data-testid="stFileUploader"] [data-testid="stFileUploaderDropzone"] button:hover {{
        background-color: var(--btn-secondary-hover) !important;
        border-color: var(--accent) !important;
    }}

    </style>
    """
