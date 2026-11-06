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


## ادامهٔ ژورنال — D8، Merkle، بردار سه‌بعدی و CI

### چرخهٔ TDD
- تست‌های D8 و Merkle ابتدا اضافه شدند و در مرحلهٔ RED به‌دلیل نبود توابع مورد انتظار شکست خوردند.
- پس از پیاده‌سازی، تست‌های پایهٔ همان قابلیت‌ها سبز شدند.
- یک تست قانون بستگی D8 در برابری دقیق floatها حساس بود؛ معیار تست به مقایسهٔ عددی با تلورانس تبدیل شد، چون حاصل ضرب ماتریس‌های اعشاری ممکن است اختلافی در حد خطای ممیز شناور داشته باشد.
- یک نقص مهم در مدل اعتماد زنجیره کشف شد: بدون expected_head مورد اعتماد، دستکاری آخرین رویداد به‌تنهایی از زنجیره قابل تشخیص نیست. API به پارامتر expected_head مجهز شد و آزمون tamper برای آن اضافه شد.
- سپس Vec3 (جمع، تفریق، dot، cross، norm، normalization با رد بردار صفر)، شاخص‌های in-degree/out-degree و چگالی گراف جهت‌دار اضافه شدند.

### قراردادهای ریاضی/داده
- D8 در این پروژه به معنی گروه دیهدری هشت‌ضلعی با ۱۶ عضو است: ۸ دوران به مضارب π/4 و ۸ بازتاب.
- چگالی گراف جهت‌دار به‌صورت گراف ساده تعریف شد: یال‌های موازی یک زوج مرتب را یک‌بار می‌شمارند، self-loop در چگالی لحاظ نمی‌شود و برای کمتر از دو گره مقدار صفر دارد. درجهٔ ورودی/خروجی یال‌های موازی را جداگانه می‌شمارد.
- Merkle: برگ‌ها با 0x00 و والدها با 0x01 domain-separated می‌شوند؛ در سطح با تعداد فرد، آخرین هش تکرار می‌شود؛ درخت خالی ریشهٔ تعریف‌شده دارد. این قرارداد سادهٔ SSG است و ادعای سازگاری با RFC 6962 ندارد.
- expected_head باید در checkpoint مورد اعتماد یا سند امضاشده نگهداری شود؛ خود زنجیره مرجع اعتماد مستقل نیست.

### آزمون‌ها
در محیط محلی روی checkout بازسازی‌شده از محتوای خوانده‌شده از GitHub:
- `PYTHONPATH=src python -m unittest discover -s tests -v`: **19 tests, OK**.
- `python -m compileall -q src tests`: موفق، بدون خطا.
این نتایج مربوط به اجرای محلی‌اند؛ نتیجهٔ GitHub Actions تا زمان بررسی جداگانه، NOT RUN/PENDING باقی می‌ماند.

### فایل‌های جدید
- `tests/test_advanced.py`: آزمون D8 (تعداد اعضا، حفظ نرم، بستگی)، Merkle (اثبات عضویت، درخت فرد، دستکاری و ورودی نامعتبر)، checkpoint، Vec3 و metrics گراف.
- `assets/visual-shadow-atlas.svg`: پوستر برداری معماری؛ تصویر قابل مشاهده و قابل نسخه‌بندی، اما حامل lossless داده نیست.
- `.github/workflows/tests.yml`: اجرای خودکار compileall و unittest در Push/PR به main.
- `.gitignore`: نادیده‌گرفتن cache و build artifacts پایتون.

### Commitهای مرحلهٔ دوم
- D8 math: 1221eb6b7a252babd92c3e493319fef66d1077b0
- D8 byte/algorithm and Vec3: 8721ea12bd4bd7e9c71e69b8d32915966b75c6f6
- Merkle + anchored chain initial: 25247efd159f0f941a2488ecb357ff11e4da95c9
- Merkle domain-byte correction: 4ee1d6b87d8b6f9de4c8dbb7bc967b34475c773b
- Advanced tests: 504d858e11ab0b5b3d83f06c0f296eab0293f0c5
- Vec3/graph metrics tests: 08b3eb20de1711abd73dee1f0b2254dcfc3a7333
- Graph metrics: 8df9f88e0739d450ec39f3768624cae35c20fc30
- Visual Shadow SVG poster: 66dfcd0998adbdda38a17a12b0ac8a3710ded107
- Math foundations update: 4c2268d51d9a4f249e70b4b5b6ded20170cf12c1
- Merkle convention docs: 69a57ae28422230133da635f5d77d467db61646a
- Handoff update: f1e101275d101c8c0fcfc855c1ec5cb8ab8f3f68
- README update: 95fe8cb92581dc8d26ceeaf45fd22f60e5ee1da9
- GitHub Actions: 8153bcb69070365bdbd28c7b61d1bd18f4041e69
- gitignore: 7ed4608fc2ddf57f510de6833612d5672a1da0a8

