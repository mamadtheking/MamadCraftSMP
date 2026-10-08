<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Mamad Craft SMP</title>

<style>
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{
font-family:Tahoma,Arial,sans-serif;
background:#020805;
color:#fff;
overflow-x:hidden;
}

/* BACKGROUND */
body:before{
content:"";
position:fixed;
inset:0;
z-index:-5;
background:
radial-gradient(circle at 20% 20%,#0c5b2b33,transparent 30%),
radial-gradient(circle at 80% 70%,#00ff8830,transparent 30%),
linear-gradient(135deg,#010503,#03150b 50%,#010503);
}

.grid{
position:fixed;
inset:0;
z-index:-4;
background-image:
linear-gradient(#00ff8810 1px,transparent 1px),
linear-gradient(90deg,#00ff8810 1px,transparent 1px);
background-size:55px 55px;
animation:gridMove 12s linear infinite;
}
@keyframes gridMove{
to{background-position:55px 55px}
}

/* PARTICLES */
.particles{position:fixed;inset:0;pointer-events:none;z-index:-2}
.particle{
position:absolute;
width:4px;height:4px;
background:#43ff91;
border-radius:50%;
box-shadow:0 0 12px #43ff91;
animation:float 7s linear infinite;
opacity:.7;
}
@keyframes float{
0%{transform:translateY(110vh) scale(.3);opacity:0}
15%{opacity:.8}
85%{opacity:.8}
100%{transform:translateY(-10vh) scale(1.4);opacity:0}
}

/* HEADER */
header{
position:sticky;
top:0;
z-index:20;
padding:18px 7%;
display:flex;
justify-content:space-between;
align-items:center;
background:#020805cc;
backdrop-filter:blur(15px);
border-bottom:1px solid #1cff7530;
box-shadow:0 0 35px #00ff8812;
}

.logo{
font-size:22px;
font-weight:900;
letter-spacing:1px;
color:#65ff9c;
text-shadow:0 0 18px #00ff77;
}

.logo span{color:white}

nav a{
color:#ddd;
text-decoration:none;
margin:0 10px;
font-size:14px;
transition:.3s;
}
nav a:hover{
color:#63ff9a;
text-shadow:0 0 15px #00ff77;
}

/* HERO */
.hero{
min-height:88vh;
display:flex;
align-items:center;
justify-content:center;
text-align:center;
padding:80px 20px;
position:relative;
}

.hero-content{
animation:heroIn 1.2s ease both;
}
@keyframes heroIn{
from{opacity:0;transform:translateY(45px) scale(.96)}
to{opacity:1;transform:none}
}

.crown{
font-size:75px;
display:inline-block;
filter:drop-shadow(0 0 20px #00ff77);
animation:crownFloat 2.5s ease-in-out infinite;
}
@keyframes crownFloat{
0%,100%{transform:translateY(0) rotate(-2deg)}
50%{transform:translateY(-15px) rotate(2deg)}
}

.hero h1{
font-size:clamp(45px,9vw,100px);
font-weight:1000;
margin:10px 0;
background:linear-gradient(90deg,#fff,#5cff98,#fff,#5cff98);
background-size:300%;
-webkit-background-clip:text;
color:transparent;
animation:titleFlow 5s linear infinite;
}
@keyframes titleFlow{
to{background-position:300%}
}

.hero p{
color:#b8cfc1;
font-size:18px;
margin:15px auto 30px;
max-width:650px;
line-height:2;
}

.buttons{
display:flex;
gap:14px;
justify-content:center;
flex-wrap:wrap;
}

.btn{
display:inline-block;
padding:15px 28px;
border-radius:12px;
text-decoration:none;
font-weight:bold;
transition:.35s;
position:relative;
overflow:hidden;
}

.btn:before{
content:"";
position:absolute;
top:0;
left:-100%;
width:70%;
height:100%;
background:linear-gradient(90deg,transparent,#ffffff55,transparent);
transform:skewX(-25deg);
transition:.5s;
}
.btn:hover:before{left:130%}

.primary{
background:#19d86a;
color:#021108;
box-shadow:0 0 25px #00ff6655;
}
.primary:hover{
transform:translateY(-6px) scale(1.04);
box-shadow:0 0 45px #00ff88aa;
}

.secondary{
border:1px solid #37ff8a66;
background:#ffffff08;
color:white;
}
.secondary:hover{
transform:translateY(-6px);
background:#1aff7520;
border-color:#37ff8a;
}

/* STATUS */
.status{
padding:25px 7%;
}
.status-box{
max-width:1000px;
margin:auto;
padding:28px;
border:1px solid #31ff8240;
border-radius:22px;
background:linear-gradient(145deg,#ffffff08,#00ff8810);
box-shadow:0 20px 70px #0008,0 0 35px #00ff8810;
display:flex;
align-items:center;
justify-content:space-between;
gap:20px;
flex-wrap:wrap;
transition:.4s;
}
.status-box:hover{
transform:translateY(-8px);
box-shadow:0 25px 80px #000,0 0 55px #00ff8825;
}

.status-title{
font-size:20px;
font-weight:bold;
}
.status-address{
color:#8ea89a;
font-size:13px;
margin-top:8px;
direction:ltr;
}

.offline{
display:flex;
align-items:center;
gap:10px;
color:#ff6262;
font-weight:bold;
}

.dot{
width:13px;
height:13px;
border-radius:50%;
background:#ff3d3d;
box-shadow:0 0 18px #ff3333;
animation:pulse 1.5s infinite;
}
@keyframes pulse{
50%{transform:scale(1.45);opacity:.5}
}

/* SECTIONS */
section{
padding:100px 7%;
}
.section-title{
text-align:center;
font-size:42px;
margin-bottom:55px;
}
.section-title span{
color:#55ff96;
text-shadow:0 0 20px #00ff66;
}

/* CARDS */
.cards{
max-width:1100px;
margin:auto;
display:grid;
grid-template-columns:repeat(auto-fit,minmax(230px,1fr));
gap:25px;
}

.card{
padding:32px 25px;
border-radius:20px;
border:1px solid #36ff8030;
background:linear-gradient(145deg,#ffffff08,#00ff8810);
text-align:center;
transition:.5s;
position:relative;
overflow:hidden;
}

.card:after{
content:"";
position:absolute;
width:150px;
height:150px;
border-radius:50%;
background:#00ff6620;
filter:blur(45px);
top:-70px;
left:-70px;
transition:.5s;
}

.card:hover{
transform:translateY(-14px) rotateX(4deg);
border-color:#48ff91;
box-shadow:0 25px 60px #000,0 0 35px #00ff8830;
}
.card:hover:after{
transform:scale(2);
}

.icon{
font-size:50px;
margin-bottom:18px;
filter:drop-shadow(0 0 12px #00ff77);
}

.card h3{
font-size:21px;
margin-bottom:12px;
}
.card p{
color:#a8bbb0;
line-height:1.9;
font-size:14px;
}

/* BIG PANEL */
.panel{
max-width:1100px;
margin:auto;
padding:55px;
border-radius:30px;
background:
linear-gradient(135deg,#ffffff09,#00ff8810),
radial-gradient(circle at top,#00ff8820,transparent 45%);
border:1px solid #43ff9140;
box-shadow:0 30px 100px #000;
position:relative;
overflow:hidden;
}

.panel:before{
content:"";
position:absolute;
inset:-100%;
background:conic-gradient(transparent,#00ff7718,transparent 25%);
animation:spin 9s linear infinite;
}
@keyframes spin{to{transform:rotate(360deg)}}

.panel-content{
position:relative;
z-index:2;
text-align:center;
}

.panel h2{
font-size:35px;
margin-bottom:20px;
}
.panel p{
color:#abc0b2;
line-height:2;
max-width:700px;
margin:auto;
}

/* RULES */
.rules{
max-width:850px;
margin:auto;
display:grid;
gap:15px;
}
.rule{
padding:20px;
border-radius:14px;
background:#ffffff07;
border:1px solid #ffffff12;
transition:.35s;
}
.rule:hover{
transform:translateX(-10px);
border-color:#38ff8a55;
background:#00ff8810;
}
.rule b{color:#55ff96}

/* FOOTER */
footer{
padding:50px 20px;
text-align:center;
border-top:1px solid #ffffff12;
color:#718277;
}
footer strong{
color:#55ff96;
}

/* SCROLL REVEAL */
.reveal{
opacity:0;
transform:translateY(50px);
transition:1s ease;
}
.reveal.show{
opacity:1;
transform:none;
}

/* MOBILE */
@media(max-width:650px){
header{padding:15px 20px}
nav{display:none}
.hero{min-height:80vh}
.hero h1{font-size:48px}
.hero p{font-size:15px}
section{padding:75px 20px}
.section-title{font-size:32px}
.panel{padding:30px 20px}
.status-box{padding:22px}
}
</style>
</head>

<body>

<div class="grid"></div>

<div class="particles">
<div class="particle" style="left:5%;animation-delay:0s"></div>
<div class="particle" style="left:13%;animation-delay:2s"></div>
<div class="particle" style="left:21%;animation-delay:4s"></div>
<div class="particle" style="left:32%;animation-delay:1s"></div>
<div class="particle" style="left:43%;animation-delay:5s"></div>
<div class="particle" style="left:55%;animation-delay:3s"></div>
<div class="particle" style="left:66%;animation-delay:6s"></div>
<div class="particle" style="left:74%;animation-delay:2s"></div>
<div class="particle" style="left:84%;animation-delay:4s"></div>
<div class="particle" style="left:94%;animation-delay:1s"></div>
</div>

<header>
<div class="logo">👑 <span>Mamad Craft</span> SMP</div>
<nav>
<a href="#home">خانه</a>
<a href="#features">ویژگی‌ها</a>
<a href="#rules">قوانین</a>
<a href="#join">ورود</a>
</nav>
</header>

<main>

<section class="hero" id="home">
<div class="hero-content">

<div class="crown">👑</div>

<h1>Mamad Craft SMP</h1>

<p>
به سرور مامد کرفت خوش اومدی!
<br>
یک دنیای Minecraft برای بازی، ساخت‌وساز و کلی ماجراجویی با رفقا.
</p>

<div class="buttons">
<a class="btn primary" href="#join">🚀 ورود به سرور</a>
<a class="btn secondary" href="#features">✨ امکانات</a>
</div>

</div>
</section>

<section class="status reveal">
<div class="status-box">

<div>
<div class="status-title">وضعیت سرور</div>
<div class="status-address">mamadcraftsmp.aternos.me</div>
</div>

<div class="offline">
<span class="dot"></span>
<span>وضعیت آنلاین در این نسخه غیرفعال است</span>
</div>

</div>
</section>

<section id="features" class="reveal">

<h2 class="section-title">ویژگی‌های <span>Mamad Craft</span></h2>

<div class="cards">

<div class="card">
<div class="icon">⛏️</div>
<h3>Survival</h3>
<p>
دنیای بقا، ساخت‌وساز، استخراج و ماجراجویی با دوستان.
</p>
</div>

<div class="card">
<div class="icon">🌎</div>
<h3>دنیای بزرگ</h3>
<p>
یک دنیای بزرگ برای کشف کردن، ساختن و پیدا کردن مکان‌های جدید.
</p>
</div>

<div class="card">
<div class="icon">⚔️</div>
<h3>ماجراجویی</h3>
<p>
با دوستانت بازی کن، رقابت کن و لحظه‌های خفن بساز.
</p>
</div>

<div class="card">
<div class="icon">👑</div>
<h3>جامعه دوستانه</h3>
<p>
سروری برای دورهمی و بازی کردن کنار رفقا.
</p>
</div>

</div>
</section>

<section class="reveal">

<div class="panel">
<div class="panel-content">

<h2>🔥 آماده‌ای وارد دنیای Mamad Craft بشی؟</h2>

<p>
ساخت‌وساز شروع میشه، ماجراجویی منتظرته و کلی اتفاق خفن قراره بیفته.
</p>

</div>
</div>

</section>

<section id="rules" class="reveal">

<h2 class="section-title">📜 <span>قوانین سرور</span></h2>

<div class="rules">

<div class="rule">
<b>01</b> — احترام به بازیکنان الزامی است.
</div>

<div class="rule">
<b>02</b> — استفاده از تقلب و هک ممنوع است.
</div>

<div class="rule">
<b>03</b> — خرابکاری در ساخت‌وساز دیگران ممنوع است.
</div>

<div class="rule">
<b>04</b> — اسپم و تبلیغات بدون اجازه ممنوع است.
</div>

<div class="rule">
<b>05</b> — برای لذت بردن همه، قوانین را رعایت کنید. ❤️
</div>

</div>
</section>

<section id="join" class="reveal">

<div class="panel">
<div class="panel-content">

<h2>🚀 ورود به Mamad Craft SMP</h2>

<p style="margin-bottom:25px">
آدرس سرور را در Minecraft وارد کن:
</p>

<div class="btn secondary" style="direction:ltr">
mamadcraftsmp.aternos.me
</div>

<br><br>

<a
class="btn primary"
href="https://rubika.ir/joinc/FGABAJCA0DAKVOBPRVBXOMADGYOKACZG"
target="_blank">
💬 ورود به روبیکا
</a>

</div>
</div>

</section>

</main>

<footer>
<strong>👑 Mamad Craft SMP</strong>
<br><br>
ساخته شده برای گیمرها ❤️
</footer>

<script>
const reveals=document.querySelectorAll(".reveal");

const observer=new IntersectionObserver(entries=>{
entries.forEach(entry=>{
if(entry.isIntersecting){
entry.target.classList.add("show");
}
});
},{
threshold:.12
});

reveals.forEach(el=>observer.observe(el));

/* Mouse glow */
document.addEventListener("mousemove",e=>{
document.body.style.setProperty("--mx",e.clientX+"px");
document.body.style.setProperty("--my",e.clientY+"px");
});
</script>

</body>
</html>
