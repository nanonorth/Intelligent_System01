import streamlit as st

st.set_page_config(
    page_title="Image Classification Project",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Mono:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Cormorant Garamond', Georgia, serif;
}
.stApp { background-color: #0b0907; color: #e8dfd0; }
h1,h2,h3,h4 { font-family: 'Cormorant Garamond', serif !important; }
#MainMenu, footer, header { visibility: hidden; }

/* ── Hero ── */
.hero {
    position: relative;
    background: linear-gradient(135deg, #1a1209 0%, #2a1b0e 55%, #0b0907 100%);
    border: 1px solid #2d2217;
    border-radius: 8px;
    padding: 3.5rem 3.5rem 3rem 3.5rem;
    margin-bottom: 2.5rem;
    overflow: hidden;
}
.hero::before {
    content: "";
    position: absolute;
    top: -60px; right: -60px;
    width: 320px; height: 320px;
    background: radial-gradient(circle, rgba(201,168,76,0.1) 0%, transparent 65%);
    border-radius: 50%;
    pointer-events: none;
}
.hero-eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.24em;
    color: #c9a84c;
    text-transform: uppercase;
    margin-bottom: 0.7rem;
}
.hero-title {
    font-size: 3.4rem;
    font-weight: 300;
    color: #f0e4c8;
    line-height: 1.1;
    margin: 0 0 0.5rem 0;
    letter-spacing: 0.02em;
}
.hero-title em { color: #c9a84c; font-style: italic; }
.hero-desc {
    color: #7a6a50;
    font-size: 1.1rem;
    font-style: italic;
    max-width: 540px;
    line-height: 1.7;
    margin-top: 0.8rem;
}
.hero-badges {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin-top: 1.6rem;
}
.badge {
    background: rgba(201,168,76,0.1);
    border: 1px solid rgba(201,168,76,0.28);
    color: #a08040;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.08em;
}

/* ── Section ── */
.sec-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.22em;
    color: #c9a84c;
    text-transform: uppercase;
    margin-bottom: 0.25rem;
}
.sec-title {
    font-size: 1.7rem;
    font-weight: 300;
    color: #e8dfd0;
    margin: 0 0 1.5rem 0;
    border-bottom: 1px solid #1e1810;
    padding-bottom: 0.65rem;
}

/* ── Model cards ── */
.model-card {
    background: linear-gradient(145deg, #131008, #1a1510);
    border: 1px solid #2d2217;
    border-radius: 8px;
    padding: 2rem;
    height: 100%;
    transition: border-color 0.25s, transform 0.2s;
    position: relative;
    overflow: hidden;
}
.model-card::before {
    content: "";
    position: absolute;
    bottom: -30px; right: -30px;
    width: 120px; height: 120px;
    border-radius: 50%;
    opacity: 0.06;
}
.model-card.ml::before { background: #4c9be8; }
.model-card.nn::before { background: #e87a4c; }
.model-card:hover {
    border-color: #5a3e1e;
    transform: translateY(-3px);
}
.model-icon { font-size: 2.4rem; margin-bottom: 0.8rem; }
.model-tag {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}
.model-tag.ml { color: #7aaac8; }
.model-tag.nn { color: #d0924c; }
.model-name {
    font-size: 1.5rem;
    font-weight: 600;
    color: #e8dfd0;
    margin-bottom: 0.3rem;
}
.model-dataset {
    font-style: italic;
    color: #6b5a3a;
    font-size: 0.92rem;
    margin-bottom: 1rem;
}
.model-desc {
    color: #7a6a52;
    font-size: 0.95rem;
    line-height: 1.75;
    margin-bottom: 1.2rem;
}
.model-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
}
.pill {
    background: #1e1810;
    border: 1px solid #2d2217;
    color: #5a4a32;
    padding: 0.18rem 0.6rem;
    border-radius: 3px;
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.05em;
}

/* ── Nav cards ── */
.nav-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.75rem;
}
.nav-card {
    background: #131008;
    border: 1px solid #2d2217;
    border-radius: 6px;
    padding: 1.2rem 1.4rem;
    display: flex;
    align-items: flex-start;
    gap: 0.9rem;
    transition: border-color 0.2s;
    text-decoration: none;
}
.nav-card:hover { border-color: #5a3e1e; }
.nav-icon { font-size: 1.4rem; flex-shrink: 0; margin-top: 0.1rem; }
.nav-name {
    font-size: 1rem;
    font-weight: 600;
    color: #e8dfd0;
    margin-bottom: 0.15rem;
}
.nav-desc { font-size: 0.85rem; color: #5a4a32; font-style: italic; }

/* ── Stats row ── */
.stats-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0.75rem;
    margin-bottom: 2rem;
}
.stat-tile {
    background: #131008;
    border: 1px solid #1e1810;
    border-radius: 6px;
    padding: 1.1rem;
    text-align: center;
}
.stat-num {
    font-family: 'DM Mono', monospace;
    font-size: 1.8rem;
    font-weight: 300;
    color: #c9a84c;
    display: block;
    line-height: 1.2;
}
.stat-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.12em;
    color: #3d2e18;
    text-transform: uppercase;
    margin-top: 0.2rem;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f0d0a 0%, #130f08 60%, #0f0d0a 100%) !important;
    border-right: 1px solid rgba(201,168,76,0.15) !important;
}
.sidebar-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.1rem;
    font-weight: 300;
    color: #9ed860;
    letter-spacing: 0.08em;
    line-height: 1.3;
    margin-bottom: 0.25rem;
}
.sidebar-sub {
    font-family: 'DM Mono', monospace;
    font-size: 0.58rem;
    letter-spacing: 0.16em;
    color: rgba(74,120,48,0.6);
    text-transform: uppercase;
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

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-eyebrow">Image Classification Project</div>
  <div class="hero-title">See the World<br>Through <em>Intelligent</em> Eyes</div>
  <div class="hero-desc">
    โปรเจคนี้พัฒนาโมเดล Machine Learning 2 ประเภท<br>
    เพื่อจำแนกภาพวาดสไตล์ศิลปิน และประเภทของดอกไม้
  </div>
  <div class="hero-badges">
    <span class="badge">Ensemble ML</span>
    <span class="badge">Neural Network</span>
    <span class="badge">Painting Style</span>
    <span class="badge">Flower Classification</span>
    <span class="badge">Transfer Learning</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── STATS ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-row">
  <div class="stat-tile"><span class="stat-num">2</span><span class="stat-label">Models</span></div>
  <div class="stat-tile"><span class="stat-num">5</span><span class="stat-label">ML Base Learners</span></div>
  <div class="stat-tile"><span class="stat-num">10</span><span class="stat-label">Artists</span></div>
  <div class="stat-tile"><span class="stat-num">5</span><span class="stat-label">Flower Classes</span></div>
</div>
""", unsafe_allow_html=True)

# ── MODELS ────────────────────────────────────────────────────────────────────
st.markdown('<p class="sec-label">โมเดล</p><h2 class="sec-title">2 Models · 2 Datasets</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
<div class="model-card ml">
  <div class="model-icon">🤖</div>
  <div class="model-tag ml">Model 01 · Ensemble ML</div>
  <div class="model-name">Stacking Classifier</div>
  <div class="model-dataset">Dataset: Flower Recognition</div>
  <div class="model-desc">
    รวม 5 โมเดลผ่าน StackingClassifier —
    RF, ExtraTrees, SVM, XGBoost, LightGBM —
    meta-learner คือ Logistic Regression<br><br>
    Feature extraction ด้วย HOG, Color Histogram (RGB+HSV),
    Multi-radius LBP, Gabor Texture และ Statistical Moments
  </div>
  <div class="model-pills">
    <span class="pill">Random Forest</span>
    <span class="pill">Extra Trees</span>
    <span class="pill">SVM · RBF</span>
    <span class="pill">XGBoost</span>
    <span class="pill">LightGBM</span>
    <span class="pill">HOG · LBP · Gabor</span>
  </div>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="model-card nn">
  <div class="model-icon">🧠</div>
  <div class="model-tag nn">Model 02 · Neural Network</div>
  <div class="model-name">EfficientNetB0</div>
  <div class="model-dataset">Dataset: Best Artworks of All Time</div>
  <div class="model-desc">
    CNN แบบ Transfer Learning จาก EfficientNetB0 (ImageNet) —
    fine-tune 2 phase เพื่อจำแนกสไตล์ภาพวาดจาก
    10 ศิลปินระดับโลก เช่น Van Gogh, Picasso, Rembrandt<br><br>
    Data augmentation: flip, rotation, zoom, brightness, contrast
  </div>
  <div class="model-pills">
    <span class="pill">EfficientNetB0</span>
    <span class="pill">Transfer Learning</span>
    <span class="pill">Fine-Tuning 2 Phase</span>
    <span class="pill">10 Artists</span>
    <span class="pill">Augmentation</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── NAVIGATION ────────────────────────────────────────────────────────────────
st.markdown('<p class="sec-label">เมนู</p><h2 class="sec-title">หน้าต่างๆ</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="nav-grid">
  <div class="nav-card">
    <div class="nav-icon">📖</div>
    <div>
      <div class="nav-name">ML Model Info</div>
      <div class="nav-desc">อธิบาย Ensemble ML — dataset, preprocessing, algorithm theory</div>
    </div>
  </div>
  <div class="nav-card">
    <div class="nav-icon">📘</div>
    <div>
      <div class="nav-name">NN Model Info</div>
      <div class="nav-desc">อธิบาย Neural Network — CNN, Transfer Learning, Fine-Tuning</div>
    </div>
  </div>
  <div class="nav-card">
    <div class="nav-icon">🌸</div>
    <div>
      <div class="nav-name">Test ML Model</div>
      <div class="nav-desc">อัปโหลดภาพดอกไม้ — โมเดลจะจำแนก daisy, rose, tulip ฯลฯ</div>
    </div>
  </div>
  <div class="nav-card">
    <div class="nav-icon">🎨</div>
    <div>
      <div class="nav-name">Test NN Model</div>
      <div class="nav-desc">อัปโหลดภาพวาด — โมเดลจะบอกว่าเป็นสไตล์ศิลปินคนใด</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding:3rem 0 1.5rem 0;
            color:#2d2217; font-family:'DM Mono',monospace;
            font-size:0.65rem; letter-spacing:0.14em;">
  IMAGE CLASSIFICATION PROJECT · ENSEMBLE ML + NEURAL NETWORK
</div>
""", unsafe_allow_html=True)