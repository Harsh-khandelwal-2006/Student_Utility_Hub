"""
Student Utility Hub  |  Developer: Harsh Khandelwal
Run:  streamlit run Student_Utility_Hub.py
Note: 'Bengaluru_House_Data_Cleaned.csv' file isi folder me honi chahiye (House Price module ke liye).
"""
from html import escape
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

DEVELOPER = "Harsh Khandelwal"
DATA_FILE = Path(__file__).with_name("Bengaluru_House_Data_Cleaned.csv")

st.set_page_config(page_title="Student Utility Hub", page_icon="⚡", layout="wide")


MODULES = {
    "Home":                   ("🏠", "#6366F1", "#EC4899", "Welcome! Ek hi jagah par saare student tools.", ["⚡", "✨", "🚀", "💡"]),
    "Todo List":              ("📝", "#06B6D4", "#3B82F6", "Apne daily tasks plan karo aur complete karo.", ["✓", "📝", "⏰", "★"]),
    "Calculator":             ("🧮", "#A855F7", "#EC4899", "Fast & smart calculator with history.", ["+", "−", "×", "÷", "%", "="]),
    "Student Marks":          ("🎓", "#10B981", "#84CC16", "Percentage, grade aur scholarship eligibility check karo.", ["🎓", "A+", "📚", "🏆"]),
    "Performance Dashboard":  ("📊", "#F59E0B", "#EF4444", "Marks ka analysis charts ke sath dekho.", ["📊", "📈", "%", "★"]),
    "House Price Prediction": ("🏡", "#14B8A6", "#6366F1", "Real Bengaluru data se ghar ki price predict karo.", ["🏠", "₹", "🏢", "🔑"]),
}