### باقی‌مانده‌ها
- بررسی اجرای واقعی GitHub Actions.
- ساخت Merkle consistency proofs، نه فقط inclusion proofs.
- تکمیل matrix/vector API و ماتریس‌های 3D.
- Git ingestion واقعی و ساخت graph snapshot از repository.
- OCR و ارزیابی CER/WER برای فارسی و انگلیسی.
- lossless carrier با benchmark ظرفیت، خطا و مقاومت در برابر آسیب.
- آپلود PNG رستری قبلی هنوز انجام نشده؛ SVG برداری در مخزن موجود است.


## ادامهٔ ژورنال — Source Ingestion و Snapshot Hash

### هدف
تبدیل ساختار واقعی یک پوشهٔ پروژه به گرافی قابل ردیابی، بدون اجرای کدهای ورودی و بدون تغییر فایل‌های اصلی.

### قابلیت‌های افزوده‌شده
- آداپتور `ingest_directory` برای ساخت repository/directory/file nodes.
- یال‌های `contains` برای ساختار سلسله‌مراتبی.
- SHA-256 فایل‌ها با خواندن قطعه‌ای، بدون بارگذاری کامل فایل در حافظه.
- شناسهٔ پایدار بر مبنای namespace مخزن، نوع گره و مسیر نسبی.
- امکان تعیین `repository_id` برای جلوگیری از برخورد دو مخزن هم‌نام.
- URI قابل حمل از جنس `repo://...`.
- هش قطعی snapshot گراف با مرتب‌سازی گره‌ها و یال‌ها و JSON canonical.
- عدم دنبال‌کردن symlink، حذف `.git` و cacheهای رایج، تشخیص تغییر سادهٔ فایل هنگام هش‌کردن، سقف node و byte.
- CLI نمونه برای خروجی SVG و manifest؛ خروجی باید بیرون از source tree باشد.

### مرزبندی
این آداپتور snapshot از working tree می‌سازد؛ تاریخچهٔ commit، branch، tag، blame، diff، Git LFS object، parsing معنایی و OCR را نمی‌خواند. SVG صرفاً نمایش ساختار و manifest است؛ دادهٔ اصلی را داخل خود حمل نمی‌کند.

### TDD و آزمون
- تست namespace متفاوت ابتدا RED شد؛ API هنوز repository_id را نمی‌پذیرفت.
- پارامتر namespace به آداپتور افزوده و تست GREEN شد.
- اجرای محلی نهایی: **27 tests, OK**.
- compileall برای src، tests و examples موفق.
- Smoke test با پروژهٔ ساختگی: 5 nodes، 4 edges، 2 files، 2 directories؛ SVG و manifest تولید شدند.
- ورودی فقط خوانده شد؛ خروجی بیرون از درخت منبع نوشته شد.

### Commitهای این مرحله
- graph snapshot hashing: 9909ae20d9edf0e26eaf6e9c89f339390486e6c5
- source ingestion initial: 34c0755029ba7f151c1d9d0d4e2fdcb9d2baaebe
- ingestion tests: c7fb143082e31f5230c73f9f7988acb0b640fe05
- CLI example: 49595db9a284d5a87c68442ea2cec2216ea8a240
- stable ID separator corrections: 5547155ce4533f03481db5f9a8227b7bddf76447
- CLI newline correction: 0e91be83a74dff8819982349bf17c6fd76640c07
- explicit repository namespace: bde2059e1e66665f8d47fdd154b5e22eeb29737f
- CLI repository namespace: e97bcef8a756f224f4addeda51c1b864fb91cce6
- namespace test: 4976734e7e85ea6b38e4257cc36a5f277aa0c2b9
- CLI output guard: 82236a0bfd2b91f192eeae47f1923fe945755000
- source-ingestion specification: 35583bc710a7b3e084ed14514b7c808cb5a8035d

