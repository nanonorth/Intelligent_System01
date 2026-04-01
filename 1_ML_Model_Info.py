import streamlit as st

st.set_page_config(
    page_title="Ensemble ML | Flower Classification",
    page_icon="🌸",
    layout="wide"
)

# ─── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Mono:wght@300;400&display=swap');

html, body, [class*="css"] {
    font-family: 'Cormorant Garamond', Georgia, serif;
}
.stApp {
    background-color: #0b0907;
    color: #e8dfd0;
}
h1, h2, h3, h4 {
    font-family: 'Cormorant Garamond', serif !important;
    letter-spacing: 0.04em;
}
code, .stCode, pre {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.82rem;
}

/* Hero banner */
.hero-wrap {
    background: linear-gradient(135deg, #0e160a 0%, #1a2a0e 50%, #0b0907 100%);
    border: 1px solid #1e2d17;
    border-radius: 4px;
    padding: 3.5rem 3rem;
    margin-bottom: 2.5rem;
    position: relative;
    overflow: hidden;
}
.hero-wrap::before {
    content: "";
    position: absolute;
    top: -40px; right: -40px;
    width: 280px; height: 280px;
    background: radial-gradient(circle, rgba(100,180,60,0.15) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-title {
    font-size: 3.2rem;
    font-weight: 300;
    color: #9ed860;
    line-height: 1.15;
    margin: 0 0 0.5rem 0;
    letter-spacing: 0.06em;
}
.hero-sub {
    font-size: 1.15rem;
    color: #6a7a50;
    font-style: italic;
    margin: 0;
}
.badge {
    display: inline-block;
    background: rgba(120,180,60,0.18);
    border: 1px solid rgba(120,180,60,0.4);
    color: #7ac870;
    padding: 0.2rem 0.75rem;
    border-radius: 2px;
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    margin-top: 1rem;
    letter-spacing: 0.08em;
}

/* Section headers */
.section-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    color: #7ac870;
    text-transform: uppercase;
    margin-bottom: 0.3rem;
}
.section-title {
    font-size: 1.9rem;
    font-weight: 300;
    color: #e8dfd0;
    margin: 0 0 1.5rem 0;
    border-bottom: 1px solid #1e2d17;
    padding-bottom: 0.75rem;
}

/* Cards */
.card {
    background: #0e140a;
    border: 1px solid #1e2d17;
    border-radius: 4px;
    padding: 1.5rem;
    height: 100%;
    transition: border-color 0.2s;
}
.card:hover { border-color: #3a5a1e; }
.card-icon { font-size: 1.8rem; margin-bottom: 0.6rem; }
.card-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #9ed860;
    margin-bottom: 0.6rem;
}
.card-body {
    font-size: 0.95rem;
    color: #6a7a52;
    line-height: 1.7;
}

/* Flower grid */
.flower-card {
    background: linear-gradient(145deg, #0e140a, #141e0e);
    border: 1px solid #1e2d17;
    border-radius: 4px;
    padding: 1.2rem 1rem;
    text-align: center;
    transition: all 0.25s;
    cursor: default;
}
.flower-card:hover {
    border-color: #7ac870;
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.5);
}
.flower-emoji { font-size: 2rem; margin-bottom: 0.5rem; }
.flower-name {
    font-size: 0.88rem;
    font-weight: 600;
    color: #e8dfd0;
    margin-bottom: 0.25rem;
    letter-spacing: 0.03em;
}
.flower-th {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    color: #4a6a3a;
    letter-spacing: 0.06em;
}

/* Architecture pipeline */
.arch-row {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
    flex-wrap: wrap;
}
.arch-block {
    background: #141e0e;
    border: 1px solid #1e2d17;
    border-radius: 3px;
    padding: 0.45rem 0.85rem;
    font-family: 'DM Mono', monospace;
    font-size: 0.78rem;
    color: #7ac870;
    white-space: nowrap;
}
.arch-block.input { border-color: #3a5a3a; color: #7ab87a; background: #0e160a; }
.arch-block.feat  { border-color: #2a4a2a; color: #9ed860; background: #101a08; }
.arch-block.proc  { border-color: #2a3a4a; color: #70a8c8; background: #0a1218; }
.arch-block.stack { border-color: #3a4a1a; color: #c8d870; background: #141c08; }
.arch-block.out   { border-color: #3a5a1a; color: #b8e870; background: #141e08; }
.arch-arrow { color: #2d3a20; font-size: 1.1rem; }

/* Step timeline */
.step {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.2rem;
    align-items: flex-start;
}
.step-num {
    background: linear-gradient(135deg, #1e2d17, #2d3a1a);
    color: #9ed860;
    border-radius: 50%;
    width: 28px; height: 28px; min-width: 28px;
    display: flex; align-items: center; justify-content: center;
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
}
.step-content { flex: 1; }
.step-title {
    font-weight: 600;
    color: #e8dfd0;
    margin-bottom: 0.2rem;
    font-size: 1rem;
}
.step-desc { color: #4a6a3a; font-size: 0.9rem; line-height: 1.6; }

/* Metric tiles */
.metric-tile {
    background: #0e140a;
    border: 1px solid #1e2d17;
    border-radius: 4px;
    padding: 1.2rem;
    text-align: center;
}
.metric-num {
    font-size: 2rem;
    font-weight: 300;
    color: #9ed860;
    font-family: 'DM Mono', monospace;
    display: block;
}
.metric-label {
    font-size: 0.8rem;
    color: #4a6a3a;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

/* Code block override */
.stCode { background: #080e04 !important; }

/* Divider */
.gold-rule {
    border: none;
    border-top: 1px solid #1e2d17;
    margin: 2.5rem 0;
}

/* Info box */
.info-box {
    background: #080e04;
    border-left: 3px solid #7ac870;
    padding: 1rem 1.2rem;
    border-radius: 0 4px 4px 0;
    font-size: 0.92rem;
    color: #6a7a52;
    line-height: 1.7;
    margin-top: 1rem;
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

# ─── FLOWERS DATA ──────────────────────────────────────────────────────────────
FLOWERS = [
    {"key": "daisy",     "emoji": "🌼", "name": "Daisy",     "th": "เดซี่",       "color": "#f0d060"},
    {"key": "dandelion", "emoji": "🌻", "name": "Dandelion", "th": "แดนดิไลออน",  "color": "#e8c040"},
    {"key": "rose",      "emoji": "🌹", "name": "Rose",      "th": "กุหลาบ",      "color": "#e87878"},
    {"key": "sunflower", "emoji": "🌞", "name": "Sunflower", "th": "ทานตะวัน",    "color": "#f0a030"},
    {"key": "tulip",     "emoji": "🌷", "name": "Tulip",     "th": "ทิวลิป",      "color": "#d870c0"},
]

# ─── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
  <p class="hero-title">Ensemble ML<br><em>Flower Classifier</em></p>
  <p class="hero-sub">Stacking Classifier · 5 Flower Species · HOG · Color Histogram · LBP · Gabor</p>
  <span class="badge">Dataset: Flowers Recognition — Kaggle</span>
</div>
""", unsafe_allow_html=True)

# ─── SECTION 1: DATASET ───────────────────────────────────────────────────────
st.markdown('<p class="section-label">01</p><h2 class="section-title">Dataset</h2>', unsafe_allow_html=True)

col_l, col_r = st.columns([3, 2], gap="large")
with col_l:
    st.markdown("""
<div class="card">
  <div class="card-title">📂 Flowers Recognition</div>
  <div class="card-body">
    แหล่งที่มา: <a href="https://www.kaggle.com/datasets/alxmamaev/flowers-recognition" style="color:#7ac870;">Kaggle — alxmamaev</a><br><br>
    ประกอบด้วยภาพดอกไม้ <strong style="color:#e8dfd0;">5 ประเภท</strong> ได้แก่ daisy, dandelion, rose, sunflower และ tulip
    รวมกว่า 4,000 รูป ถ่ายในสภาพแสงและมุมที่หลากหลาย<br><br>
    ลักษณะของข้อมูล:
    <ul style="color:#4a6a3a; margin-top:0.5rem; line-height:2;">
      <li>รูปแบบ <code>.jpg</code> ความละเอียดหลากหลาย</li>
      <li>จำนวนรูปต่อคลาส <strong style="color:#e8dfd0;">ไม่เท่ากัน</strong> (imbalanced)</li>
      <li>ฉากหลังหลากหลาย ทั้งในร่มและกลางแจ้ง</li>
      <li>บางรูปมี noise และแสงไม่สม่ำเสมอ</li>
    </ul>
  </div>
</div>
""", unsafe_allow_html=True)

with col_r:
    st.markdown("""
<div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; height:100%;">
  <div class="metric-tile"><span class="metric-num">5</span><span class="metric-label">Classes</span></div>
  <div class="metric-tile"><span class="metric-num">~4k</span><span class="metric-label">Images</span></div>
  <div class="metric-tile"><span class="metric-num">128²</span><span class="metric-label">Input Size</span></div>
  <div class="metric-tile"><span class="metric-num">80/20</span><span class="metric-label">Train/Test</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="gold-rule">', unsafe_allow_html=True)

# ─── SECTION 2: FLOWER CLASSES ────────────────────────────────────────────────
st.markdown('<p class="section-label">02</p><h2 class="section-title">ดอกไม้ 5 ประเภทที่จำแนก</h2>', unsafe_allow_html=True)

cols = st.columns(5)
for i, f in enumerate(FLOWERS):
    with cols[i]:
        st.markdown(f"""
<div class="flower-card" style="border-top: 3px solid {f['color']}88;">
  <div class="flower-emoji">{f['emoji']}</div>
  <div class="flower-name">{f['name']}</div>
  <div class="flower-th">{f['th']}</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="gold-rule">', unsafe_allow_html=True)

# ─── SECTION 3: PREPROCESSING ─────────────────────────────────────────────────
st.markdown('<p class="section-label">03</p><h2 class="section-title">การเตรียมข้อมูล</h2>', unsafe_allow_html=True)

c1, c2 = st.columns(2, gap="large")
with c1:
    steps_left = [
        ("ลบรูป Corrupt", "ตรวจสอบทุกไฟล์ด้วย PIL — รูปที่เปิดไม่ได้หรือ grayscale จะถูกข้ามทันที"),
        ("Resize & Convert", "ปรับทุกรูปเป็น <code>128×128</code> pixels และแปลงเป็น RGB เพื่อให้ทุกรูปมีขนาดและ channel เดียวกัน"),
        ("Label Encoding", "แปลง label ชื่อดอกไม้เป็นตัวเลขด้วย <code>LabelEncoder</code> จาก scikit-learn"),
        ("Train/Test Split", "แบ่งข้อมูล 80% / 20% โดยใช้ stratified split เพื่อรักษาสัดส่วนแต่ละคลาส"),
    ]
    for n, (title, desc) in enumerate(steps_left, 1):
        st.markdown(f"""
<div class="step">
  <div class="step-num">{n:02d}</div>
  <div class="step-content">
    <div class="step-title">{title}</div>
    <div class="step-desc">{desc}</div>
  </div>
</div>""", unsafe_allow_html=True)

with c2:
    steps_right = [
        ("Feature Extraction", "สกัด HOG, Color Histogram (32 bins × 3 channels), LBP และ Gabor filter features จากแต่ละรูป"),
        ("Feature Concatenation", "รวม features ทุกประเภทเป็น vector เดียว ขนาด ~1,900+ มิติต่อรูป"),
        ("Standard Scaling", "Normalize feature vector ด้วย <code>StandardScaler</code> ให้มีค่าเฉลี่ย 0 และ SD 1"),
        ("PCA Reduction", "ลด dimension ด้วย PCA เหลือ <code>n_components=0.95</code> เพื่อตัด noise และเร่งความเร็ว"),
    ]
    for n, (title, desc) in enumerate(steps_right, 5):
        st.markdown(f"""
<div class="step">
  <div class="step-num">{n:02d}</div>
  <div class="step-content">
    <div class="step-title">{title}</div>
    <div class="step-desc">{desc}</div>
  </div>
</div>""", unsafe_allow_html=True)

st.markdown('<hr class="gold-rule">', unsafe_allow_html=True)

# ─── SECTION 4: ALGORITHM THEORY ──────────────────────────────────────────────
st.markdown('<p class="section-label">04</p><h2 class="section-title">ทฤษฎีของอัลกอริทึม (Ensemble ML)</h2>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🔬 Feature Engineering", "🌲 Base Classifiers", "🏆 Stacking Ensemble"])

with tab1:
    col_a, col_b = st.columns([3, 2], gap="large")
    with col_a:
        st.markdown("""
<div class="card">
  <div class="card-title">การสกัด Feature จากภาพ</div>
  <div class="card-body">
    แทนที่จะให้โมเดลเรียนรู้ pixel โดยตรง เราสกัด <strong style="color:#e8dfd0;">Feature เชิงความหมาย</strong> ออกมาก่อน:<br><br>
    <strong style="color:#e8dfd0;">① HOG — Histogram of Oriented Gradients</strong><br>
    วัดทิศทางและความแรงของขอบ (gradient) ในภาพ เหมาะจับรูปทรงและโครงสร้างของดอกไม้ เช่น กลีบ ก้าน<br><br>
    <strong style="color:#e8dfd0;">② Color Histogram</strong><br>
    นับการกระจายตัวของสีในแต่ละ channel (R, G, B) แบ่งเป็น 32 bins ดอกไม้แต่ละชนิดมีโทนสีเฉพาะตัวมาก<br><br>
    <strong style="color:#e8dfd0;">③ LBP — Local Binary Pattern</strong><br>
    เปรียบเทียบ pixel กับเพื่อนบ้านรอบๆ เพื่อจับ texture เช่น ความหยาบของกลีบ ลายพื้นผิว<br><br>
    <strong style="color:#e8dfd0;">④ Gabor Filter</strong><br>
    กรองภาพด้วยความถี่และทิศทางต่างๆ เพื่อจับ texture ในมาตราส่วนที่หลากหลาย
  </div>
</div>
""", unsafe_allow_html=True)
    with col_b:
        st.markdown("""
<div class="card">
  <div class="card-title">Feature Vector Summary</div>
  <div class="card-body">
    <strong style="color:#7ac870;">HOG</strong><br>
    orientations=9, pixels_per_cell=(8,8)<br>
    cells_per_block=(2,2)<br>
    <span style="color:#4a6a3a; font-size:0.85rem;">→ ~1,764 dims</span><br><br>
    <strong style="color:#7ac870;">Color Histogram</strong><br>
    32 bins × 3 channels (R, G, B)<br>
    normalized per channel<br>
    <span style="color:#4a6a3a; font-size:0.85rem;">→ 96 dims</span><br><br>
    <strong style="color:#7ac870;">LBP</strong><br>
    P=8, R=1, method='uniform'<br>
    10-bin histogram<br>
    <span style="color:#4a6a3a; font-size:0.85rem;">→ 10 dims</span><br><br>
    <strong style="color:#7ac870;">Gabor</strong><br>
    4 frequencies × 4 orientations<br>
    mean + std per filter<br>
    <span style="color:#4a6a3a; font-size:0.85rem;">→ 32 dims</span>
  </div>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br><strong style='color:#6a7a52;font-size:0.9rem;'>Feature Pipeline:</strong>", unsafe_allow_html=True)
    st.markdown("""
<div class="arch-row">
  <div class="arch-block input">Image<br>128×128×3</div>
  <div class="arch-arrow">→</div>
  <div class="arch-block feat">HOG<br>1,764d</div>
  <div class="arch-arrow">+</div>
  <div class="arch-block feat">Color Hist<br>96d</div>
  <div class="arch-arrow">+</div>
  <div class="arch-block feat">LBP<br>10d</div>
  <div class="arch-arrow">+</div>
  <div class="arch-block feat">Gabor<br>32d</div>
  <div class="arch-arrow">→</div>
  <div class="arch-block proc">StandardScaler<br>+ PCA 95%</div>
  <div class="arch-arrow">→</div>
  <div class="arch-block out">Feature Vector<br>(reduced)</div>
</div>
""", unsafe_allow_html=True)

with tab2:
    col_a, col_b = st.columns(2, gap="large")
    with col_a:
        st.markdown("""
<div class="card">
  <div class="card-title">Base Classifiers ที่ใช้</div>
  <div class="card-body">
    Stacking Ensemble ประกอบด้วย <strong style="color:#e8dfd0;">5 Base Learners</strong> ที่แตกต่างกัน:<br><br>
    <strong style="color:#7ac870;">🌲 Random Forest (RF)</strong><br>
    ต้นไม้การตัดสินใจหลายต้น โหวตร่วมกัน ทนต่อ noise และ outlier<br><br>
    <strong style="color:#7ac870;">🌳 Extra Trees (ET)</strong><br>
    คล้าย RF แต่แยก node แบบสุ่มมากกว่า ลด variance ได้ดี<br><br>
    <strong style="color:#7ac870;">⚙️ SVM (Support Vector Machine)</strong><br>
    หาขอบเขตที่ดีที่สุดระหว่างคลาส ใช้ kernel RBF สำหรับข้อมูลไม่เชิงเส้น<br><br>
    <strong style="color:#7ac870;">⚡ XGBoost</strong><br>
    Gradient Boosting แบบ optimized สร้างต้นไม้ทีละต้น แก้ error ของต้นก่อน<br><br>
    <strong style="color:#7ac870;">💡 LightGBM</strong><br>
    Gradient Boosting แบบเร็วกว่า XGBoost ใช้ leaf-wise tree growth
  </div>
</div>
""", unsafe_allow_html=True)
    with col_b:
        st.markdown("""
<div class="card">
  <div class="card-title">ทำไมต้องใช้ Base Classifiers หลายตัว?</div>
  <div class="card-body">
    แต่ละอัลกอริทึมมี <strong style="color:#e8dfd0;">จุดแข็งต่างกัน</strong>:<br><br>
    RF / ET เก่งเรื่อง generalization และรับมือ noise ได้ดี<br>
    SVM เก่งเรื่องขอบเขตชัดเจนในพื้นที่ high-dimension<br>
    XGB / LGBM เก่งเรื่องการจับ pattern ซับซ้อน<br><br>
    การรวมกันทำให้ Meta-Learner เห็น <strong style="color:#e8dfd0;">มุมมองที่หลากหลาย</strong>
    ของข้อมูล และสามารถเลือกเชื่อโมเดลที่เหมาะสมกับแต่ละตัวอย่างได้<br><br>
    <div class="info-box">
      หลักการ: โมเดลที่ผิดพลาดต่างกัน เมื่อรวมกันจะลดข้อผิดพลาดโดยรวมลงได้
      — <em>Bias-Variance Tradeoff</em>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

with tab3:
    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown("""
<div class="card" style="border-color:#2a4a2a;">
  <div class="card-icon">🔀</div>
  <div class="card-title" style="color:#7ac870;">Level 0 — Base Learners</div>
  <div class="card-body">
    <strong>Train</strong> Base Classifiers ทั้ง 5 ตัวบนข้อมูล training<br>
    แต่ละตัวทำนาย probability สำหรับทุก class<br><br>
    ใช้ <code>cross_val_predict</code> (cv=5) เพื่อสร้าง
    <strong style="color:#e8dfd0;">Out-of-Fold predictions</strong>
    ป้องกัน data leakage ไปยัง Meta-Learner<br><br>
    <ul style="color:#4a6a3a; line-height:2;">
      <li>RF: <code>n_estimators=300</code></li>
      <li>ET: <code>n_estimators=300</code></li>
      <li>SVM: <code>kernel='rbf', C=10, probability=True</code></li>
      <li>XGB: <code>n_estimators=200, lr=0.05</code></li>
      <li>LGBM: <code>n_estimators=200, lr=0.05</code></li>
    </ul>
  </div>
</div>
""", unsafe_allow_html=True)
    with c2:
        st.markdown("""
<div class="card" style="border-color:#3a5a1a;">
  <div class="card-icon">🏆</div>
  <div class="card-title" style="color:#b8e870;">Level 1 — Meta-Learner</div>
  <div class="card-body">
    <strong>Logistic Regression</strong> ทำหน้าที่เป็น Meta-Learner<br>
    รับ output (probabilities) ของ Base Learners ทั้ง 5 เป็น input<br><br>
    <code>LogisticRegression(C=1.0, max_iter=1000)</code><br><br>
    <ul style="color:#4a6a3a; line-height:2;">
      <li>เรียนรู้ว่าควรเชื่อโมเดลไหน ในสถานการณ์แบบใด</li>
      <li>Regularization ป้องกัน overfitting</li>
      <li>ตีความได้ง่าย — เหมาะเป็น meta layer</li>
    </ul>
    <div class="info-box">
      Input ของ Meta-Learner = <code>5 models × 5 classes = 25 features</code>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br><strong style='color:#6a7a52;font-size:0.9rem;'>Stacking Architecture:</strong>", unsafe_allow_html=True)
    st.markdown("""
<div class="arch-row">
  <div class="arch-block input">Feature<br>Vector</div>
  <div class="arch-arrow">→</div>
  <div class="arch-block feat">RF<br>prob×5</div>
  <div class="arch-arrow">+</div>
  <div class="arch-block feat">ET<br>prob×5</div>
  <div class="arch-arrow">+</div>
  <div class="arch-block feat">SVM<br>prob×5</div>
  <div class="arch-arrow">+</div>
  <div class="arch-block feat">XGB<br>prob×5</div>
  <div class="arch-arrow">+</div>
  <div class="arch-block feat">LGBM<br>prob×5</div>
  <div class="arch-arrow">→</div>
  <div class="arch-block stack">Logistic<br>Regression</div>
  <div class="arch-arrow">→</div>
  <div class="arch-block out">5 classes<br>prediction</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="gold-rule">', unsafe_allow_html=True)

# ─── SECTION 5: MODEL CODE ────────────────────────────────────────────────────
st.markdown('<p class="section-label">05</p><h2 class="section-title">โค้ดโมเดล</h2>', unsafe_allow_html=True)

col_code, col_cfg = st.columns([3, 2], gap="large")
with col_code:
    st.code("""
import numpy as np
from sklearn.ensemble import (RandomForestClassifier,
                               ExtraTreesClassifier,
                               StackingClassifier)
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
import xgboost as xgb
import lightgbm as lgb
import joblib

CLASSES     = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
IMG_SIZE    = (128, 128)

# ── Base estimators ───────────────────────────────
base_estimators = [
    ('rf',   RandomForestClassifier(n_estimators=300,
                                    random_state=42, n_jobs=-1)),
    ('et',   ExtraTreesClassifier(n_estimators=300,
                                   random_state=42, n_jobs=-1)),
    ('svm',  SVC(kernel='rbf', probability=True,
                 C=10, gamma='scale', random_state=42)),
    ('xgb',  xgb.XGBClassifier(n_estimators=200, learning_rate=0.05,
                                max_depth=6, eval_metric='mlogloss',
                                random_state=42)),
    ('lgbm', lgb.LGBMClassifier(n_estimators=200, learning_rate=0.05,
                                  num_leaves=31, random_state=42,
                                  n_jobs=-1)),
]

# ── Meta-learner (Level 1) ────────────────────────
meta = LogisticRegression(C=1.0, max_iter=1000, random_state=42)

# ── Stacking Classifier ───────────────────────────
model = StackingClassifier(
    estimators=base_estimators,
    final_estimator=meta,
    cv=5,
    stack_method='predict_proba',
    n_jobs=-1
)

# ── Preprocessing pipeline ────────────────────────
scaler = StandardScaler()
pca    = PCA(n_components=0.95, random_state=42)

X_sc  = scaler.fit_transform(X_train)
X_pca = pca.fit_transform(X_sc)

# ── Train & Save ──────────────────────────────────
model.fit(X_pca, y_train)

joblib.dump({
    'model':         model,
    'scaler':        scaler,
    'pca':           pca,
    'label_encoder': le,
}, 'ensemble_model.pkl')
""", language="python")

with col_cfg:
    st.markdown("""
<div class="card">
  <div class="card-title">⚙️ Model Config</div>
  <div class="card-body">
    <table style="width:100%; font-size:0.88rem; border-collapse:collapse;">
      <tr><td style="color:#4a6a3a; padding:0.3rem 0;">RF / ET Trees</td><td style="color:#e8dfd0; text-align:right;"><code>300</code></td></tr>
      <tr><td style="color:#4a6a3a; padding:0.3rem 0;">SVM Kernel</td><td style="color:#e8dfd0; text-align:right;"><code>RBF, C=10</code></td></tr>
      <tr><td style="color:#4a6a3a; padding:0.3rem 0;">XGB / LGBM LR</td><td style="color:#e8dfd0; text-align:right;"><code>0.05</code></td></tr>
      <tr><td style="color:#4a6a3a; padding:0.3rem 0;">Stacking CV</td><td style="color:#e8dfd0; text-align:right;"><code>5-fold</code></td></tr>
      <tr><td style="color:#4a6a3a; padding:0.3rem 0;">Meta-Learner</td><td style="color:#e8dfd0; text-align:right;"><code>LogisticRegression</code></td></tr>
      <tr><td style="color:#4a6a3a; padding:0.3rem 0;">PCA Variance</td><td style="color:#e8dfd0; text-align:right;"><code>95%</code></td></tr>
      <tr><td style="color:#4a6a3a; padding:0.3rem 0;">Train / Test</td><td style="color:#e8dfd0; text-align:right;"><code>80 / 20</code></td></tr>
    </table>
  </div>
</div>
<br>
<div class="card">
  <div class="card-title">🔍 Features Used</div>
  <div class="card-body">
    <code>HOG</code> — shape &amp; edge gradients<br>
    <code>Color Histogram</code> — color distribution<br>
    <code>LBP</code> — local texture patterns<br>
    <code>Gabor</code> — multi-scale texture<br><br>
    รวม → <code>StandardScaler</code><br>
    ลด dim → <code>PCA (95% variance)</code>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="gold-rule">', unsafe_allow_html=True)

# ─── SECTION 6: DEVELOPMENT STEPS ────────────────────────────────────────────
st.markdown('<p class="section-label">06</p><h2 class="section-title">ขั้นตอนการพัฒนา</h2>', unsafe_allow_html=True)

all_steps = [
    ("Load & Filter Dataset", "โหลดภาพจากโฟลเดอร์ทั้ง 5 ประเภท ลบรูป corrupt และแปลงทุกรูปเป็น RGB กรองเฉพาะ <code>.jpg/.jpeg/.png</code>"),
    ("Explore & Visualize", "ตรวจสอบ class distribution, แสดงตัวอย่างภาพแต่ละประเภท และหาค่า min/max/mean ของจำนวนภาพต่อคลาส"),
    ("Extract Features", "สกัด HOG, Color Histogram, LBP และ Gabor features จากทุกรูป แล้ว concatenate เป็น feature vector เดียว"),
    ("Preprocess Features", "Scale ด้วย StandardScaler และลด dimension ด้วย PCA เก็บ variance ไว้ 95%"),
    ("Train & Compare Base Models", "Train RF, ET, SVM, XGBoost และ LightGBM แยกกัน ทดสอบ accuracy และ confusion matrix แต่ละตัว"),
    ("Build Stacking Ensemble", "รวม Base Classifiers ด้วย StackingClassifier ใช้ 5-fold CV สร้าง out-of-fold predictions ป้องกัน data leakage"),
    ("Evaluate & Analyze", "วัด Test Accuracy, สร้าง Confusion Matrix และ Classification Report เปรียบเทียบ Stacking กับ Single Model"),
    ("Save & Deploy", "บันทึกโมเดลพร้อม scaler, PCA และ label encoder ลงไฟล์ <code>ensemble_model.pkl</code> ด้วย joblib"),
]

cols_steps = st.columns(2, gap="large")
for i, (title, desc) in enumerate(all_steps):
    with cols_steps[i % 2]:
        st.markdown(f"""
<div class="step">
  <div class="step-num">{i+1:02d}</div>
  <div class="step-content">
    <div class="step-title">{title}</div>
    <div class="step-desc">{desc}</div>
  </div>
</div>""", unsafe_allow_html=True)

st.markdown('<hr class="gold-rule">', unsafe_allow_html=True)

# ─── SECTION 7: REFERENCES ───────────────────────────────────────────────────
st.markdown('<p class="section-label">07</p><h2 class="section-title">แหล่งอ้างอิง</h2>', unsafe_allow_html=True)

refs = [
    ("📦 Dataset", "Flowers Recognition — Kaggle", "https://www.kaggle.com/datasets/alxmamaev/flowers-recognition"),
    ("📖 Paper", "HOG Features — Dalal & Triggs, CVPR 2005", "https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf"),
    ("📖 Paper", "Stacking Generalization — Wolpert, 1992", "https://www.sciencedirect.com/science/article/pii/S0893608005800231"),
    ("📚 Docs", "scikit-learn: StackingClassifier", "https://scikit-learn.org/stable/modules/ensemble.html#stacking"),
    ("📚 Docs", "XGBoost Documentation", "https://xgboost.readthedocs.io/"),
    ("📚 Docs", "LightGBM Documentation", "https://lightgbm.readthedocs.io/"),
]

ref_cols = st.columns(3)
for i, (tag, title, url) in enumerate(refs):
    with ref_cols[i % 3]:
        st.markdown(f"""
<div class="card" style="margin-bottom:0.75rem;">
  <div style="font-family:'DM Mono',monospace; font-size:0.7rem; color:#4a6a3a; margin-bottom:0.3rem;">{tag}</div>
  <a href="{url}" target="_blank" style="color:#7ac870; font-size:0.9rem; text-decoration:none;">{title}</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding:3rem 0 1rem 0; color:#1e2d17;
            font-family:'DM Mono',monospace; font-size:0.72rem; letter-spacing:0.1em;">
  ENSEMBLE ML · FLOWER CLASSIFICATION · 5 SPECIES
</div>
""", unsafe_allow_html=True)