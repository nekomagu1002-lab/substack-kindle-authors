from pathlib import Path

source = Path('index.html').read_text(encoding='utf-8')

extra = '''
<style id="pdf-print-overrides">
@page { size: A4; margin: 9mm; }
@media print {
  html, body { background: #fff !important; color: #20262d !important; font-size: 10.5px !important; }
  .page { width: 100% !important; max-width: none !important; }
  .site-header { padding: 0 0 10px !important; margin-bottom: 10px !important; }
  .site-header h1 { font-size: 22px !important; margin-bottom: 5px !important; }
  .subtitle { font-size: 10px !important; }
  .stats { margin-top: 7px !important; font-size: 9px !important; gap: 5px 14px !important; }
  .stats strong { font-size: 12px !important; }
  .intro { margin: 8px 0 10px !important; font-size: 8.5px !important; }
  .controls, .reset, .back-top, .skip-link, .result-line, noscript { display: none !important; }
  .authors {
    display: grid !important;
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    gap: 5mm !important;
    align-items: start !important;
  }
  .author-card {
    display: block !important;
    break-inside: avoid !important;
    page-break-inside: avoid !important;
    margin: 0 !important;
    padding: 10px 11px !important;
    border: 1px solid #cfd6da !important;
    border-top: 2px solid #9ca8af !important;
    border-radius: 2px !important;
    box-shadow: none !important;
  }
  .card-meta { margin-bottom: 6px !important; gap: 5px !important; }
  .ku-badge { font-size: 7.5px !important; padding: 2px 5px !important; }
  .new-label { font-size: 7px !important; }
  .author-card h2 { font-size: 12px !important; line-height: 1.45 !important; margin: 0 0 3px !important; }
  .publication { font-size: 8.5px !important; line-height: 1.45 !important; }
  .author-name { margin: 6px 0 7px !important; font-size: 8px !important; line-height: 1.4 !important; }
  .author-name span { font-size: 6.8px !important; }
  .book-list { padding-top: 7px !important; margin-bottom: 7px !important; }
  .book-list h3 { font-size: 6.8px !important; margin-bottom: 4px !important; }
  .book + .book { margin-top: 6px !important; padding-top: 6px !important; }
  .book-title { font-size: 8.5px !important; line-height: 1.45 !important; margin-bottom: 4px !important; }
  .amazon-link, .substack-link {
    min-height: 0 !important;
    padding: 3px 6px !important;
    font-size: 7.5px !important;
    border-radius: 2px !important;
  }
  .card-bottom { gap: 5px !important; }
  .kind-label { font-size: 6.8px !important; }
  .site-footer { margin-top: 14px !important; padding: 10px 0 0 !important; font-size: 7.5px !important; }
}
</style>
'''

if '</head>' not in source:
    raise SystemExit('index.html: </head> not found')

Path('print.html').write_text(source.replace('</head>', extra + '\n</head>', 1), encoding='utf-8')
