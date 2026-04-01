import streamlit as st
import numpy as np
from PIL import Image
import joblib
import os

st.set_page_config(
    page_title="Test NN Model | Painting Style",
    page_icon="🌸",
    layout="wide"
)

# ─── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Mono:wght@300;400;500&display=swap');
 
html, body, [class*="css"] {
    font-family: 'Cormorant Garamond', Georgia, serif;
}
.stApp { background-color: #0b0907; color: #e8dfd0; }
h1,h2,h3,h4 { font-family: 'Cormorant Garamond', serif !important; }
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stFileUploader"] label { display: none; }
[data-testid="stFileUploader"] {
    background: #131008;
    border: 1.5px dashed #2d2217;
    border-radius: 6px;
}
.stSpinner > div { border-top-color: #c9a84c !important; }
 
/* ── Hero ── */
.hero {
    background: linear-gradient(135deg, #0e160a 0%, #1a2a0e 55%, #0b0907 100%);
    border: 1px solid #1e2d17;
    border-radius: 6px;
    padding: 2.8rem 3rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.hero::after {
    content: "🌸";
    position: absolute;
    right: 2.5rem; top: 50%;
    transform: translateY(-50%);
    font-size: 5rem;
    opacity: 0.12;
}
.hero-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.22em;
    color: #7ac870;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}
.hero-title {
    font-size: 2.8rem;
    font-weight: 300;
    color: #f0f4e8;
    line-height: 1.15;
    margin: 0 0 0.4rem 0;
}
.hero-title em { color: #9ed878; font-style: italic; }
.hero-sub { color: #6a7a50; font-size: 1rem; font-style: italic; }
 
/* ── Status ── */
.status-ok {
    background: rgba(80,160,100,0.1);
    border: 1px solid rgba(80,160,100,0.3);
    color: #7ac890;
    padding: 0.6rem 1.2rem;
    border-radius: 4px;
    font-family: 'DM Mono', monospace;
    font-size: 0.82rem;
    letter-spacing: 0.06em;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}
.status-warn {
    background: rgba(200,140,60,0.1);
    border: 1px solid rgba(200,140,60,0.3);
    color: #c8a060;
    padding: 0.6rem 1.2rem;
    border-radius: 4px;
    font-family: 'DM Mono', monospace;
    font-size: 0.82rem;
    letter-spacing: 0.06em;
}
 
/* ── Chips ── */
.chips { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.5rem; }
.chip {
    background: rgba(120,180,80,0.1);
    border: 1px solid rgba(120,180,80,0.25);
    color: #7aaa50;
    padding: 0.25rem 0.7rem;
    border-radius: 20px;
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.06em;
}
 
/* ── Section ── */
.sec-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    color: #7ac870;
    text-transform: uppercase;
    margin-bottom: 0.2rem;
}
.sec-title {
    font-size: 1.6rem;
    font-weight: 300;
    color: #e8dfd0;
    margin: 0 0 1.2rem 0;
    border-bottom: 1px solid #181e10;
    padding-bottom: 0.6rem;
}
 
/* ── Result card ── */
.result-card {
    background: linear-gradient(145deg, #0e140a, #141e0e);
    border: 1px solid #1e2d17;
    border-radius: 6px;
    padding: 2rem;
    height: 100%;
}
.result-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    color: #4a6a3a;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}
.result-main {
    font-size: 2.4rem;
    font-weight: 300;
    color: #b8e870;
    margin-bottom: 0.2rem;
    line-height: 1.2;
}
.result-conf {
    font-family: 'DM Mono', monospace;
    font-size: 0.9rem;
    color: #6a9840;
}
 
/* ── Bars ── */
.bar-wrap { margin-top: 1.5rem; }
.bar-row {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    margin-bottom: 0.85rem;
}
.bar-name {
    font-family: 'DM Mono', monospace;
    font-size: 0.78rem;
    color: #7a8c72;
    width: 110px;
    flex-shrink: 0;
}
.bar-track {
    flex: 1;
    height: 6px;
    background: #141e0e;
    border-radius: 3px;
    overflow: hidden;
}
.bar-fill { height: 100%; border-radius: 3px; }
.bar-pct {
    font-family: 'DM Mono', monospace;
    font-size: 0.78rem;
    color: #4a6a3a;
    width: 42px;
    text-align: right;
    flex-shrink: 0;
}
.bar-rank-1 .bar-fill { background: linear-gradient(90deg, #6ab840, #9ed860); }
.bar-rank-2 .bar-fill { background: linear-gradient(90deg, #4a7830, #6a9840); }
.bar-rank-3 .bar-fill { background: linear-gradient(90deg, #283818, #3a5828); }
.bar-other  .bar-fill { background: #1e2d17; }
.bar-rank-1 .bar-name { color: #9ed860; }
 
/* ── Rank cards ── */
.rank-card {
    background: #0e140a;
    border-radius: 6px;
    padding: 1.4rem;
    text-align: center;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a0f07 0%, #0d1409 60%, #0a0f07 100%) !important;
    border-right: 1px solid rgba(106,184,64,0.15) !important;
}
[data-testid="stSidebar"] > div:first-child {
    padding-top: 0 !important;
}
[data-testid="stSidebarNav"] a {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.7rem !important;
    letter-spacing: 0.14em !important;
    text-transform: uppercase !important;
    color: rgba(74,120,48,0.7) !important;
    padding: 0.55rem 1rem !important;
    border-radius: 4px !important;
    transition: all 0.25s ease !important;
    border-left: 2px solid transparent !important;
}
[data-testid="stSidebarNav"] a:hover {
    color: #9ed860 !important;
    background: rgba(106,184,64,0.06) !important;
    border-left-color: rgba(106,184,64,0.3) !important;
}
[data-testid="stSidebarNav"] a[aria-current="page"] {
    color: #9ed860 !important;
    background: rgba(106,184,64,0.1) !important;
    border-left: 2px solid #6ab840 !important;
}
[data-testid="collapsedControl"] svg {
    color: rgba(106,184,64,0.4) !important;
}
[data-testid="stSidebar"]::-webkit-scrollbar { width: 2px; }
[data-testid="stSidebar"]::-webkit-scrollbar-track { background: transparent; }
[data-testid="stSidebar"]::-webkit-scrollbar-thumb {
    background: rgba(106,184,64,0.2);
    border-radius: 2px;
}       

</style>
""", unsafe_allow_html=True)

# ─── MODEL SETUP ──────────────────────────────────────────────────────────────
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../../models/ensemble_model.pkl")

@st.cache_resource
def load_model():
    if os.path.exists(MODEL_PATH):
        data = joblib.load(MODEL_PATH)
        return data['model'], data['scaler'], data['label_encoder'], data['pca']
    return None, None, None, None

model, scaler, le, pca = load_model()

def extract_features(img_array):
    from skimage.feature import hog, local_binary_pattern
    from skimage.color import rgb2gray
    img_resized = np.array(Image.fromarray(img_array).resize((128, 128)))
    gray = rgb2gray(img_resized)
    hog_features = hog(gray, orientations=9, pixels_per_cell=(8, 8),
                       cells_per_block=(2, 2), feature_vector=True)
    color_features = []
    for channel in range(3):
        hist, _ = np.histogram(img_resized[:, :, channel], bins=32, range=(0, 256))
        color_features.extend(hist / (hist.sum() + 1e-7))
    lbp = local_binary_pattern(gray, P=8, R=1, method='uniform')
    lbp_hist, _ = np.histogram(lbp, bins=10, range=(0, 10))
    lbp_feat = lbp_hist / (lbp_hist.sum() + 1e-7)
    return np.concatenate([hog_features, color_features, lbp_feat])

# ─── FLOWER METADATA ──────────────────────────────────────────────────────────
FLOWER_META = {
    'daisy':     {'emoji': '🌼', 'label': 'Daisy',     'th': 'เดซี่',       'color': '#f0d060'},
    'dandelion': {'emoji': '🌻', 'label': 'Dandelion', 'th': 'แดนดิไลออน',  'color': '#e8c040'},
    'rose':      {'emoji': '🌹', 'label': 'Rose',      'th': 'กุหลาบ',      'color': '#e87878'},
    'sunflower': {'emoji': '🌞', 'label': 'Sunflower', 'th': 'ทานตะวัน',    'color': '#f0a030'},
    'tulip':     {'emoji': '🌷', 'label': 'Tulip',     'th': 'ทิวลิป',      'color': '#d870c0'},
}

def get_meta(name):
    return FLOWER_META.get(name, {'emoji': '🌺', 'label': name, 'th': name, 'color': '#9ed860'})

# ─── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-label">Ensemble ML · Flower Classifier</div>
  <div class="hero-title">Name That <em>Flower</em><br>in a Single Glance</div>
  <div class="hero-sub">อัปโหลดรูปดอกไม้ — Stacking Ensemble จะจำแนกให้ทันที</div>
</div>
""", unsafe_allow_html=True)

# ─── STATUS ───────────────────────────────────────────────────────────────────
if model is None:
    st.markdown("""
<div class="status-warn">
  ⚠️ &nbsp;ยังไม่มีโมเดล — กรุณา train โมเดลก่อนโดยรัน
  <code>notebooks/02_ensemble_ml.ipynb</code>
</div>
""", unsafe_allow_html=True)
else:
    st.markdown('<div class="status-ok">✦ &nbsp;โมเดลพร้อมใช้งาน</div>', unsafe_allow_html=True)
 
st.markdown("<br>", unsafe_allow_html=True)
 
st.markdown("""
<div class="chips">
  <span class="chip">5 Classes</span>
  <span class="chip">Stacking Classifier</span>
  <span class="chip">RF · ET · SVM · XGB · LGBM</span>
  <span class="chip">HOG · Color Hist · LBP · Gabor</span>
  <span class="chip">128 × 128 px</span>
</div>
""", unsafe_allow_html=True)
 
st.markdown("---")
 
# ─── FLOWER GUIDE ─────────────────────────────────────────────────────────────
st.markdown(
    '<p class="sec-label">ดอกไม้ที่รองรับ</p>'
    '<h2 class="sec-title">5 ประเภทที่จำแนกได้</h2>',
    unsafe_allow_html=True
)
 
guide_cols = st.columns(5, gap="small")
for col, (key, m) in zip(guide_cols, FLOWER_META.items()):
    with col:
        st.markdown(f"""
<div style="background:#0e140a; border:1px solid #1e2d17;
     border-top:3px solid {m['color']}66; border-radius:6px;
     padding:1rem; text-align:center;">
  <div style="font-size:2rem; margin-bottom:0.4rem;">{m['emoji']}</div>
  <div style="font-size:0.95rem; font-weight:600; color:#e8dfd0;">{m['label']}</div>
  <div style="font-size:0.82rem; color:#4a6a3a; font-style:italic;">{m['th']}</div>
</div>
""", unsafe_allow_html=True)
 
st.markdown("<br>", unsafe_allow_html=True)

# ─── UPLOAD SECTION ───────────────────────────────────────────────────────────
st.markdown('<p class="sec-label">วิเคราะห์ภาพ</p><h2 class="sec-title">อัปโหลดภาพวาด</h2>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "อัปโหลดรูปภาพ",
    type=["jpg", "jpeg", "png"],
    help="รองรับ JPG, JPEG, PNG"
)

# ─── PREDICTION ───────────────────────────────────────────────────────────────
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    col_img, col_res = st.columns([1, 1], gap="large")
 
    with col_img:
        st.markdown('<p class="sec-label">ภาพที่อัปโหลด</p>', unsafe_allow_html=True)
        st.image(image, use_container_width=True)
        w, h = image.size
        st.markdown(f"""
<div style="font-family:'DM Mono',monospace; font-size:0.72rem;
            color:#2d3a20; margin-top:0.5rem;">
  {uploaded_file.name} · {w}×{h}px · {uploaded_file.size/1024:.1f} KB
</div>
""", unsafe_allow_html=True)
 
    with col_res:
        if model is None:
            st.markdown("""
<div class="result-card" style="display:flex;align-items:center;
     justify-content:center;min-height:300px;">
  <div style="text-align:center;color:#2d3a20;">
    <div style="font-size:2.5rem;margin-bottom:1rem;">⚙️</div>
    <div style="font-style:italic;">กรุณา train โมเดลก่อน</div>
  </div>
</div>
""", unsafe_allow_html=True)
        else:
            with st.spinner("กำลังวิเคราะห์..."):
                img_array     = np.array(image)
                features      = extract_features(img_array).reshape(1, -1)
                feat_sc       = scaler.transform(features)
                feat_pca      = pca.transform(feat_sc)
                prediction    = model.predict(feat_pca)[0]
                probabilities = model.predict_proba(feat_pca)[0]
 
            predicted_name = le.inverse_transform([prediction])[0]
            top_idx  = np.argsort(probabilities)[::-1]
            meta     = get_meta(predicted_name)
            top_conf = probabilities[top_idx[0]]
 
            st.markdown(f"""
<div class="result-card">
  <div class="result-label">ผลการจำแนก</div>
  <div class="result-main">{meta['emoji']} {meta['label']}</div>
  <div style="color:#4a6a3a; font-style:italic; font-size:0.95rem;
              margin-bottom:0.5rem;">{meta['th']}</div>
  <div class="result-conf">ความมั่นใจ: {top_conf:.1%}</div>
  <div class="bar-wrap">
    <div style="font-family:'DM Mono',monospace; font-size:0.65rem;
                letter-spacing:0.2em; color:#2d3a20;
                text-transform:uppercase; margin-bottom:0.8rem;">
      Probability Distribution
    </div>
""", unsafe_allow_html=True)
 
            bars_html = ""
            for rank, idx in enumerate(top_idx):
                cn   = le.classes_[idx]
                prob = probabilities[idx]
                m    = get_meta(cn)
                pct  = prob * 100
                bar_class = f"bar-rank-{rank+1}" if rank < 3 else "bar-other"
                bars_html += f"""
<div class="bar-row {bar_class}">
  <div class="bar-name">{m['emoji']} {m['label']}</div>
  <div class="bar-track">
    <div class="bar-fill" style="width:{pct:.1f}%"></div>
  </div>
  <div class="bar-pct">{pct:.1f}%</div>
</div>"""
 
            st.markdown(bars_html + "</div></div>", unsafe_allow_html=True)
 
    # ── TOP 3 ─────────────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        '<p class="sec-label">อันดับสูงสุด</p>'
        '<h2 class="sec-title">Top 3 Predictions</h2>',
        unsafe_allow_html=True
    )
 
    rank_labels  = ["🥇 อันดับ 1", "🥈 อันดับ 2", "🥉 อันดับ 3"]
    rank_borders = ["#9ed860",     "#7a9a60",     "#5a7840"]
 
    cols3 = st.columns(3, gap="medium")
    for rank, (col, idx) in enumerate(zip(cols3, top_idx[:3])):
        cn   = le.classes_[idx]
        prob = probabilities[idx]
        m    = get_meta(cn)
        with col:
            st.markdown(f"""
<div class="rank-card"
     style="border:1px solid {rank_borders[rank]}44;
            border-top:3px solid {rank_borders[rank]};">
  <div style="font-size:0.75rem; color:{rank_borders[rank]};
              font-family:'DM Mono',monospace;
              letter-spacing:0.1em; margin-bottom:0.6rem;">{rank_labels[rank]}</div>
  <div style="font-size:2.5rem; margin-bottom:0.4rem;">{m['emoji']}</div>
  <div style="font-size:1.05rem; color:#e8dfd0;
              font-weight:600; margin-bottom:0.15rem;">{m['label']}</div>
  <div style="font-style:italic; color:#4a6a3a;
              font-size:0.85rem; margin-bottom:0.8rem;">{m['th']}</div>
  <div style="font-family:'DM Mono',monospace;
              font-size:1.4rem; color:{rank_borders[rank]};">{prob:.1%}</div>
</div>
""", unsafe_allow_html=True)
 
# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding:3rem 0 1.5rem 0;
            color:#1e2d17; font-family:'DM Mono',monospace;
            font-size:0.68rem; letter-spacing:0.12em;">
  FLOWER CLASSIFIER · STACKING ENSEMBLE ML · 5 CLASSES
</div>
""", unsafe_allow_html=True)