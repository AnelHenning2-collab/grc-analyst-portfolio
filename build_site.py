"""
Converts all portfolio .md files into styled HTML pages.
Run from the repo root: python build_site.py
"""
import re, os
import markdown as md_lib
from pathlib import Path

ROOT = Path(__file__).parent

PAGES = [
    ("acceptable-use-policy.md",        "Acceptable Use Policy",               "Health Insurance · HIPAA"),
    ("data-classification-policy.md",   "Data Classification Policy",          "Healthcare · Hospital System"),
    ("incident-response-policy.md",     "Incident Response Policy",            "Managed Care · Medicaid/CHIP"),
    ("nist-csf-gap-analysis.md",        "NIST CSF Gap Analysis",               "Federal Civilian Agency · FISMA"),
    ("compliance-framework-mapping.md", "Cross-Framework Compliance Mapping",  "Federal IT Contractor · FedRAMP"),
    ("security-awareness-training.md",  "Security Awareness Training",         "P&C Insurance · NAIC"),
    ("risk-register-README.md",         "Risk Register & Methodology",         "Federal Health Contractor · ATO"),
]

NAV_LINKS = [
    ("Home",              "index.html"),
    ("AUP",               "acceptable-use-policy.html"),
    ("Data Classification","data-classification-policy.html"),
    ("Incident Response", "incident-response-policy.html"),
    ("NIST CSF Analysis", "nist-csf-gap-analysis.html"),
    ("Framework Mapping", "compliance-framework-mapping.html"),
    ("Security Training", "security-awareness-training.html"),
    ("Risk Register",     "risk-register.html"),
]

INDUSTRY_COLORS = {
    "Health Insurance":          "#028090",
    "Healthcare":                "#076B72",
    "Managed Care":              "#175384",
    "Federal Civilian Agency":   "#4B348C",
    "Federal IT Contractor":     "#5B2186",
    "P&C Insurance":             "#92400E",
    "Federal Health Contractor": "#065A82",
}

def tag_color(industry_str):
    for key, col in INDUSTRY_COLORS.items():
        if key.lower() in industry_str.lower():
            return col
    return "#028090"

