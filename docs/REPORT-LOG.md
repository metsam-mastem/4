# گزارش کار — ژورنال و تاریخچهٔ SSG

این سند مکمل سند تحویل است: روایت شکل‌گیری، تصمیم‌ها، فرضیه‌ها، تجربه‌ها، محدودیت‌ها و راهنمای توسعه‌دهندهٔ بعدی. هر تغییر مهم باید با تاریخ، انگیزه، فایل‌های تغییرکرده، آزمون و ریسک به انتهای آن افزوده شود.

## شناسنامه
پروژه: SSG — Symbolic Systems Grammar (نام کاری)
نسخهٔ مستندات: 0.4.0-draft
تاریخ: 2026-11-06
مخزن: https://github.com/metsam-mastem/4

## روایت شکل‌گیری

### ایدهٔ نمادین
رشتهٔ اولیهٔ طراحی‌شده توسط کاربر:
§|[{}]+=|[•×•]|=+[{}]|§
دو موجودیت مستقل در [•×•] تعامل می‌کنند؛ تبادل اطلاعات، تغییر وضعیت یا ایجاد ساختار جدید ممکن است. کلیدها متعدد و لایه‌ای هستند و ظاهر نمادها با کلید نمایش تغییر می‌کند. چندبعدی بودن شامل ابعاد مستقل، چندمعنایی زمینه‌مند و ساختارهای تو‌در‌تو است. معنای += و =+ هنوز باز است و نباید حدس زده شود.

### توسعه به SSG 0.3.0
معماری مفهومی شامل Identity، Symbolic، Semantic، Key/Decoding، Fractal، Logic، Crypto، Knowledge و Runtime/Studio شد. تصمیم‌های کاربر: D4+D8+Adaptive؛ Graph-first + Tree views؛ Hybrid crypto.

### استعارهٔ سایه و Visual Shadow
کاربر مثال دست روی زمین و خط دور انگشتان را مطرح کرد: خط، خود دست نیست؛ سایه/رد آن است. این ایده به SOURCE → KNOWLEDGE GRAPH → VISUAL SHADOW → RECONSTRUCTION تبدیل شد. پیشنهاد شد ۴۰۰ صفحه یا یک مخزن Git در پوستر چندطیفی و چندمقیاسی نمایش داده شود. تصمیم مهندسی: سه حالت را جدا کنیم: پوستر معنایی lossy، اطلس تعاملی traceable، و حامل تصویری lossless. OCR به‌تنهایی بازیابی بایت‌به‌بایت را تضمین نمی‌کند.

### Shift register
شیفت رجیستر الهام‌بخش تبدیل/جابه‌جایی برگشت‌پذیر در چیدمان داده است، نه رمزنگاری. امنیت باید با استانداردهای معتبر تأمین شود.

### ریاضیات
بردار، ماتریس، تبدیل affine، گراف، مستطیل، مکعب‌مستطیل، D4/D8، فیبوناچی، π، اعداد اول، اعداد گنگ و نسبت‌های 1، √2، √3، √5، φ، 2 و 2√2 به مشخصات اضافه شدند. هر نسبت باید کاربرد، فرمول، دقت، تلورانس و آزمون داشته باشد.

### معماری ایران
مرور اولیهٔ منابع نشان داد نسبت واحدی برای تمام معماری ایران وجود ندارد. √2، √3، √5، هندسهٔ مربع، مدولار بودن، محور و تقارن در زمینه‌های مختلف بررسی شده‌اند. هر بنا باید جداگانه سنجیده شود؛ نسبت نزدیک به یک مقدار، قصد تاریخی را ثابت نمی‌کند.

### الهام از بلاک‌چین
ایدهٔ ریسمان مبدأ تا مقصد به provenance chain تبدیل شد: هش artifact، پیوند به هش قبلی، ثبت نسخه و تبدیل، Merkle proof و checkpoint امضاشده. تصمیم: Git + hash chain + Merkle proof کافی است؛ شبکهٔ عمومی و توکن بدون نیاز واقعی وارد نسخهٔ اول نمی‌شود.

## شاخص‌های دقت
Source traceability، identity stability، graph integrity، provenance completeness، lossless round-trip، visual mapping coverage، OCR CER/WER، layout overflow/collision، ratio deviation، reproducibility، decode success، tamper detection و resource budget.

