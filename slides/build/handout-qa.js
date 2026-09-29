// A4 안내문 렌더링 검사: 쪽 넘침, 상자 넘침, 작은 글자, 여백 이탈을 #qa에 기록한다.
(async () => {
  await document.fonts.ready;
  const out = [];
  const pages = [...document.querySelectorAll('.page')];
  const txt = (el) => el.textContent.trim().replace(/\s+/g, ' ').slice(0, 24);
  pages.forEach((p, i) => {
    const n = i + 1;
    if (p.scrollHeight > p.clientHeight + 1) out.push(`p${n} 쪽 넘침: ${p.scrollHeight - p.clientHeight}px`);
    p.querySelectorAll('.pr, td, th, .files > div, .bx, .flow .s').forEach((el) => {
      if (el.scrollHeight > el.clientHeight + 1 || el.scrollWidth > el.clientWidth + 1) {
        out.push(`p${n} 넘침: ${el.tagName.toLowerCase()}.${el.className} "${txt(el)}"`);
      }
    });
    const pr = p.getBoundingClientRect();
    const w = document.createTreeWalker(p, NodeFilter.SHOW_TEXT);
    let t;
    while ((t = w.nextNode())) {
      if (!t.textContent.trim()) continue;
      const el = t.parentElement;
      const r = document.createRange();
      r.selectNodeContents(t);
      const rr = r.getBoundingClientRect();
      if (rr.width === 0) continue;
      const fs = parseFloat(getComputedStyle(el).fontSize);
      const min = el.closest('.foot') ? 10.5 : 12;
      if (fs < min) out.push(`p${n} 작은 글자 ${fs}px: "${t.textContent.trim().slice(0, 20)}"`);
      if (rr.left < pr.left + 30 || rr.right > pr.right - 30 || rr.top < pr.top + 25 || rr.bottom > pr.bottom - 20) {
        out.push(`p${n} 여백 이탈: "${t.textContent.trim().slice(0, 20)}"`);
      }
    }
  });
  document.getElementById('qa').textContent = `QA pages=${pages.length}\n` + (out.length ? out.join('\n') : 'OK');
})();