SHARED_CSS = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    /* 12pt = 16px; set on html so rem units resolve correctly */
    html { font-size: 16px; }

    :root {
      --navy:     #1E2761;
      --teal:     #028090;
      --green:    #04763A;
      --gold:     #F5C518;
      --ice:      #CADBFC;
      --light-bg: #EEF3FF;
      --dark-txt: #000000;
      --mid-gray: #000000;
      --white:    #FFFFFF;
      --border:   #DDE3F0;
    }
    body {
      font-family: 'Segoe UI', Calibri, sans-serif;
      color: var(--dark-txt);
      background: #F8FAFF;
      line-height: 1.75;
      font-size: 1rem;   /* 16px = 12pt */
    }
    a { color: var(--teal); text-decoration: none; }
    a:hover { text-decoration: underline; }

    /* NAV */
    nav {
      background: var(--navy);
      position: sticky; top: 0; z-index: 100;
      box-shadow: 0 2px 12px rgba(0,0,0,.25);
    }
    .nav-inner {
      max-width: 1200px; margin: 0 auto;
      display: flex; align-items: center; flex-wrap: wrap;
      padding: 0 24px;
    }
    .nav-brand {
      font-weight: 700; font-size: 1rem;
      color: var(--gold) !important;
      padding: 16px 20px 16px 0;
      white-space: nowrap;
      border-right: 1px solid rgba(255,255,255,.15);
      margin-right: 8px;
    }
    .nav-brand:hover { text-decoration: none !important; }
    .nav-links { display: flex; flex-wrap: wrap; gap: 2px; }
    .nav-links a {
      color: var(--ice) !important;
      font-size: 0.9rem; font-weight: 500;
      padding: 18px 12px;
      transition: color .15s, background .15s;
      white-space: nowrap;
    }
    .nav-links a:hover, .nav-links a.active {
      color: var(--white) !important;
      background: rgba(255,255,255,.08);
      text-decoration: none;
    }
    .nav-dl {
      margin-left: auto;
      background: var(--gold);
      color: var(--navy) !important;
      font-weight: 700; font-size: 0.875rem;
      padding: 9px 18px !important;
      border-radius: 4px;
      white-space: nowrap;
    }
    .nav-dl:hover { opacity: .85; background: var(--gold); text-decoration: none !important; }

    /* PAGE WRAPPER */
    .page-wrap { max-width: 900px; margin: 0 auto; padding: 48px 24px 80px; }

    /* PAGE HEADER */
    .page-header { margin-bottom: 36px; }
    .page-header .industry-tag {
      display: inline-block;
      font-size: 0.8rem; font-weight: 700;
      letter-spacing: 1px; text-transform: uppercase;
      padding: 5px 14px; border-radius: 999px;
      color: var(--white); margin-bottom: 14px;
    }
    .page-header h1 {
      font-size: clamp(1.6rem, 4vw, 2.3rem);
      font-weight: 700; color: var(--navy);
      line-height: 1.2; margin-bottom: 10px;
    }
    .page-header .subtitle {
      font-size: 1rem; color: var(--mid-gray);
      max-width: 680px;
    }

    /* CONTENT CARD */
    .content-card {
      background: var(--white);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 40px 44px;
      margin-bottom: 32px;
      box-shadow: 0 2px 12px rgba(0,0,0,.05);
    }

    /* MARKDOWN CONTENT STYLES — all body text at 1rem = 16px = 12pt */
    .md-content h1 { font-size: 1.6rem; color: var(--navy); margin: 0 0 20px; }
    .md-content h2 {
      font-size: 1.2rem; font-weight: 700;
      color: var(--navy); margin: 32px 0 14px;
      padding-bottom: 6px;
      border-bottom: 2px solid var(--light-bg);
    }
    .md-content h3 { font-size: 1.05rem; font-weight: 700; color: var(--teal); margin: 20px 0 8px; }
    .md-content h4 { font-size: 1rem; font-weight: 700; color: var(--dark-txt); margin: 16px 0 6px; }
    .md-content p  { margin-bottom: 14px; font-size: 1rem; color: var(--dark-txt); }
    .md-content ul, .md-content ol { margin: 10px 0 16px 26px; }
    .md-content li { margin-bottom: 6px; font-size: 1rem; color: var(--dark-txt); }
    .md-content strong { color: var(--dark-txt); }
    .md-content em { color: var(--dark-txt); font-style: italic; }
    .md-content code {
      background: var(--light-bg); border-radius: 3px;
      padding: 2px 6px; font-size: 0.9rem; font-family: Consolas, monospace;
    }
    .md-content pre {
      background: var(--light-bg); border-radius: 6px;
      padding: 16px; overflow-x: auto; margin-bottom: 16px;
    }
    .md-content pre code { background: none; padding: 0; font-size: 0.9rem; }
    .md-content blockquote {
      border-left: 4px solid var(--teal);
      background: var(--light-bg);
      padding: 12px 16px; margin: 16px 0;
      border-radius: 0 6px 6px 0;
      font-style: italic; color: var(--dark-txt);
    }
    .md-content hr { border: none; border-top: 1px solid var(--border); margin: 28px 0; }

    /* TABLES */
    .md-content table {
      width: 100%; border-collapse: collapse;
      margin: 16px 0 20px; font-size: 0.95rem;
      display: block; overflow-x: auto;
      -webkit-overflow-scrolling: touch;
    }
    .md-content th {
      background: var(--navy); color: var(--white);
      padding: 11px 14px; text-align: left; font-weight: 600;
    }
    .md-content td {
      padding: 10px 14px; border-bottom: 1px solid var(--border);
      color: var(--dark-txt);
    }
    .md-content tr:nth-child(even) td { background: var(--light-bg); }
    .md-content tr:hover td { background: #E4EDFF; }

    /* STAR SECTION */
    .star-section {
      background: linear-gradient(135deg, #0A1A50 0%, #1E2761 100%);
      border-radius: 10px;
      padding: 36px 40px;
      margin-bottom: 32px;
      color: var(--white);
    }
    .star-section .star-label {
      font-size: 0.8rem; font-weight: 700;
      letter-spacing: 2px; text-transform: uppercase;
      color: var(--gold); margin-bottom: 6px;
    }
    .star-section h2 {
      font-size: 1.3rem; color: var(--white);
      margin-bottom: 6px; border: none; padding: 0;
    }
    .star-meta {
      font-size: 0.95rem; color: var(--ice);
      font-style: italic; margin-bottom: 28px;
    }
    .star-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 20px;
    }
    .star-block {
      background: rgba(255,255,255,.07);
      border-radius: 8px; padding: 18px 20px;
    }
    .star-block .star-block-label {
      font-size: 0.8rem; font-weight: 700;
      text-transform: uppercase; letter-spacing: 1.5px;
      color: var(--teal); margin-bottom: 10px;
    }
    .star-block p, .star-block li {
      font-size: 1rem; color: #D0DEFF; line-height: 1.7;
    }
    .star-block ul { margin-left: 18px; }
    .star-block li { margin-bottom: 6px; }
    .star-win {
      background: var(--green);
      border-radius: 8px; padding: 20px 24px;
    }
    .star-win .win-label {
      font-size: 0.8rem; font-weight: 700;
      text-transform: uppercase; letter-spacing: 1.5px;
      color: var(--gold); margin-bottom: 10px;
    }
    .star-win .win-headline {
      font-size: 1.1rem; font-weight: 700;
      color: var(--white); margin-bottom: 8px;
    }
    .star-win .win-detail { font-size: 1rem; color: #B2E8D0; }

    /* BACK LINK */
    .back-link {
      display: inline-flex; align-items: center; gap: 6px;
      font-size: 1rem; font-weight: 600;
      color: var(--teal); margin-bottom: 28px;
    }
    .back-link:hover { text-decoration: none; opacity: .8; }

    /* FOOTER */
    footer {
      background: #1E273D; color: var(--ice);
      text-align: center; padding: 28px 20px;
      font-size: 0.9rem;
    }
    footer a { color: var(--gold); }

    /* ── MOBILE / IPHONE RESPONSIVE ── */
    @media (max-width: 768px) {
      /* Nav: scrolls horizontally, no wrapping chaos */
      .nav-inner { flex-wrap: nowrap; padding: 0 12px; overflow: hidden; }
      .nav-brand  { font-size: 0.85rem; padding: 14px 12px 14px 0; }
      .nav-links  {
        overflow-x: auto; -webkit-overflow-scrolling: touch;
        flex-wrap: nowrap; scrollbar-width: none;
      }
      .nav-links::-webkit-scrollbar { display: none; }
      .nav-links a { padding: 16px 9px; font-size: 0.78rem; }
      .nav-dl { font-size: 0.72rem; padding: 7px 10px !important; flex-shrink: 0; }

      /* Page layout */
      .page-wrap { padding: 28px 16px 56px; }
      .page-header h1 { font-size: 1.4rem; }
      .section-title  { font-size: 1.3rem; }
      .content-card   { padding: 20px 16px; }

      /* STAR blocks stack vertically */
      .star-section { padding: 24px 16px; }
      .star-grid    { grid-template-columns: 1fr; }
      .star-block   { padding: 14px 16px; }

      /* Tables: horizontal scroll on small screens */
      .md-content table { font-size: 0.82rem; }
      .md-content th, .md-content td { padding: 7px 10px; }
    }

    @media (max-width: 480px) {
      .page-header h1 { font-size: 1.25rem; }
      .content-card   { padding: 16px 12px; }
      .star-section   { padding: 18px 12px; }
    }
"""

NAV_HTML = """
<nav>
  <div class="nav-inner">
    <a class="nav-brand" href="index.html">Anél Henning · GRC Portfolio</a>
    <div class="nav-links">
      {links}
    </div>
    <a class="nav-links nav-dl" href="GRC_Analyst_Portfolio_Anel_Henning.pptx" download>⬇ Download Deck</a>
  </div>
</nav>
"""

FOOTER_HTML = """
<footer>
  <p>
    <strong style="color:#fff;">Anél Henning</strong> &nbsp;·&nbsp; GRC Analyst
    &nbsp;·&nbsp; <a href="mailto:logicalcoders@outlook.com">logicalcoders@outlook.com</a>
  </p>
  <p style="margin-top:8px;color:#111111;">
    NIST CSF 2.0 · NIST 800-53 Rev.5 · ISO 27001:2022 · SOC 2 TSC · HIPAA · NAIC · FedRAMP · FISMA
  </p>
</footer>
"""

def build_nav(active_href="index.html"):
    links = ""
    for label, href in NAV_LINKS:
        cls = ' class="active"' if href == active_href else ''
        links += f'<a href="{href}"{cls}>{label}</a>\n      '
    return NAV_HTML.format(links=links)

def split_star(raw_md):
    """Split markdown into (main_content, star_dict) where star_dict has S/T/A/R parts."""
    marker = "## Portfolio STAR Story"
    if marker not in raw_md:
        return raw_md, None

    main_part, star_part = raw_md.split(marker, 1)

    def extract(section_name, text):
        pattern = rf"### {section_name}\n(.*?)(?=\n### |\Z)"
        m = re.search(pattern, text, re.DOTALL)
        return m.group(1).strip() if m else ""

    # Extract industry/role line ("> **Industry:**...")
    industry_match = re.search(r"> \*\*Industry:\*\* (.+)", star_part)
    industry_line = industry_match.group(1).strip() if industry_match else ""

    s_raw = extract("Situation", star_part)
    t_raw = extract("Task", star_part)
    a_raw = extract("Action", star_part)
    r_raw = extract("Result", star_part)

    return main_part.strip(), {
        "industry": industry_line,
        "situation": s_raw,
        "task":      t_raw,
        "action":    a_raw,
        "result":    r_raw,
    }

def md_to_html(text):
    """Convert markdown to HTML with tables extension."""
    return md_lib.markdown(text, extensions=["tables", "fenced_code"])

def build_star_block(star):
    if not star:
        return ""

    # Convert action bullets (markdown list) to <ul>
    def md_mini(text):
        lines = text.strip().split("\n")
        if any(l.strip().startswith("-") for l in lines):
            items = [re.sub(r"^[-*]\s*", "", l).strip() for l in lines if l.strip()]
            return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
        return f"<p>{text.strip()}</p>"

    # Result: first line = headline, rest = detail
    result_lines = star["result"].strip().split("\n", 1)
    win_headline = result_lines[0].strip().lstrip("-*").strip()
    win_detail   = result_lines[1].strip() if len(result_lines) > 1 else ""

    return f"""
<div class="star-section">
  <div class="star-label">STAR Method · Real-World Scenario</div>
  <h2>Portfolio STAR Story</h2>
  <div class="star-meta">{star['industry']}</div>
  <div class="star-grid">
    <div class="star-block">
      <div class="star-block-label">Situation</div>
      <p>{star['situation']}</p>
    </div>
    <div class="star-block">
      <div class="star-block-label">Task</div>
      <p>{star['task']}</p>
    </div>
    <div class="star-block" style="grid-column: 1 / -1;">
      <div class="star-block-label">Actions I Took</div>
      {md_mini(star['action'])}
    </div>
  </div>
  <div class="star-win">
    <div class="win-label">🏆 The Win</div>
    <div class="win-headline">{win_headline}</div>
    <div class="win-detail">{win_detail}</div>
  </div>
</div>
"""

def build_page(md_file, title, industry, out_file, active_href):
    raw = (ROOT / md_file).read_text(encoding="utf-8")
    main_md, star = split_star(raw)

    # Remove the h1 from main content (we render it in page-header)
    main_md = re.sub(r"^# .+\n", "", main_md, count=1).strip()

    main_html  = md_to_html(main_md)
    star_html  = build_star_block(star)
    ind_color  = tag_color(industry)
    nav        = build_nav(active_href)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title} | Anél Henning GRC Portfolio</title>
  <style>{SHARED_CSS}</style>
</head>
<body>
{nav}
<div class="page-wrap">
  <a class="back-link" href="index.html">← Back to Portfolio</a>
  <div class="page-header">
    <span class="industry-tag" style="background:{ind_color};">{industry}</span>
    <h1>{title}</h1>
    <p class="subtitle">GRC work product · Includes full policy/framework and a STAR method scenario below.</p>
  </div>
  {star_html}
  <div class="content-card">
    <div class="md-content">
      {main_html}
    </div>
  </div>
</div>
{FOOTER_HTML}
</body>
</html>"""

    (ROOT / out_file).write_text(html, encoding="utf-8")
    print(f"  Built: {out_file}")

# ── Build all pages ────────────────────────────────────────────────────────
print("Building portfolio pages...")
output_map = {
    "acceptable-use-policy.md":        "acceptable-use-policy.html",
    "data-classification-policy.md":   "data-classification-policy.html",
    "incident-response-policy.md":     "incident-response-policy.html",
    "nist-csf-gap-analysis.md":        "nist-csf-gap-analysis.html",
    "compliance-framework-mapping.md": "compliance-framework-mapping.html",
    "security-awareness-training.md":  "security-awareness-training.html",
    "risk-register-README.md":         "risk-register.html",
}

for md_file, title, industry in PAGES:
    out_file = output_map[md_file]
    build_page(md_file, title, industry, out_file, out_file)

print("Done.")
