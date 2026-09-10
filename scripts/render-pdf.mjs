import { chromium } from 'playwright';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
await page.goto(pathToFileURL(path.resolve('print.html')).href, { waitUntil: 'load' });
await page.emulateMedia({ media: 'print' });
await page.pdf({
  path: 'substack-kindle-authors.pdf',
  format: 'A4',
  printBackground: true,
  preferCSSPageSize: true,
  displayHeaderFooter: true,
  headerTemplate: '<div></div>',
  footerTemplate: '<div style="font-size:7px;color:#666;width:100%;padding:0 9mm;text-align:right"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
  margin: { top: '9mm', right: '9mm', bottom: '12mm', left: '9mm' }
});
await browser.close();