### گام‌های بعدی
1. Git metadata adapter برای commit/branch/tag/diff و انتساب revision دقیق.
2. Parserهای Markdown/code و chunk-level source locators.
3. OCR pipeline و benchmark فارسی/انگلیسی.
4. layout engine چندمقیاسی با collision/overflow metrics.
5. Merkle consistency proofs و امضای checkpoint.
6. تست CI از GitHub Actions و گزارش قابل مشاهدهٔ آخرین اجرا.


## ثبت کنترل نهایی این دور — 2026-11-06

### Commitهای مستندات و کنترل
- README با راهنمای اسکن محلی: 21387a6dacebef121fca36aece916c6b78dbbc02
- هنداف تکمیل‌شدهٔ ingestion: eb28a3c2504f02e21dba8b032ef9eadd6e1302a5
- ژورنال Source Ingestion: db9e45e906b116d6342728d6eda90999f687dcd2
- خروجی‌گیری بیرون از source tree: 82236a0bfd2b91f192eeae47f1923fe945755000
- سند Source Ingestion: 35583bc710a7b3e084ed14514b7c808cb5a8035d

### کنترل نهایی مخزن
فایل‌های mathcore، graph، provenance، ingestion، دو مجموعه تست، CLI نمونه، سند source ingestion، ژورنال، هنداف، پوستر SVG، workflow و README دوباره از GitHub خوانده شدند. پاسخ fetch برای همهٔ این مسیرها موفق بود.
Commit status query برای commit ژورنال، status entry برنگرداند؛ بنابراین وضعیت GitHub Actions هنوز **NOT VERIFIED** است و نباید PASS اعلام شود.

### وضعیت آزمون محلی
- 27 تست: PASS در اجرای محلی.
- compileall روی src/tests/examples: PASS.
- نمونهٔ اسکن پروژهٔ ساختگی: PASS، 5 node / 4 edge / 2 file / 2 directory و تولید SVG/manifest.
- GitHub Actions: NOT VERIFIED.
- Git history ingestion، OCR، Merkle consistency proof، lossless visual carrier: NOT IMPLEMENTED.


## ادامهٔ ژورنال — Git History Adapter | 2026-11-06

### دامنه
افزودن آداپتور مستقل و فقط‌خواندنی برای تاریخچهٔ Git به SSG، بدون ادغام آن با اسکنر working-tree و بدون اجرای کد مخزن ورودی.

### چرخهٔ تست
- ابتدا tests/test_git_ingest.py با چهار سناریو ثبت شد: commit/branch/tag/parent، محدودیت تعداد commit، مسیر غیرمخزن و مخزن خالی.
- اجرای CI روی commit تستی به حالت failure رسید؛ این RED مورد انتظار پیش از وجود ماژول بود.
- سپس src/ssg/git_ingest.py پیاده‌سازی و commit شد؛ CI جدید برای آن در وضعیت queued مشاهده شد.
- تا مشاهدهٔ نتیجهٔ اجرای جدید، تست‌ها PASS محسوب نمی‌شوند.

### طراحی پیاده‌سازی
- فرمان‌های Git با آرایهٔ argv و بدون shell اجرا می‌شوند.
- ورودی باید ریشهٔ working tree باشد؛ symlink root رد می‌شود.
- promptهای تعاملی، system/global config و optional lockها غیرفعال‌اند.
- هر فرمان timeout مستقل دارد.
- سقف commit با دریافت یک رکورد اضافه کنترل می‌شود؛ عبور از سقف به خطا منجر می‌شود و گراف ناقص برنمی‌گردد.
- commitها، parent edgeها، branchها و tagهای محلی به گراف تبدیل می‌شوند.
- والدهای shallow/unavailable به شکل boundary node ثبت می‌شوند.
- checkout، اجرای hook یا source code، خواندن blobها و تغییر مخزن انجام نمی‌شود.

### فایل‌ها و commitها
- tests/test_git_ingest.py — 1b9dcbea8162b330108f16554cfa86cae8b4fe3e (RED test commit)
- src/ssg/git_ingest.py — a3cf3d315e77e7d7322c929e20fd5fa522033150 (implementation commit)
- مستندات README، source ingestion، handoff و roadmap در همین دور تکمیل شدند.

### وضعیت
- تست‌نویسی قبل از پیاده‌سازی: PASS (ترتیب commitها قابل مشاهده است).
- پیاده‌سازی آداپتور: COMMITTED.
- اجرای CI پیاده‌سازی: PENDING در زمان ثبت این گزارش.
- اجرای محلی در این محیط: NOT RUN.
- remote refs، diff/tree/blob، blame، LFS، parser معنایی و OCR: NOT IMPLEMENTED.
