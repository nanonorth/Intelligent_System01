import streamlit as st
import numpy as np
from PIL import Image
import os
import json

st.set_page_config(
    page_title="Test NN Model | Painting Style",
    page_icon="🎨",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Mono:wght@300;400;500&display=swap');

html, body, [class*="css"] { font-family: 'Cormorant Garamond', Georgia, serif; }
.stApp { background-color: #0b0907; color: #e8dfd0; }
h1,h2,h3,h4 { font-family: 'Cormorant Garamond', serif !important; }

.hero {
    background: linear-gradient(135deg, #1a1209 0%, #2a1b0e 60%, #0b0907 100%);
    border: 1px solid #2d2217; border-radius: 6px;
    padding: 2.8rem 3rem; margin-bottom: 2rem;
    position: relative; overflow: hidden;
}
.hero::after {
    content: "🎨"; position: absolute; right: 2.5rem; top: 50%;
    transform: translateY(-50%); font-size: 5rem; opacity: 0.08;
}
.hero-label { font-family: 'DM Mono', monospace; font-size: 0.68rem; letter-spacing: 0.22em; color: #c9a84c; text-transform: uppercase; margin-bottom: 0.4rem; }
.hero-title { font-size: 2.8rem; font-weight: 300; color: #f0e4c8; line-height: 1.15; margin: 0 0 0.4rem 0; }
.hero-title em { color: #c9a84c; font-style: italic; }
.hero-sub { color: #7a6a50; font-size: 1rem; font-style: italic; }

.status-ok { background: rgba(80,160,100,0.1); border: 1px solid rgba(80,160,100,0.3); color: #7ac890; padding: 0.6rem 1.2rem; border-radius: 4px; font-family: 'DM Mono', monospace; font-size: 0.82rem; letter-spacing: 0.06em; display: inline-flex; align-items: center; gap: 0.5rem; }
.status-warn { background: rgba(200,140,60,0.1); border: 1px solid rgba(200,140,60,0.3); color: #c8a060; padding: 0.6rem 1.2rem; border-radius: 4px; font-family: 'DM Mono', monospace; font-size: 0.82rem; letter-spacing: 0.06em; }

.result-card { background: linear-gradient(145deg, #16120c, #1e1810); border: 1px solid #3d2e18; border-radius: 6px; padding: 2rem; height: 100%; }
.result-label { font-family: 'DM Mono', monospace; font-size: 0.65rem; letter-spacing: 0.2em; color: #6b5a3a; text-transform: uppercase; margin-bottom: 0.5rem; }
.result-main { font-size: 2.4rem; font-weight: 300; color: #e8c87a; margin-bottom: 0.2rem; line-height: 1.2; }
.result-conf { font-family: 'DM Mono', monospace; font-size: 0.9rem; color: #9e7840; }

.bar-wrap { margin-top: 1.5rem; }
.bar-row { display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.85rem; }
.bar-name { font-family: 'DM Mono', monospace; font-size: 0.78rem; color: #9e8c72; width: 120px; flex-shrink: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.bar-track { flex: 1; height: 6px; background: #1e1810; border-radius: 3px; overflow: hidden; }
.bar-fill { height: 100%; border-radius: 3px; }
.bar-pct { font-family: 'DM Mono', monospace; font-size: 0.78rem; color: #6b5a3a; width: 42px; text-align: right; flex-shrink: 0; }
.bar-rank-1 .bar-fill { background: linear-gradient(90deg, #c9a84c, #e8c87a); }
.bar-rank-2 .bar-fill { background: linear-gradient(90deg, #7a6a52, #a08860); }
.bar-rank-3 .bar-fill { background: linear-gradient(90deg, #3d3028, #5a4830); }
.bar-other .bar-fill  { background: #2d2217; }
.bar-rank-1 .bar-name { color: #e8c87a; }

.chips { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.5rem; }
.chip { background: rgba(180,130,60,0.1); border: 1px solid rgba(180,130,60,0.25); color: #a08040; padding: 0.25rem 0.7rem; border-radius: 20px; font-family: 'DM Mono', monospace; font-size: 0.72rem; letter-spacing: 0.06em; }

.sec-label { font-family: 'DM Mono', monospace; font-size: 0.65rem; letter-spacing: 0.2em; color: #c9a84c; text-transform: uppercase; margin-bottom: 0.2rem; }
.sec-title { font-size: 1.6rem; font-weight: 300; color: #e8dfd0; margin: 0 0 1.2rem 0; border-bottom: 1px solid #1e1810; padding-bottom: 0.6rem; }

#MainMenu, footer, header { visibility: hidden; }
.stSpinner > div { border-top-color: #c9a84c !important; }
            
/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f0d0a 0%, #130f08 60%, #0f0d0a 100%) !important;
    border-right: 1px solid rgba(201,168,76,0.15) !important;
}
[data-testid="stSidebar"] > div:first-child {
    padding-top: 0 !important;
}
[data-testid="stSidebarNav"] a {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.7rem !important;
    letter-spacing: 0.14em !important;
    text-transform: uppercase !important;
    color: rgba(160,128,64,0.55) !important;
    padding: 0.55rem 1rem !important;
    border-radius: 4px !important;
    transition: all 0.25s ease !important;
    border-left: 2px solid transparent !important;
}
[data-testid="stSidebarNav"] a:hover {
    color: #c9a84c !important;
    background: rgba(201,168,76,0.06) !important;
    border-left-color: rgba(201,168,76,0.3) !important;
}
[data-testid="stSidebarNav"] a[aria-current="page"] {
    color: #c9a84c !important;
    background: rgba(201,168,76,0.1) !important;
    border-left: 2px solid #c9a84c !important;
}
[data-testid="collapsedControl"] svg {
    color: rgba(201,168,76,0.4) !important;
}
[data-testid="stSidebar"]::-webkit-scrollbar { width: 2px; }
[data-testid="stSidebar"]::-webkit-scrollbar-track { background: transparent; }
[data-testid="stSidebar"]::-webkit-scrollbar-thumb {
    background: rgba(201,168,76,0.2);
    border-radius: 2px;
}
            
</style>
""", unsafe_allow_html=True)

# ─── MODEL SETUP ──────────────────────────────────────────────────────────────
MODEL_PATH   = os.path.join(os.path.dirname(__file__), "../../models/cnn_model.h5")
CLASSES_PATH = os.path.join(os.path.dirname(__file__), "../../models/painting_classes.json")

@st.cache_resource
def load_model():
    if os.path.exists(MODEL_PATH):
        import tensorflow as tf
        m = tf.keras.models.load_model(MODEL_PATH)
        classes = json.load(open(CLASSES_PATH)) if os.path.exists(CLASSES_PATH) else []
        return m, classes
    return None, []

model, CLASSES = load_model()

def preprocess_image(image):
    img = image.resize((224, 224))
    arr = np.array(img) / 255.0
    return np.expand_dims(arr, axis=0)

ARTIST_META = {
    'Vincent_van_Gogh':       {'emoji': '🌻', 'label': 'Vincent van Gogh',      'era': 'Post-Impressionism'},
    'Edgar_Degas':            {'emoji': '🩰', 'label': 'Edgar Degas',            'era': 'Impressionism'},
    'Pablo_Picasso':          {'emoji': '🎭', 'label': 'Pablo Picasso',          'era': 'Cubism'},
    'Pierre-Auguste_Renoir':  {'emoji': '🌸', 'label': 'Pierre-Auguste Renoir', 'era': 'Impressionism'},
    'Albrecht_Durer':         {'emoji': '✒️', 'label': 'Albrecht Dürer',         'era': 'Northern Renaissance'},
    'Paul_Gauguin':           {'emoji': '🌴', 'label': 'Paul Gauguin',           'era': 'Post-Impressionism'},
    'Francisco_Goya':         {'emoji': '🖤', 'label': 'Francisco Goya',         'era': 'Romanticism'},
    'Rembrandt':              {'emoji': '🕯️', 'label': 'Rembrandt',              'era': 'Dutch Golden Age'},
    'Alfred_Sisley':          {'emoji': '🌊', 'label': 'Alfred Sisley',          'era': 'Impressionism'},
    'Titian':                 {'emoji': '👑', 'label': 'Titian',                 'era': 'Venetian Renaissance'},
}

def get_meta(class_name):
    return ARTIST_META.get(class_name, {'emoji': '🎨', 'label': class_name.replace('_', ' '), 'era': ''})

# ─── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-label">Neural Network · Painting Classifier</div>
  <div class="hero-title">Identify the <em>Master</em><br>Behind the Brushstroke</div>
  <div class="hero-sub">อัปโหลดภาพวาด — โมเดลจะบอกว่าเป็นสไตล์ของศิลปินคนใด</div>
</div>
""", unsafe_allow_html=True)

if model is None:
    st.markdown('<div class="status-warn">⚠️ &nbsp;ยังไม่มีโมเดล — กรุณา train โมเดลก่อนโดยรัน <code>notebooks/04_neural_network.ipynb</code></div>', unsafe_allow_html=True)
else:
    n = len(CLASSES)
    st.markdown(f'<div class="status-ok">✦ &nbsp;โมเดลพร้อมใช้งาน · {n} ศิลปิน Vincent van Gogh, Edgar Degas,Pablo Picasso,Pierre-Auguste Renoir,Albrecht Dürer,Paul Gauguin,Francisco Goya,Rembrandt,Alfred Sisley,Titian</div>' , unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"""
<div class="chips">
  <span class="chip">{len(CLASSES)} Artists</span>
  <span class="chip">Neural Network</span>
  <span class="chip">MobileNetV2</span>
  <span class="chip">Transfer Learning</span>
  <span class="chip">224 × 224 px</span>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown('<p class="sec-label">วิเคราะห์ภาพ</p><h2 class="sec-title">อัปโหลดภาพวาด</h2>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("อัปโหลดรูปภาพ", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    col_img, col_res = st.columns([1, 1], gap="large")

    with col_img:
        st.markdown('<p class="sec-label">ภาพที่อัปโหลด</p>', unsafe_allow_html=True)
        st.image(image, use_container_width=True)
        w, h = image.size
        st.markdown(f'<div style="font-family:\'DM Mono\',monospace;font-size:0.72rem;color:#3d2e18;margin-top:0.5rem;">{uploaded_file.name} · {w}×{h}px · {uploaded_file.size/1024:.1f} KB</div>', unsafe_allow_html=True)

    with col_res:
        if model is None:
            st.markdown('<div class="result-card" style="display:flex;align-items:center;justify-content:center;min-height:300px;"><div style="text-align:center;color:#3d2e18;"><div style="font-size:2.5rem;margin-bottom:1rem;">⚙️</div><div style="font-style:italic;">กรุณา train โมเดลก่อน</div></div></div>', unsafe_allow_html=True)
        else:
            with st.spinner("กำลังวิเคราะห์..."):
                processed    = preprocess_image(image)
                predictions  = model.predict(processed)[0]
                top_idx      = np.argsort(predictions)[::-1]
                predicted_idx = top_idx[0]

            predicted_name = CLASSES[predicted_idx] if CLASSES else f"Class {predicted_idx}"
            meta      = get_meta(predicted_name)
            top_conf  = predictions[predicted_idx]

            bars_html = ""
            for rank, idx in enumerate(top_idx):
                cn   = CLASSES[idx] if idx < len(CLASSES) else f"Class {idx}"
                prob = predictions[idx]
                m    = get_meta(cn)
                pct  = prob * 100
                bar_class = f"bar-rank-{rank+1}" if rank < 3 else "bar-other"
                bars_html += f'<div class="bar-row {bar_class}"><div class="bar-name" title="{m["label"]}">{m["emoji"]} {m["label"]}</div><div class="bar-track"><div class="bar-fill" style="width:{pct:.1f}%"></div></div><div class="bar-pct">{pct:.1f}%</div></div>'

            st.markdown(f"""
<div class="result-card">
  <div class="result-label">การวิเคราะห์สไตล์</div>
  <div class="result-main">{meta['emoji']} {meta['label']}</div>
  <div style="color:#6b5a3a;font-style:italic;font-size:0.95rem;margin-bottom:0.5rem;">{meta['era']}</div>
  <div class="result-conf">ความมั่นใจ: {top_conf:.1%}</div>
  <div class="bar-wrap">
    <div style="font-family:'DM Mono',monospace;font-size:0.65rem;letter-spacing:0.2em;color:#3d2e18;text-transform:uppercase;margin-bottom:0.8rem;">Probability Distribution</div>
    {bars_html}
  </div>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="sec-label">อันดับสูงสุด</p><h2 class="sec-title">Top 3 Predictions</h2>', unsafe_allow_html=True)

    top3 = top_idx[:3]
    cols3 = st.columns(3, gap="medium")
    rank_labels  = ["🥇 อันดับ 1", "🥈 อันดับ 2", "🥉 อันดับ 3"]
    rank_borders = ["#c9a84c", "#9e9e9e", "#cd7f32"]

    for rank, (col, idx) in enumerate(zip(cols3, top3)):
        cn   = CLASSES[idx] if idx < len(CLASSES) else f"Class {idx}"
        prob = predictions[idx]
        m    = get_meta(cn)
        with col:
            st.markdown(f"""
<div style="background:#131008;border:1px solid {rank_borders[rank]}44;border-top:3px solid {rank_borders[rank]};border-radius:6px;padding:1.4rem;text-align:center;">
  <div style="font-size:0.75rem;color:{rank_borders[rank]};font-family:'DM Mono',monospace;letter-spacing:0.1em;margin-bottom:0.6rem;">{rank_labels[rank]}</div>
  <div style="font-size:2.5rem;margin-bottom:0.4rem;">{m['emoji']}</div>
  <div style="font-size:1.05rem;color:#e8dfd0;font-weight:600;margin-bottom:0.2rem;">{m['label']}</div>
  <div style="font-style:italic;color:#6b5a3a;font-size:0.85rem;margin-bottom:0.8rem;">{m['era']}</div>
  <div style="font-family:'DM Mono',monospace;font-size:1.4rem;color:{rank_borders[rank]};">{prob:.1%}</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div style="text-align:center;padding:3rem 0 1.5rem 0;color:#2d2217;font-family:\'DM Mono\',monospace;font-size:0.68rem;letter-spacing:0.12em;">PAINTING STYLE CLASSIFIER · NEURAL NETWORK · MOBILENETV2</div>', unsafe_allow_html=True)