with st.sidebar:
    st.markdown("## ⚡ Student Hub")
    st.caption(f"Developer: **{DEVELOPER}**")
    st.markdown("---")
    page = st.radio(
        "Module", list(MODULES), key="nav",
        format_func=lambda n: f"{MODULES[n][0]}  {n}",
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.caption("🚀 Final Year Project")

ICON, C1, C2, SUB, SYMBOLS = MODULES[page]

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');
:root { --c1:__C1__; --c2:__C2__; --panel:rgba(255,255,255,.06); --line:rgba(255,255,255,.12); }

@property --ang { syntax:'<angle>'; inherits:false; initial-value:0deg; }
@property --n   { syntax:'<integer>'; inherits:false; initial-value:0; }

html, body, .stApp, [class*="css"] { font-family:'Poppins',sans-serif; }

/* ---------- keyframes ---------- */
@keyframes bgmove  { 0%{background-position:0% 50%} 50%{background-position:100% 50%} 100%{background-position:0% 50%} }
@keyframes float   { from{transform:translateY(-15px) scale(1)} to{transform:translateY(15px) scale(1.06)} }
@keyframes fadeUp  { from{opacity:0; transform:translateY(24px)} to{opacity:1; transform:translateY(0)} }
@keyframes slideIn { from{opacity:0; transform:translateX(-40px)} to{opacity:1; transform:translateX(0)} }
@keyframes pulse   { 0%,100%{box-shadow:0 0 0 0 __C1__66} 50%{box-shadow:0 0 0 14px transparent} }
@keyframes spin    { to{ --ang:360deg } }
@keyframes count   { from{ --n:0 } }
@keyframes pop     { 0%{opacity:0; transform:scale(.3)} 60%{transform:scale(1.12)} 100%{opacity:1; transform:scale(1)} }
@keyframes rise    { 0%{transform:translateY(0) rotate(0); opacity:0} 10%{opacity:.35} 90%{opacity:.35} 100%{transform:translateY(-110vh) rotate(360deg); opacity:0} }
@keyframes blink   { 50%{opacity:0} }
@keyframes wobble  { 0%,100%{transform:rotate(-14deg) scale(1)} 50%{transform:rotate(14deg) scale(1.3)} }
@keyframes glow    { 0%,100%{text-shadow:0 0 6px __C1__88} 50%{text-shadow:0 0 22px __C1__} }

/* ---------- background ---------- */
.stApp {
  background: linear-gradient(-45deg,#0b0b18,#12102b,#0b1a2b,#1a0f24);
  background-size:400% 400%; animation:bgmove 18s ease infinite; color:#f5f5fa;
}
.stApp::before {
  content:""; position:fixed; inset:0; pointer-events:none; z-index:0;
  background: radial-gradient(500px circle at 15% 20%, __C1__33, transparent 60%),
              radial-gradient(600px circle at 85% 80%, __C2__2e, transparent 60%);
  animation:float 10s ease-in-out infinite alternate;
}
.floaters { position:fixed; inset:0; pointer-events:none; overflow:hidden; z-index:0; }
.floaters span { position:absolute; bottom:-60px; color:var(--c1); opacity:0; font-weight:700; animation:rise linear infinite; }

#MainMenu, footer { visibility:hidden; }
header[data-testid="stHeader"] { background:transparent; }
.block-container { max-width:1100px; padding-top:1.5rem; position:relative; z-index:1; }
.block-container > div > div { animation:fadeUp .6s ease backwards; }
[data-testid="stHorizontalBlock"] > div { animation:fadeUp .6s ease backwards; }
[data-testid="stHorizontalBlock"] > div:nth-child(2) { animation-delay:.1s; }
[data-testid="stHorizontalBlock"] > div:nth-child(3) { animation-delay:.2s; }
[data-testid="stHorizontalBlock"] > div:nth-child(4) { animation-delay:.3s; }
[data-testid="stHorizontalBlock"] > div:nth-child(5) { animation-delay:.4s; }

/* ---------- hero ---------- */
.hero {
  display:flex; align-items:center; gap:20px; padding:26px 30px; border-radius:22px;
  background:linear-gradient(120deg,__C1__,__C2__); background-size:200% 200%;
  animation:bgmove 8s ease infinite, slideIn .7s ease both;
  box-shadow:0 12px 40px __C1__55; margin-bottom:18px;
}
.hero .emoji { font-size:56px; animation:float 3s ease-in-out infinite alternate; }
.hero h1 { margin:0; font-size:36px; font-weight:800; color:#fff; }
.hero p  { margin:4px 0 0; color:rgba(255,255,255,.9); font-size:15px; }

.sec { font-size:18px; font-weight:700; margin:22px 0 10px; display:flex; align-items:center; gap:10px; }
.sec::after { content:""; flex:1; height:2px; background:linear-gradient(90deg,var(--c1),transparent); }

/* ---------- sidebar ---------- */
[data-testid="stSidebar"] { background:rgba(10,10,22,.92); border-right:1px solid var(--line); }
[data-testid="stSidebar"] div[role="radiogroup"] { gap:8px; }
[data-testid="stSidebar"] div[role="radiogroup"] label {
  background:var(--panel); border:1px solid var(--line); border-radius:14px;
  padding:10px 14px; width:100%; transition:all .25s ease;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:hover { transform:translateX(6px); border-color:var(--c1); }
[data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child { display:none; }
[data-testid="stSidebar"] div[role="radiogroup"] label p { margin:0; font-weight:600; color:#b4b4c8; }
[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
  background:linear-gradient(120deg,__C1__55,__C2__55); border-color:var(--c1); animation:pulse 2s infinite;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p { color:#fff; }

/* ---------- inputs ---------- */
.stTextInput input, .stNumberInput input, div[data-baseweb="select"] > div {
  background:rgba(255,255,255,.07) !important; color:#fff !important;
  border:1px solid var(--line) !important; border-radius:12px !important; transition:all .25s;
}
.stTextInput input:focus, .stNumberInput input:focus { border-color:var(--c1) !important; box-shadow:0 0 14px __C1__77 !important; transform:scale(1.01); }
[data-testid="stFileUploader"] section { background:var(--panel); border:2px dashed var(--c1); border-radius:16px; transition:all .3s; }
[data-testid="stFileUploader"] section:hover { transform:scale(1.02); box-shadow:0 0 24px __C1__55; }

/* ---------- buttons ---------- */
.stButton > button, .stFormSubmitButton > button {
  width:100%; border:none; border-radius:12px; padding:.6rem 1.2rem; font-weight:700; color:#fff !important;
  background:linear-gradient(120deg,var(--c1),var(--c2)); background-size:200% 200%;
  transition:all .25s ease; box-shadow:0 6px 18px __C1__55;
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
  transform:translateY(-3px) scale(1.03); box-shadow:0 10px 26px __C1__99; animation:bgmove 2s ease infinite;
}
.stButton > button:active, .stFormSubmitButton > button:active { transform:scale(.93); }
.stButton > button p, .stFormSubmitButton > button p { color:#fff !important; }

/* ---------- cards (rotating gradient border) ---------- */
[data-testid="stVerticalBlockBorderWrapper"] {
  border:2px solid transparent !important; border-radius:20px;
  background:linear-gradient(#14142b,#14142b) padding-box,
             conic-gradient(from var(--ang), __C1__, __C2__, __C1__) border-box;
  animation:spin 6s linear infinite, fadeUp .6s ease backwards;
}
[data-testid="stMetric"] {
  background:var(--panel); border:1px solid var(--line); border-radius:16px; padding:14px 18px;
  border-bottom:3px solid var(--c1); transition:transform .25s, box-shadow .25s; animation:pop .6s ease backwards;
}
[data-testid="stMetric"]:hover { transform:translateY(-6px); box-shadow:0 10px 24px __C1__44; }
[data-testid="stMetricValue"] { font-weight:800; }
[data-testid="stProgress"] [role="progressbar"] > div { background:linear-gradient(90deg,var(--c1),var(--c2),var(--c1)) !important; background-size:200% 100%; animation:bgmove 2s linear infinite; }
div[data-testid="stAlert"] { animation:pop .5s ease both; border-radius:14px; }

.stat { background:var(--panel); border:1px solid var(--line); border-radius:16px; padding:16px; text-align:center;
        border-top:3px solid var(--c1); transition:transform .25s, box-shadow .25s; }
.stat:hover { transform:translateY(-6px) scale(1.03); box-shadow:0 10px 24px __C1__44; }
.stat b { display:block; font-size:30px; background:linear-gradient(120deg,var(--c1),var(--c2)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.stat b.count { animation:count 1.4s ease-out both; counter-reset:num var(--n); }
.stat b.count::before { content:counter(num); }
.stat span { color:#a5a5bd; font-size:13px; }

.task { display:flex; align-items:center; padding:10px 16px; border-radius:14px; background:var(--panel);
        border:1px solid var(--line); border-left:5px solid var(--c1); font-weight:500; transition:all .3s; }
.task:hover { transform:translateX(8px); background:rgba(255,255,255,.1); }
.task.done { border-left-color:#10B981; opacity:.6; text-decoration:line-through; }

.screen { display:flex; justify-content:center; align-items:center; gap:18px; padding:16px; border-radius:16px;
          background:#06060f; border:1px solid var(--c1); box-shadow:inset 0 0 25px __C1__44;
          font-family:'Courier New',monospace; font-size:34px; font-weight:700; color:var(--c1); animation:glow 2.5s infinite; }
.screen .sym { display:inline-block; animation:wobble 2s ease-in-out infinite; color:var(--c2); font-size:44px; }
.screen .cur { animation:blink 1s infinite; }

.result { margin-top:14px; padding:20px 26px; border-radius:18px; text-align:center;
          background:linear-gradient(120deg,__C1__33,__C2__33); border:1px solid var(--c1);
          animation:pop .6s cubic-bezier(.34,1.56,.64,1) both; }
.result small { color:#c8c8dc; } .result h2 { margin:4px 0 0; font-size:44px; font-weight:800; animation:glow 2s infinite; }

.hist { padding:8px 14px; margin-bottom:6px; border-radius:10px; background:var(--panel); border-left:4px solid var(--c1); animation:slideIn .4s ease both; transition:transform .2s; }
.hist:hover { transform:translateX(6px); }
.modcard { font-size:44px; animation:float 3s ease-in-out infinite alternate; display:inline-block; }
.footer { text-align:center; color:#8a8aa3; font-size:13px; margin-top:40px; }
.footer b { color:var(--c1); }
</style>
"""
st.markdown(CSS.replace("__C1__", C1).replace("__C2__", C2), unsafe_allow_html=True)


def show_html(code, height):
    """HTML + JS widget (naye aur purane dono Streamlit versions par chalta hai)."""
    if hasattr(st, "iframe"):
        st.iframe(code, height=height)
    else:
        import streamlit.components.v1 as components
        components.html(code, height=height)


def floaters(symbols):
    """Background me upar uthte hue floating symbols."""
    spans = "".join(
        f'<span style="left:{(i * 73) % 100}%;font-size:{22 + (i * 7) % 26}px;'
        f'animation-duration:{9 + (i * 5) % 9}s;animation-delay:-{(i * 2.3) % 12:.1f}s">{symbols[i % len(symbols)]}</span>'
        for i in range(14)
    )
    st.markdown(f'<div class="floaters">{spans}</div>', unsafe_allow_html=True)


def hero():
    st.markdown(
        f'<div class="hero"><div class="emoji">{ICON}</div>'
        f'<div><h1>{page}</h1><p>{SUB}</p></div></div>',
        unsafe_allow_html=True,
    )


def section(text):
    st.markdown(f'<div class="sec">{text}</div>', unsafe_allow_html=True)


def stat(col, number, label):
    if isinstance(number, int):  # numbers count-up animation ke sath
        html_num = f'<b class="count" style="--n:{number}"></b>'
    else:
        html_num = f"<b>{number}</b>"
    col.markdown(f'<div class="stat">{html_num}<span>{label}</span></div>', unsafe_allow_html=True)


floaters(SYMBOLS)
hero()


show_html(
    f"""
<div style="font-family:Poppins,sans-serif;display:flex;justify-content:space-between;padding:8px 18px;
 border-radius:12px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);color:#fff;font-size:13px;font-weight:600">
 <span id="g"></span><span id="t" style="color:{C1};font-weight:800"></span></div>
<script>
function tick(){{var d=new Date(),h=d.getHours();
 document.getElementById('g').textContent=(h<12?'Good morning':h<17?'Good afternoon':'Good evening')+' 👋  |  {DEVELOPER}';
 document.getElementById('t').textContent=d.toLocaleDateString([], {{weekday:'short',day:'numeric',month:'short'}})+' • '+d.toLocaleTimeString();}}
tick();setInterval(tick,1000);
</script>""",
    height=46,
)


if page == "Home":

    def open_page(name):
        st.session_state.nav = name  # sidebar radio ko change karta hai

    show_html(
        """
<style>
 *{box-sizing:border-box;font-family:Poppins,sans-serif}
 body{margin:0}
 .wrap{position:relative;overflow:hidden;border-radius:24px;height:290px;box-shadow:0 14px 40px rgba(0,0,0,.45)}
 .track{display:flex;height:100%;transition:transform .8s cubic-bezier(.77,0,.18,1)}
 .slide{min-width:100%;height:100%;display:flex;align-items:center;justify-content:space-between;padding:0 70px;color:#fff}
 .slide h2{font-size:32px;margin:0 0 8px;font-weight:800}
 .slide p{margin:0 0 18px;font-size:15px;opacity:.92;max-width:430px}
 .slide .big{font-size:105px;animation:bounce 2.4s ease-in-out infinite}
 .slide .txt{opacity:0;transform:translateX(-50px);transition:all .8s ease .3s}
 .slide.active .txt{opacity:1;transform:translateX(0)}
 .go{border:none;border-radius:30px;padding:11px 26px;font-size:15px;font-weight:700;color:#222;background:#fff;cursor:pointer;
     box-shadow:0 6px 18px rgba(0,0,0,.3);transition:all .25s}
 .go:hover{transform:translateY(-3px) scale(1.07);box-shadow:0 10px 26px rgba(0,0,0,.45)}
 .go:active{transform:scale(.94)}
 @keyframes bounce{0%,100%{transform:translateY(0) rotate(-4deg)}50%{transform:translateY(-18px) rotate(4deg)}}
 .dots{position:absolute;bottom:14px;left:50%;transform:translateX(-50%);display:flex;gap:8px}
 .dot{width:10px;height:10px;border-radius:50%;background:rgba(255,255,255,.4);cursor:pointer;transition:all .3s}
 .dot.on{width:30px;border-radius:10px;background:#fff}
 .btn{position:absolute;top:50%;transform:translateY(-50%);width:42px;height:42px;border:none;border-radius:50%;
      background:rgba(255,255,255,.25);color:#fff;font-size:20px;cursor:pointer;backdrop-filter:blur(6px);transition:.2s}
 .btn:hover{background:rgba(255,255,255,.5);transform:translateY(-50%) scale(1.12)}
 .prev{left:12px}.next{right:12px}
 .bar{position:absolute;bottom:0;left:0;height:4px;background:#fff;width:0}
</style>
<div class="wrap" id="w">
 <div class="track" id="tr">
  <div class="slide" style="background:linear-gradient(120deg,#6366F1,#EC4899)"><div class="txt"><h2>⚡ Student Utility Hub</h2><p>5 powerful tools ek hi app me — padhai ko banao easy aur smart.</p><button class="go" onclick="openMod('Todo List')">Get Started 🚀</button></div><div class="big">🚀</div></div>
  <div class="slide" style="background:linear-gradient(120deg,#06B6D4,#3B82F6)"><div class="txt"><h2>📝 Todo List</h2><p>Tasks add karo, tick karo aur progress bar se productivity track karo.</p><button class="go" onclick="openMod('Todo List')">Open Todo List →</button></div><div class="big">✅</div></div>
  <div class="slide" style="background:linear-gradient(120deg,#A855F7,#EC4899)"><div class="txt"><h2>🧮 Calculator</h2><p>Live screen, 6 operations aur calculation history ke sath.</p><button class="go" onclick="openMod('Calculator')">Open Calculator →</button></div><div class="big">➗</div></div>
  <div class="slide" style="background:linear-gradient(120deg,#10B981,#84CC16)"><div class="txt"><h2>🎓 Student Marks</h2><p>Percentage, grade aur scholarship eligibility ek click me.</p><button class="go" onclick="openMod('Student Marks')">Open Student Marks →</button></div><div class="big">🏆</div></div>
  <div class="slide" style="background:linear-gradient(120deg,#F59E0B,#EF4444)"><div class="txt"><h2>📊 Performance Dashboard</h2><p>Marks ke charts dekho aur weak subject pehchano.</p><button class="go" onclick="openMod('Performance Dashboard')">Open Dashboard →</button></div><div class="big">📈</div></div>
  <div class="slide" style="background:linear-gradient(120deg,#14B8A6,#6366F1)"><div class="txt"><h2>🏡 House Price Prediction</h2><p>Real Bengaluru dataset par trained ML model.</p><button class="go" onclick="openMod('House Price Prediction')">Open House Price →</button></div><div class="big">🏘️</div></div>
 </div>
 <button class="btn prev" onclick="go(i-1)">‹</button><button class="btn next" onclick="go(i+1)">›</button>
 <div class="dots" id="dots"></div><div class="bar" id="bar"></div>
</div>
<script>
 var tr=document.getElementById('tr'),sl=document.querySelectorAll('.slide'),dots=document.getElementById('dots'),bar=document.getElementById('bar'),i=0,timer;
 sl.forEach(function(_,k){var d=document.createElement('div');d.className='dot';d.onclick=function(){go(k)};dots.appendChild(d)});
 function go(n){i=(n+sl.length)%sl.length;tr.style.transform='translateX(-'+i*100+'%)';
  sl.forEach(function(s,k){s.classList.toggle('active',k==i)});
  document.querySelectorAll('.dot').forEach(function(d,k){d.classList.toggle('on',k==i)});
  bar.style.transition='none';bar.style.width='0';setTimeout(function(){bar.style.transition='width 4s linear';bar.style.width='100%'},50);
  clearInterval(timer);timer=setInterval(function(){go(i+1)},4000);}
 // Button click -> sidebar ka module open karo
 function openMod(name){
  try{
   var labels=window.parent.document.querySelectorAll('[data-testid="stSidebar"] label');
   for(var k=0;k<labels.length;k++){ if(labels[k].innerText.indexOf(name)>-1){ labels[k].click(); return; } }
  }catch(e){}
 }
 go(0);
</script>""",
        height=310,
    )

    section("✨ Modules (click karke open karo)")
    names = [n for n in MODULES if n != "Home"]
    for row in (names[:3], names[3:]):
        for col, n in zip(st.columns(3), row):
            icon, _, _, desc, _ = MODULES[n]
            with col.container(border=True):
                st.markdown(
                    f'<div class="modcard">{icon}</div><br><b style="font-size:17px">{n}</b><br>'
                    f'<span style="color:#a5a5bd;font-size:13px">{desc}</span>',
                    unsafe_allow_html=True,
                )
                st.button("Open →", key=f"open_{n}", on_click=open_page, args=(n,))

elif page == "Todo List":
    if "tasks" not in st.session_state:
        st.session_state.tasks = []
        st.session_state.next_id = 1

    def toggle(task_id):
        for t in st.session_state.tasks:
            if t["id"] == task_id:
                t["done"] = st.session_state[f"chk{task_id}"]

    def delete(task_id):
        st.session_state.tasks = [t for t in st.session_state.tasks if t["id"] != task_id]

    def clear_done():
        st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]

    section("➕ Naya Task")
    with st.form("add_task", clear_on_submit=True):
        title = st.text_input("Task likho aur Enter dabao", placeholder="Jaise: Maths ka assignment complete karna")
        if st.form_submit_button("Add Task") and title.strip():
            st.session_state.tasks.append({"id": st.session_state.next_id, "title": title.strip(), "done": False})
            st.session_state.next_id += 1
            st.rerun()

    tasks = st.session_state.tasks
    total = len(tasks)
    done = sum(t["done"] for t in tasks)
    section("📊 Progress")
    a, b, c = st.columns(3)
    stat(a, total, "Total Tasks")
    stat(b, total - done, "Pending")
    stat(c, done, "Completed")
    st.write("")
    st.progress(done / total if total else 0.0, text=f"{done} / {total} tasks complete")

    section("📋 Tumhare Tasks")
    if not tasks:
        st.info("Abhi koi task nahi hai. Upar se add karo 👆")
    for t in tasks:
        c1_, c2_, c3_ = st.columns([0.08, 0.77, 0.15])
        c1_.checkbox("done", value=t["done"], key=f"chk{t['id']}", on_change=toggle, args=(t["id"],), label_visibility="collapsed")
        c2_.markdown(f'<div class="task {"done" if t["done"] else ""}">{escape(t["title"])}</div>', unsafe_allow_html=True)
        c3_.button("🗑", key=f"del{t['id']}", on_click=delete, args=(t["id"],))

    if done:
        st.write("")
        st.button("🧹 Completed tasks hatao", on_click=clear_done)

elif page == "Calculator":
    OPS = {
        "➕ Addition": ("+", lambda a, b: a + b),
        "➖ Subtraction": ("−", lambda a, b: a - b),
        "✖️ Multiplication": ("×", lambda a, b: a * b),
        "➗ Division": ("÷", lambda a, b: a / b),
        "⚡ Power": ("^", lambda a, b: a ** b),
        "📐 Modulus": ("%", lambda a, b: a % b),
    }
    if "history" not in st.session_state:
        st.session_state.history = []

    left, right = st.columns([3, 2])
    with left:
        with st.container(border=True):
            screen = st.empty()  # live screen (inputs ke baad fill hoti hai)
            x, y = st.columns(2)
            n1 = x.number_input("Pehla number", value=0.0, key="n1")
            n2 = y.number_input("Dusra number", value=0.0, key="n2")
            op = st.selectbox("Operation chuno", list(OPS))
            go = st.button("Calculate")
            symbol, fn = OPS[op]
            screen.markdown(
                f'<div class="screen"><span>{n1:g}</span><span class="sym">{symbol}</span>'
                f'<span>{n2:g}</span><span>=</span><span class="cur">?</span></div>',
                unsafe_allow_html=True,
            )

        if go:
            try:
                res = fn(n1, n2)
                st.session_state.history.insert(0, f"{n1:g} {symbol} {n2:g} = {res:g}")
                st.markdown(f'<div class="result"><small>{op}</small><h2>{res:g}</h2></div>', unsafe_allow_html=True)
            except (ZeroDivisionError, OverflowError):
                st.error("Ye calculation possible nahi hai (zero se divide / bahut bada number).")

    with right:
        section("🕘 History")
        if st.session_state.history:
            for h in st.session_state.history[:8]:
                st.markdown(f'<div class="hist">{h}</div>', unsafe_allow_html=True)
            st.button("Clear History", on_click=lambda: st.session_state.history.clear())
        else:
            st.caption("Abhi koi calculation nahi hui.")


elif page == "Student Marks":
    SUBJECTS = ["Math", "English", "Hindi", "Science", "Computer"]
    with st.container(border=True):
        a, b = st.columns([2, 1])
        name = a.text_input("Tumhara naam")
        age = b.number_input("Age", 1, 100, 18)

        section("📚 Marks Enter Karo (out of 100)")
        cols = st.columns(5)
        marks = [cols[i].number_input(s, 0.0, 100.0, key=f"m_{s}") for i, s in enumerate(SUBJECTS)]
        code = st.text_input("Scholarship code", placeholder="SCH100 / SCH200 / SCH300")
        go = st.button("Result Dekho")

    if go:
        if not name.strip():
            st.warning("Pehle apna naam likho.")
        else:
            total = sum(marks)
            pct = total / 5
            grade = "A+" if pct >= 90 else "A" if pct >= 75 else "B" if pct >= 60 else "C" if pct >= 40 else "Fail"

            st.success(f"Hello {name.strip()} 👋")
            section("🏅 Result")
            m1, m2, m3 = st.columns(3)
            m1.metric("Total Marks", f"{total:g} / 500")
            m2.metric("Percentage", f"{pct:.2f}%")
            m3.metric("Grade", grade)
            st.progress(min(pct / 100, 1.0))

            section("✅ Eligibility")
            e1, e2, e3 = st.columns(3)
            (e1.success if 18 <= age <= 25 else e1.error)("Age: Allowed" if 18 <= age <= 25 else "Age: Not Allowed")
            (e2.success if pct >= 75 else e2.error)("Percentage: Eligible" if pct >= 75 else "Percentage: Not Eligible")
            ok = code.strip().upper() in ("SCH100", "SCH200", "SCH300")
            (e3.success if ok else e3.error)("Scholarship: Eligible" if ok else "Scholarship: Not Eligible")
            if pct >= 90:
                st.balloons()


elif page == "Performance Dashboard":
    section("✏️ Apne Marks Edit Karo (table me click karke badlo)")
    default = pd.DataFrame(
        {"Unit Test": [72, 65, 80, 70, 85], "Mid Term": [78, 70, 82, 75, 88],
         "Pre-Board": [84, 74, 85, 80, 90], "Final": [88, 79, 87, 85, 94]},
        index=["Math", "English", "Hindi", "Science", "Computer"],
    )
    df = st.data_editor(default, key="perf_table").clip(0, 100)

    subject_avg = df.mean(axis=1)
    exam_avg = df.mean(axis=0)
    growth = exam_avg.iloc[-1] - exam_avg.iloc[0]

    section("📌 Summary")
    a, b, c, d = st.columns(4)
    a.metric("Overall Average", f"{subject_avg.mean():.1f}%")
    b.metric("Best Subject", subject_avg.idxmax())
    c.metric("Needs Focus", subject_avg.idxmin())
    d.metric("Improvement", f"{growth:+.1f}%")

    g1, g2 = st.columns(2)
    with g1:
        section("📊 Subject-wise Average")
        st.bar_chart(subject_avg, color=C1)
    with g2:
        section("📈 Exam-wise Progress")
        st.line_chart(exam_avg, color=C2)

    weak = subject_avg.idxmin()
    st.info(f"💡 Tip: **{weak}** me average sabse kam hai ({subject_avg.min():.1f}%). Isme extra practice karo!")


else:
    if not DATA_FILE.exists():
        st.error(f"Dataset file nahi mili: `{DATA_FILE.name}` — ise `Student_Utility_Hub.py` ke same folder me rakho.")
        st.stop()

    @st.cache_data
    def load_data_and_model(path):
        data = pd.read_csv(path)
        top = data["location"].value_counts().head(15).index.tolist()
        locs = top + ["Other"]
        data["loc"] = data["location"].where(data["location"].isin(top), "Other")

        def features(d):
            cols = [(d["loc"] == l).astype(float) for l in locs]
            return np.column_stack(cols + [d["total_sqft"], d["bhk"], d["bath"], d["balcony"]])

        X, y = features(data), data["price"].values
        idx = np.random.default_rng(1).permutation(len(y))
        cut = int(0.8 * len(y))
        train, test = idx[:cut], idx[cut:]
        w, *_ = np.linalg.lstsq(X[train], y[train], rcond=None)
        pred = X[test] @ w
        r2 = 1 - ((y[test] - pred) ** 2).sum() / ((y[test] - y[test].mean()) ** 2).sum()
        mae = np.abs(y[test] - pred).mean()
        return data, top, locs, w, r2, mae

    data, top, locs, w, r2, mae = load_data_and_model(DATA_FILE)

    def predict(location, sqft, bhk, bath, balcony):
        loc = location if location in top else "Other"
        row = [1.0 if l == loc else 0.0 for l in locs] + [sqft, bhk, bath, balcony]
        return max(float(np.dot(w, row)), 10.0)

    def fmt(lakh):
        return f"₹ {lakh / 100:.2f} Crore" if lakh >= 100 else f"₹ {lakh:.1f} Lakh"

    section("📌 Dataset & Model")
    a, b, c, d = st.columns(4)
    stat(a, len(data), "Houses in Dataset")
    stat(b, int(data["location"].nunique()), "Locations")
    stat(c, f"{r2:.2f}", "Model R² Score")
    stat(d, f"₹{mae:.0f}L", "Avg Error (MAE)")

    section("🏡 Ghar ki details bharo")
    with st.container(border=True):
        l1, l2 = st.columns(2)
        location = l1.selectbox("Location", top + ["Other"], help="Top 15 areas; baaki sab 'Other' me aate hain.")
        sqft = l2.slider("Area (sq ft)", 400, 5000, 1200, 50)
        k1, k2, k3 = st.columns(3)
        bhk = k1.selectbox("BHK", [1, 2, 3, 4, 5, 6], index=1)
        bath = k2.selectbox("Bathrooms", [1, 2, 3, 4, 5], index=1)
        balcony = k3.selectbox("Balconies", [0, 1, 2, 3], index=1)
        go = st.button("💰 Price Predict Karo")

    if go:
        p = predict(location, sqft, bhk, bath, balcony)
        st.markdown(
            f'<div class="result"><small>Estimated Price • {location}</small><h2>{fmt(p)}</h2>'
            f'<small>≈ ₹ {p * 100000 / sqft:,.0f} per sq ft</small></div>',
            unsafe_allow_html=True,
        )
        st.balloons()

    tab1, tab2, tab3 = st.tabs(["📈 Area vs Price", "📍 Location Prices", "🗂 Dataset"])
    with tab1:
        areas = np.arange(400, 5050, 100)
        st.line_chart(pd.DataFrame({"Price (Lakh)": [predict(location, s, bhk, bath, balcony) for s in areas]}, index=areas), color=C1)
        st.caption("Selected location, BHK, bath aur balcony ke liye area badhne par price kaise badhti hai.")
    with tab2:
        pps = (data["price"] * 100000 / data["total_sqft"]).groupby(data["location"]).mean()
        st.bar_chart(pps[top].sort_values(ascending=False).round(0), color=C2)
        st.caption("Top 15 locations ka average price per sq ft (₹).")
    with tab3:
        st.dataframe(data.drop(columns="loc").head(100))
        st.caption("Source: Bengaluru House Price Data (public Kaggle dataset) • price Lakh ₹ me hai.")

    st.caption("Model: Linear Regression (80% train / 20% test) • Dataset sirf Bengaluru ka hai.")

st.markdown(f'<div class="footer">Made with ❤️ by <b>{DEVELOPER}</b> • Student Utility Hub</div>', unsafe_allow_html=True)
