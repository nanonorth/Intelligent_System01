import streamlit as st

st.set_page_config(
    page_title="Neural Network | Painting Style Classification",
    page_icon="🎨",
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
    background-color: #0e0c0a;
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
    background: linear-gradient(135deg, #1a1209 0%, #2e1f0c 50%, #0e0c0a 100%);
    border: 1px solid #3d2e1a;
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
    background: radial-gradient(circle, rgba(180,130,60,0.15) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-title {
    font-size: 3.2rem;
    font-weight: 300;
    color: #e8c87a;
    line-height: 1.15;
    margin: 0 0 0.5rem 0;
    letter-spacing: 0.06em;
}
.hero-sub {
    font-size: 1.15rem;
    color: #9e8c72;
    font-style: italic;
    margin: 0;
}
.badge {
    display: inline-block;
    background: rgba(180,130,60,0.18);
    border: 1px solid rgba(180,130,60,0.4);
    color: #c9a84c;
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
    color: #c9a84c;
    text-transform: uppercase;
    margin-bottom: 0.3rem;
}
.section-title {
    font-size: 1.9rem;
    font-weight: 300;
    color: #e8dfd0;
    margin: 0 0 1.5rem 0;
    border-bottom: 1px solid #2d2318;
    padding-bottom: 0.75rem;
}

/* Cards */
.card {
    background: #16120d;
    border: 1px solid #2d2318;
    border-radius: 4px;
    padding: 1.5rem;
    height: 100%;
    transition: border-color 0.2s;
}
.card:hover { border-color: #5a3e1e; }
.card-icon { font-size: 1.8rem; margin-bottom: 0.6rem; }
.card-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #e8c87a;
    margin-bottom: 0.6rem;
}
.card-body {
    font-size: 0.95rem;
    color: #9e8c72;
    line-height: 1.7;
}

/* Artist grid */
.artist-card {
    background: linear-gradient(145deg, #16120d, #1e160e);
    border: 1px solid #2d2318;
    border-radius: 4px;
    padding: 1.2rem 1rem;
    text-align: center;
    transition: all 0.25s;
    cursor: default;
}
.artist-card:hover {
    border-color: #c9a84c;
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.5);
}
.artist-avatar {
    width: 52px; height: 52px;
    border-radius: 50%;
    background: linear-gradient(135deg, #3d2e1a, #5a3e1e);
    display: flex; align-items: center; justify-content: center;
    font-size: 1.4rem;
    margin: 0 auto 0.7rem auto;
    border: 1px solid #3d2e1a;
}
.artist-name {
    font-size: 0.88rem;
    font-weight: 600;
    color: #e8dfd0;
    margin-bottom: 0.25rem;
    letter-spacing: 0.03em;
}
.artist-era {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    color: #6b5a3e;
    letter-spacing: 0.06em;
}

/* Architecture diagram */
.arch-row {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
    flex-wrap: wrap;
}
.arch-block {
    background: #1e160e;
    border: 1px solid #3d2e1a;
    border-radius: 3px;
    padding: 0.45rem 0.85rem;
    font-family: 'DM Mono', monospace;
    font-size: 0.78rem;
    color: #c9a84c;
    white-space: nowrap;
}
.arch-block.input  { border-color: #3a5a3a; color: #7ab87a; background: #101a10; }
.arch-block.conv   { border-color: #3d4a5a; color: #7aaac8; background: #101520; }
.arch-block.pool   { border-color: #3a2a4a; color: #a07ad0; background: #150f1e; }
.arch-block.dense  { border-color: #5a3a1a; color: #d0924c; background: #1e1208; }
.arch-block.out    { border-color: #5a3a3a; color: #d07a7a; background: #1e1010; }
.arch-arrow { color: #3d2e1a; font-size: 1.1rem; }

/* Step timeline */
.step {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.2rem;
    align-items: flex-start;
}
.step-num {
    background: linear-gradient(135deg, #3d2e1a, #5a3e1e);
    color: #e8c87a;
    border-radius: 50%;
    width: 28px; height: 28px; min-width: 28px;
    display: flex; align-items: center; justify-content: center;
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    font-weight: 400;
}
.step-content { flex: 1; }
.step-title {
    font-weight: 600;
    color: #e8dfd0;
    margin-bottom: 0.2rem;
    font-size: 1rem;
}
.step-desc { color: #7a6a52; font-size: 0.9rem; line-height: 1.6; }

/* Metric tiles */
.metric-tile {
    background: #16120d;
    border: 1px solid #2d2318;
    border-radius: 4px;
    padding: 1.2rem;
    text-align: center;
}
.metric-num {
    font-size: 2rem;
    font-weight: 300;
    color: #e8c87a;
    font-family: 'DM Mono', monospace;
    display: block;
}
.metric-label {
    font-size: 0.8rem;
    color: #6b5a3e;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

/* Code block override */
.stCode { background: #0a0806 !important; }

/* Divider */
.gold-rule {
    border: none;
    border-top: 1px solid #2d2318;
    margin: 2.5rem 0;
}

/* Callback box */
.info-box {
    background: #12100c;
    border-left: 3px solid #c9a84c;
    padding: 1rem 1.2rem;
    border-radius: 0 4px 4px 0;
    font-size: 0.92rem;
    color: #9e8c72;
    line-height: 1.7;
    margin-top: 1rem;
}

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

# ─── ARTISTS DATA ──────────────────────────────────────────────────────────────
ARTISTS = [
    {"name": "Vincent van Gogh",        "era": "Post-Impressionism · 1853–1890"},
    {"name": "Edgar Degas",             "era": "Impressionism · 1834–1917"},
    {"name": "Pablo Picasso",           "era": "Cubism · 1881–1973"},
    {"name": "Pierre-Auguste Renoir",   "era": "Impressionism · 1841–1919"},
    {"name": "Albrecht Dürer",          "era": "Northern Renaissance · 1471–1528"},
    {"name": "Paul Gauguin",            "era": "Post-Impressionism · 1848–1903"},
    {"name": "Francisco Goya",          "era": "Romanticism · 1746–1828"},
    {"name": "Rembrandt",               "era": "Dutch Golden Age · 1606–1669"},
    {"name": "Alfred Sisley",           "era": "Impressionism · 1839–1899"},
    {"name": "Titian",                  "era": "Venetian Renaissance · 1488–1576"},
]

# ─── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
  <p class="hero-title">Neural Network<br><em>Painting Style Classifier</em></p>
  <p class="hero-sub">Convolutional Neural Network · 10 Master Artists · Transfer Learning</p>
  <span class="badge">Dataset: Best Artworks of All Time — Kaggle</span>
</div>
""", unsafe_allow_html=True)

# ─── SECTION 1: DATASET ───────────────────────────────────────────────────────
st.markdown('<p class="section-label">01</p><h2 class="section-title">Dataset</h2>', unsafe_allow_html=True)

col_l, col_r = st.columns([3, 2], gap="large")
with col_l:
    st.markdown("""
<div class="card">
  <div class="card-title">📂 Best Artworks of All Time</div>
  <div class="card-body">
    แหล่งที่มา: <a href="https://www.kaggle.com/datasets/ikarus777/best-artworks-of-all-time" style="color:#c9a84c;">Kaggle — ikarus777</a><br><br>
    ประกอบด้วยภาพวาดจากศิลปินระดับโลก 50 คน คัดเลือกมา <strong style="color:#e8dfd0;">10 ศิลปิน</strong> ที่มีภาพมากที่สุด
    เพื่อให้โมเดลเรียนรู้ได้เพียงพอและ dataset สมดุลขึ้น<br><br>
    ลักษณะของข้อมูล:
    <ul style="color:#7a6a52; margin-top:0.5rem; line-height:2;">
      <li>รูปแบบ <code>.jpg</code> ความละเอียดหลากหลาย</li>
      <li>จำนวนรูปต่อคลาส <strong style="color:#e8dfd0;">ไม่เท่ากัน</strong> (imbalanced)</li>
      <li>บางรูป corrupt หรือ grayscale</li>
      <li>สไตล์ภายในคลาสเดียวกันมี variance สูง</li>
    </ul>
  </div>
</div>
""", unsafe_allow_html=True)

with col_r:
    st.markdown("""
<div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; height:100%;">
  <div class="metric-tile"><span class="metric-num">10</span><span class="metric-label">Artists</span></div>
  <div class="metric-tile"><span class="metric-num">~8k</span><span class="metric-label">Images</span></div>
  <div class="metric-tile"><span class="metric-num">128²</span><span class="metric-label">Input Size</span></div>
  <div class="metric-tile"><span class="metric-num">80/20</span><span class="metric-label">Train/Test</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="gold-rule">', unsafe_allow_html=True)

# ─── SECTION 2: ARTISTS ───────────────────────────────────────────────────────
st.markdown('<p class="section-label">02</p><h2 class="section-title">ศิลปิน 10 คนที่เลือก</h2>', unsafe_allow_html=True)

cols = st.columns(5)
for i, artist in enumerate(ARTISTS):
    with cols[i % 5]:
        st.markdown(f"""
<div class="artist-card">
  <div class="artist-name">{artist["name"]}</div>
  <div class="artist-era">{artist["era"]}</div>
</div>
""", unsafe_allow_html=True)
    if i == 4:
        st.markdown("<div style='margin-bottom:0.75rem'></div>", unsafe_allow_html=True)
        cols = st.columns(5)

st.markdown('<hr class="gold-rule">', unsafe_allow_html=True)

# ─── SECTION 3: PREPROCESSING ─────────────────────────────────────────────────
st.markdown('<p class="section-label">03</p><h2 class="section-title">การเตรียมข้อมูล</h2>', unsafe_allow_html=True)

c1, c2 = st.columns(2, gap="large")
with c1:
    steps_left = [
        ("ลบรูป Corrupt", "ตรวจสอบทุกไฟล์ด้วย PIL — รูปที่เปิดไม่ได้จะถูกข้ามทันที"),
        ("Resize & Normalize", "ปรับทุกรูปเป็น <code>128×128</code> pixels แล้ว normalize pixel values เป็น <code>[0, 1]</code>"),
        ("One-Hot Encoding", "แปลง label ชื่อศิลปินเป็น One-Hot vector ขนาด 10 มิติ"),
        ("Train/Val/Test Split", "แบ่งข้อมูล 70% / 15% / 15% โดยใช้ stratified split เพื่อรักษาสัดส่วนแต่ละคลาส"),
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
        ("Data Augmentation", "เพิ่มข้อมูลเทียมแบบ real-time ระหว่าง training: random flip, rotation ±15°, zoom, brightness, contrast"),
        ("Class Weight Balancing", "คำนวณ <code>class_weight</code> อัตโนมัติเพื่อ compensate คลาสที่มีรูปน้อยกว่า"),
        ("ImageDataGenerator", "ใช้ Keras <code>ImageDataGenerator</code> เพื่อ load รูปเป็น batch แทนการโหลดทั้งหมดเข้า RAM"),
        ("Feature Scaling", "Pixel ถูก scale ด้วย <code>preprocess_input()</code> ของ EfficientNet เพื่อให้ตรงกับ pretrained weight"),
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
st.markdown('<p class="section-label">04</p><h2 class="section-title">ทฤษฎีของอัลกอริทึม (Neural Network)</h2>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🔬 CNN Basics", "⚡ Transfer Learning / EfficientNet", "🎯 Fine-Tuning Strategy"])

with tab1:
    col_a, col_b = st.columns([3, 2], gap="large")
    with col_a:
        st.markdown("""
<div class="card">
  <div class="card-title">Convolutional Neural Network (CNN)</div>
  <div class="card-body">
    CNN เป็น Neural Network ที่ออกแบบมาเฉพาะสำหรับข้อมูลภาพ ประกอบด้วย 3 ส่วนหลัก:
    <br><br>
    <strong style="color:#e8dfd0;">① Convolutional Layer</strong><br>
    ใช้ filter/kernel เลื่อนผ่านภาพเพื่อตรวจจับ pattern เช่น ขอบ, เส้น, พื้นผิว
    แต่ละ filter จะสร้าง Feature Map ขึ้นมา
    <br><br>
    <strong style="color:#e8dfd0;">② Pooling Layer</strong><br>
    ลดขนาด Feature Map (Max Pooling หรือ Average Pooling)
    เพื่อลด computation และสร้าง translation invariance
    <br><br>
    <strong style="color:#e8dfd0;">③ Fully Connected Layer</strong><br>
    นำ feature ที่สกัดได้มาจัดหมวดหมู่ด้วย Dense layers
    layer สุดท้ายใช้ Softmax สำหรับ multi-class classification
  </div>
</div>
""", unsafe_allow_html=True)
    with col_b:
        st.markdown("""
<div class="card">
  <div class="card-title">Activation Functions</div>
  <div class="card-body">
    <strong style="color:#7aaac8;">ReLU</strong><br>
    <code>f(x) = max(0, x)</code><br>
    ใช้ใน Hidden layers — แก้ปัญหา Vanishing Gradient<br><br>
    <strong style="color:#7aaac8;">Softmax</strong><br>
    <code>σ(z)ᵢ = eᶻⁱ / Σeᶻʲ</code><br>
    ใช้ใน Output layer — แปลง logit เป็น probability ที่รวมกันได้ 1<br><br>
    <strong style="color:#7aaac8;">Dropout</strong><br>
    ปิด neuron แบบ random ระหว่าง training เพื่อป้องกัน Overfitting<br><br>
    <strong style="color:#7aaac8;">Batch Normalization</strong><br>
    Normalize output ของแต่ละ layer ให้เร็วขึ้นและ stable ขึ้น
  </div>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br><strong style='color:#9e8c72;font-size:0.9rem;'>Architecture Flow:</strong>", unsafe_allow_html=True)
    st.markdown("""
<div class="arch-row">
  <div class="arch-block input">Input<br>128×128×3</div>
  <div class="arch-arrow">→</div>
  <div class="arch-block conv">Conv2D 32<br>BatchNorm · ReLU</div>
  <div class="arch-arrow">→</div>
  <div class="arch-block pool">MaxPool<br>2×2</div>
  <div class="arch-arrow">→</div>
  <div class="arch-block conv">Conv2D 64<br>BatchNorm · ReLU</div>
  <div class="arch-arrow">→</div>
  <div class="arch-block pool">MaxPool<br>2×2</div>
  <div class="arch-arrow">→</div>
  <div class="arch-block conv">Conv2D 128<br>BatchNorm · ReLU</div>
  <div class="arch-arrow">→</div>
  <div class="arch-block pool">GlobalAvgPool</div>
  <div class="arch-arrow">→</div>
  <div class="arch-block dense">Dense 256<br>Dropout 0.5</div>
  <div class="arch-arrow">→</div>
  <div class="arch-block out">Softmax<br>10 classes</div>
</div>
""", unsafe_allow_html=True)

with tab2:
    col_a, col_b = st.columns([2, 3], gap="large")
    with col_a:
        st.markdown("""
<div class="card">
  <div class="card-title">Transfer Learning คืออะไร?</div>
  <div class="card-body">
    แทนที่จะ train โมเดลจาก scratch โดยใช้ dataset เล็กๆ เราสามารถ
    <strong style="color:#e8dfd0;">ยืม knowledge</strong> จากโมเดลที่ train บน ImageNet (~14M รูป) มาแล้ว<br><br>
    โมเดลเหล่านี้เรียนรู้ feature พื้นฐานของภาพแล้ว เช่น:
    <ul style="color:#7a6a52; line-height:2;">
      <li>ขอบ, เส้น, มุม (early layers)</li>
      <li>พื้นผิว, วัตถุพื้นฐาน (mid layers)</li>
      <li>รูปทรงซับซ้อน (deep layers)</li>
    </ul>
    เราเพียงแค่ <strong style="color:#e8dfd0;">เพิ่ม classifier head ใหม่</strong>
    แล้ว fine-tune ให้รู้จักสไตล์ภาพวาด
  </div>
</div>
""", unsafe_allow_html=True)
    with col_b:
        st.markdown("""
<div class="card">
  <div class="card-title">⚡ EfficientNetB0 — Base Model</div>
  <div class="card-body">
    <strong style="color:#e8dfd0;">EfficientNet</strong> เป็น CNN architecture ที่ scale ทั้ง depth, width, และ resolution
    พร้อมกันอย่างสมดุล (Compound Scaling) ทำให้ได้ accuracy สูงด้วย parameter น้อยกว่า
    ResNet หรือ VGG อย่างมาก<br><br>
    <strong style="color:#7aaac8;">ทำไมเลือก EfficientNetB0?</strong>
    <ul style="color:#7a6a52; line-height:2;">
      <li>Parameters: ~5.3M — เบา เหมาะกับ dataset ขนาดกลาง</li>
      <li>ImageNet accuracy: 77.1% Top-1</li>
      <li>Pretrained weight จาก <code>imagenet</code></li>
      <li>Input: <code>224×224</code> หรือปรับได้</li>
    </ul>
    <div class="info-box">
      Load ด้วย: <code>tf.keras.applications.EfficientNetB0(weights='imagenet', include_top=False)</code>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

with tab3:
    st.markdown("""
<div class="card">
  <div class="card-title">กลยุทธ์การ Fine-Tune แบบ 2 Phase</div>
  <div class="card-body" style="font-size:1rem;">
  </div>
</div>
""", unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown("""
<div class="card" style="border-color:#3d4a5a;">
  <div class="card-icon">🧊</div>
  <div class="card-title" style="color:#7aaac8;">Phase 1 — Feature Extraction</div>
  <div class="card-body">
    <strong>Freeze</strong> layers ทั้งหมดของ EfficientNetB0<br>
    เพิ่มเฉพาะ classifier head ใหม่แล้ว train เฉพาะส่วนนั้น<br><br>
    <code>base_model.trainable = False</code><br><br>
    <ul style="color:#7a6a52; line-height:2;">
      <li>Epochs: 10–15</li>
      <li>Learning Rate: <code>1e-3</code></li>
      <li>Optimizer: Adam</li>
    </ul>
    จุดประสงค์: ให้ head เรียนรู้ features ของงานศิลปะก่อน
    โดยไม่ทำลาย pretrained weights
  </div>
</div>
""", unsafe_allow_html=True)
    with c2:
        st.markdown("""
<div class="card" style="border-color:#5a3a1a;">
  <div class="card-icon">🔥</div>
  <div class="card-title" style="color:#d0924c;">Phase 2 — Fine-Tuning</div>
  <div class="card-body">
    <strong>Unfreeze</strong> layers บนสุด 20–30 ชั้นสุดท้ายของ base model<br>
    train ทั้งระบบด้วย learning rate ต่ำมาก<br><br>
    <code>base_model.trainable = True</code><br><br>
    <ul style="color:#7a6a52; line-height:2;">
      <li>Epochs: 20–30 (+ EarlyStopping)</li>
      <li>Learning Rate: <code>1e-5</code> (ต่ำมาก)</li>
      <li>Optimizer: Adam</li>
    </ul>
    จุดประสงค์: ปรับ deep features ให้ sensitive กับ
    สไตล์การวาดของแต่ละศิลปิน
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="gold-rule">', unsafe_allow_html=True)

# ─── SECTION 5: MODEL ARCHITECTURE CODE ───────────────────────────────────────
st.markdown('<p class="section-label">05</p><h2 class="section-title">โค้ดโมเดล</h2>', unsafe_allow_html=True)

col_code, col_cfg = st.columns([3, 2], gap="large")
with col_code:
    st.code("""
import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow.keras.applications import EfficientNetB0

ARTISTS = [
    'Vincent_van_Gogh', 'Edgar_Degas', 'Pablo_Picasso',
    'Pierre-Auguste_Renoir', 'Albrecht_Durer', 'Paul_Gauguin',
    'Francisco_Goya', 'Rembrandt', 'Alfred_Sisley', 'Titian'
]
NUM_CLASSES = len(ARTISTS)   # 10
IMG_SIZE    = (128, 128)

# ── Base model (frozen) ───────────────────────────
base = EfficientNetB0(
    weights='imagenet',
    include_top=False,
    input_shape=(*IMG_SIZE, 3)
)
base.trainable = False   # Phase 1: freeze

# ── Custom classification head ────────────────────
x = base.output
x = layers.GlobalAveragePooling2D()(x)
x = layers.BatchNormalization()(x)
x = layers.Dense(256, activation='relu')(x)
x = layers.Dropout(0.5)(x)
x = layers.Dense(128, activation='relu')(x)
x = layers.Dropout(0.3)(x)
output = layers.Dense(NUM_CLASSES, activation='softmax')(x)

model = Model(inputs=base.input, outputs=output)

# ── Compile ───────────────────────────────────────
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
    loss='categorical_crossentropy',
    metrics=['accuracy', tf.keras.metrics.TopKCategoricalAccuracy(k=3)]
)

# ── Callbacks ────────────────────────────────────
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_accuracy', patience=5, restore_best_weights=True
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss', factor=0.5, patience=3, min_lr=1e-7
    ),
    tf.keras.callbacks.ModelCheckpoint(
        'best_model.keras', save_best_only=True, monitor='val_accuracy'
    ),
]
""", language="python")

with col_cfg:
    st.markdown("""
<div class="card">
  <div class="card-title">⚙️ Training Config</div>
  <div class="card-body">
    <table style="width:100%; font-size:0.88rem; border-collapse:collapse;">
      <tr><td style="color:#6b5a3e; padding:0.3rem 0;">Batch Size</td><td style="color:#e8dfd0; text-align:right;"><code>32</code></td></tr>
      <tr><td style="color:#6b5a3e; padding:0.3rem 0;">Phase 1 LR</td><td style="color:#e8dfd0; text-align:right;"><code>1e-3</code></td></tr>
      <tr><td style="color:#6b5a3e; padding:0.3rem 0;">Phase 2 LR</td><td style="color:#e8dfd0; text-align:right;"><code>1e-5</code></td></tr>
      <tr><td style="color:#6b5a3e; padding:0.3rem 0;">Loss</td><td style="color:#e8dfd0; text-align:right;"><code>categorical_crossentropy</code></td></tr>
      <tr><td style="color:#6b5a3e; padding:0.3rem 0;">Optimizer</td><td style="color:#e8dfd0; text-align:right;"><code>Adam</code></td></tr>
      <tr><td style="color:#6b5a3e; padding:0.3rem 0;">Dropout</td><td style="color:#e8dfd0; text-align:right;"><code>0.5 / 0.3</code></td></tr>
      <tr><td style="color:#6b5a3e; padding:0.3rem 0;">Metrics</td><td style="color:#e8dfd0; text-align:right;"><code>acc, top-3 acc</code></td></tr>
    </table>
  </div>
</div>
<br>
<div class="card">
  <div class="card-title">📈 Data Augmentation</div>
  <div class="card-body">
    <code>RandomFlip("horizontal")</code><br>
    <code>RandomRotation(0.15)</code><br>
    <code>RandomZoom(0.15)</code><br>
    <code>RandomBrightness(0.2)</code><br>
    <code>RandomContrast(0.2)</code><br>
    <code>preprocess_input()</code> — EfficientNet scaling
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="gold-rule">', unsafe_allow_html=True)

# ─── SECTION 6: DEVELOPMENT STEPS ────────────────────────────────────────────
st.markdown('<p class="section-label">06</p><h2 class="section-title">ขั้นตอนการพัฒนา</h2>', unsafe_allow_html=True)

all_steps = [
    ("Load & Filter Dataset", "โหลดภาพจากโฟลเดอร์ทั้ง 10 ศิลปิน ลบรูป corrupt และ grayscale ออก กรองเฉพาะ <code>.jpg/.jpeg/.png</code>"),
    ("Explore & Visualize", "ตรวจสอบ class distribution, แสดงตัวอย่างภาพแต่ละศิลปิน และหาค่า min/max/mean ของจำนวนภาพต่อคลาส"),
    ("Preprocess Images", "Resize → 128×128, normalize ด้วย <code>preprocess_input</code>, one-hot encode labels, stratified split"),
    ("Build Base CNN (Baseline)", "สร้าง CNN จาก scratch เพื่อเป็น baseline ก่อน ประเมิน accuracy ว่าอยู่ที่ระดับใด"),
    ("Transfer Learning Phase 1", "Load EfficientNetB0 (frozen), ต่อ head ใหม่, train 15 epochs, ดู val_accuracy ที่ได้"),
    ("Fine-Tuning Phase 2", "Unfreeze 30 layers สุดท้าย, ลด LR เป็น 1e-5, train อีก 30 epochs พร้อม EarlyStopping"),
    ("Evaluate & Analyze", "วัด Test Accuracy, Top-3 Accuracy, สร้าง Confusion Matrix และ Classification Report"),
    ("Save & Deploy", "บันทึกโมเดลเป็น <code>.keras</code> และ <code>.pkl</code> สำหรับ scaler/label encoder"),
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
    ("📦 Dataset", "Best Artworks of All Time", "https://www.kaggle.com/datasets/ikarus777/best-artworks-of-all-time"),
    ("📖 Paper", "EfficientNet: Rethinking Model Scaling for CNNs — Tan & Le, 2019", "https://arxiv.org/abs/1905.11946"),
    ("📖 Paper", "HOG Features — Dalal & Triggs, CVPR 2005", "https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf"),
    ("📚 Docs", "TensorFlow / Keras Documentation", "https://www.tensorflow.org/api_docs"),
    ("📚 Docs", "Keras Transfer Learning Guide", "https://keras.io/guides/transfer_learning/"),
    ("📚 Docs", "scikit-learn Documentation", "https://scikit-learn.org/stable/"),
]

ref_cols = st.columns(3)
for i, (tag, title, url) in enumerate(refs):
    with ref_cols[i % 3]:
        st.markdown(f"""
<div class="card" style="margin-bottom:0.75rem;">
  <div style="font-family:'DM Mono',monospace; font-size:0.7rem; color:#6b5a3e; margin-bottom:0.3rem;">{tag}</div>
  <a href="{url}" target="_blank" style="color:#c9a84c; font-size:0.9rem; text-decoration:none;">{title}</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding: 3rem 0 1rem 0; color: #3d2e1a; font-family:'DM Mono',monospace; font-size:0.72rem; letter-spacing:0.1em;">
NEURAL NETWORK · PAINTING STYLE CLASSIFICATION · 10 MASTER ARTISTS
</div>
""", unsafe_allow_html=True)