## سابقهٔ مخزن
- 2026-11-06: مخزن metsam-mastem/4 در حساب متصل پیدا شد؛ عمومی، مجوز admin/push موجود، اندازهٔ صفر، branch search برای main خالی بود.
- 2026-11-06: README اولیه با commit c50aaf1fdc6d331d44011c547fc17c95e060c06a ایجاد شد.
- فایل‌های بعدی، آزمون‌ها و وضعیت commit باید از نتیجهٔ واقعی ابزار ثبت شوند.

## تجربه‌ها و محدودیت‌ها
1. پوستر معمولی backup lossless نیست.
2. OCR خطا دارد و باید بر اساس زبان/نوع سند benchmark شود.
3. زیبایی را با صحت یا حقیقت یکی نگیریم.
4. عدد مشهور به‌تنهایی قانون طراحی نیست.
5. blockchain-inspired provenance جایگزین امضا و مدیریت کلید نیست.
6. هر transform باید lossless/lossy بودن را اعلام کند.
7. منبع اصلی هرگز با تصویر جایگزین نشود.

## راهنمای توسعه‌دهنده
پیش از تغییر، معماری و آزمون مرتبط را بخوان. برای هر الگوریتم تست مثبت، منفی و مرزی بنویس. هر گره باید provenance داشته باشد. تصویر باید legend و mapping داشته باشد. از کتابخانهٔ استاندارد برای crypto استفاده کن. ژورنال را پس از هر تغییر به‌روزرسانی کن. وضعیت‌ها را PASS/FAIL/NOT RUN/BLOCKED و مبتنی بر شواهد گزارش کن.

## وضعیت این مرحله
این ژورنال جمع‌بندی مکالمهٔ SSG در دسترس و پژوهش این مرحله است؛ ادعای دسترسی به تمام تاریخچهٔ حساب یا فایل‌های بیرون از این مکالمه ندارد. مدارک جدید باید جداگانه ثبت شوند.


## ثبت تحویل فنی — 2026-11-06

### تخصیص مخزن و ایجاد فایل‌ها
مخزن مقصد به‌صورت دقیق تأیید شد: metsam-mastem/4، عمومی، دسترسی admin و push موجود. اولین commit، README و سپس اسناد و اسکلت مرجع ایجاد شدند. فایل‌های افزوده‌شده:
- docs/00-project-charter.md
- docs/01-architecture.md
- docs/02-mathematical-foundations.md
- docs/03-proportion-engine.md
- docs/04-precision-kpis.md
- docs/05-visual-shadow-and-decoding.md
- docs/06-blockchain-inspired-provenance.md
- docs/07-iranian-geometry-research.md
- docs/08-handoff.md
- docs/09-roadmap-and-tests.md
- docs/REPORT-LOG.md
- src/ssg/__init__.py
- src/ssg/mathcore.py
- src/ssg/graph.py
- src/ssg/provenance.py
- src/ssg/visual.py
- tests/test_core.py
- assets/visual-shadow-poster-prompt.md
- schemas/manifest.example.json
- pyproject.toml

### تصمیم‌ها و فرمول‌های تثبیت‌شده
- نسبت مستطیل با بزرگ‌ترین ضلع تقسیم بر کوچک‌ترین ضلع تعریف شد.
- خانواده‌های 1، √2، √3، √5، φ، 2 و 2√2 مستند شدند.
- فرمول‌های مستطیل و مکعب‌مستطیل، بردار، ضرب داخلی، نرم، تبدیل دورانی، گراف و خطای نسبی ثبت شدند.
- D4 به‌صورت گروه ۸ عضوی تقارن مربع و D8 در این پروژه به‌صورت گروه ۱۶ عضوی تقارن هشت‌ضلعی تعریف شد؛ این قرارداد باید ثابت بماند.
- فیبوناچی برای شبکه و مقیاس‌بندی اختیاری، π برای هندسهٔ شعاعی، و اعداد اول برای توزیع/شاخص‌گذاری غیرامنیتی در نظر گرفته شدند.
- اعداد گنگ در قالب عبارت دقیق و مقدار تقریبی همراه با precision نگهداری می‌شوند.

### پیاده‌سازی مرجع
اسکلت Python شامل Vec2، Rect، Cuboid، نسبت‌ها، Fibonacci، D4 orbit، KnowledgeGraph، اعتبارسنجی endpointها، hash-chain provenance و SVG renderer ایجاد شد. این یک هستهٔ مرجع کوچک است، نه محصول کامل.

### آزمون و شواهد
فایل آزمون نوشته شد، اما در این مرحله در runtime پروژه اجرا نشده است: وضعیت آزمون‌ها NOT RUN. وجود فایل تست به‌معنای PASS نیست. اجرای بعدی باید با Python 3.11+ و دستور درج‌شده در راهنمای تحویل انجام شود.

### تصویر و دارایی‌های باینری
پوستر مفهومی در مکالمه تولید شده و فایل محلی آن با نام a_futuristic_cyber_mystical_infographic_poster_wi.png در محیط کاری موجود است. GitHub connector مورد استفاده برای ایجاد فایل، مسیر UTF-8 text را فراهم می‌کند و آپلود مستقیم این فایل باینری 3.2MB از مسیر فعلی تأیید نشده است. بنابراین فعلاً prompt بازتولید پوستر در assets ثبت شده؛ فایل PNG هنوز در مخزن commit نشده است. این مورد BLOCKED/PENDING است، نه PASS.

### محدودیت دامنهٔ کاوش
این ژورنال تمام نکات SSG موجود در مکالمهٔ جاری و خلاصهٔ زمینهٔ قبلی SSG را تجمیع می‌کند؛ به معنی دسترسی کامل به همهٔ گفتگوهای حساب، فایل‌های خارج از این زمینه یا مخازن دیگر نیست. هر منبع جدید باید جداگانه بازیابی و به ژورنال افزوده شود.

### گام‌های بعدی
1. اجرای تست‌ها و ثبت خروجی واقعی.
2. بازبینی code quality و edge cases.
3. افزودن D8 transformations و tests.
4. پیاده‌سازی Merkle tree واقعی با test vectors.
5. Git ingestion adapter و source locator.
6. تولید SVG poster از graph واقعی و ثبت node-to-source mapping.
7. طراحی threat model و capacity benchmark قبل از visual lossless carrier.


## Commit ledger — 2026-11-06

The following GitHub operations returned commit SHAs:
- README initial: c50aaf1fdc6d331d44011c547fc17c95e060c06a
- Project charter: a72885fc27dbf1efa8b622514216376b79d8db57
- Architecture: 4386097051ecaf7a15bd4d99e7440b5ea653ad8c
- Mathematical foundations: c244f0b2f37d93d76bdd0c061b458d2385af2dea
- Proportion engine: c1aa9d06baaa6e16fcb6961558f8a4ac190b73b8
- Precision KPIs: 92857f71009b01634f4eab7d7744959278d0cbac
- Visual Shadow: b9fea2404f2ef98aaadde5bc7ee40d0ab61e50c5
- Blockchain provenance: ae0b5b755af355ff3c97e9f6c59a1f71d2dfe84e
- Iranian geometry research first write: 7567786d6ce9015dbfb991abbff045567549aed4
- Handoff: c98515b44e96f79c6bb251ddfbc6d15275e0216f
- Report journal first write: e7692e2a7b2381d238874609a27df210d37208b7
- Python package init: ea52bcec21f1af32cd02dc248464386a9df8087c
- Math core: 1b280db7ac3fefc03a7dd6fa02ab6320f8599b57
- Graph core: a5c364ccc5070dbaaac8eff3c3b06f60ff3191bb
- Provenance core: 59a6b4326a635d79133f9fdd1f5c7a648fdc16e3
- SVG renderer: 243acc37ffe05af430af022563e7da5fc2b7e949
- Unit tests authored: 99108cc3c499859a49dd0f6a10881dc7914f04c8
- Roadmap: 0aad67d2e2128e836613fd2aaa281af31e20b888
- Poster prompt: ff2207aaaf70e283a24bc757c50e441bca69419c
- Example manifest: 86d7b3283d1e63a0485ff205d879934e3d580d7f
- Python project metadata: efb25e9460054648faee0d8a5b60e5aa1a8e92a6
- Research URL correction: 95b77ad96fa47946b9407f14802cfaaa5f02716c
- Delivery journal update: 5797b65bdc198d3991b86cc8857e1c849088b20c

A later fetch verified README, REPORT-LOG, and mathcore files are readable from the GitHub repository. The container could not clone GitHub because DNS/network access was unavailable; therefore tests were not run against the committed checkout. This remains NOT RUN/BLOCKED, not PASS.
