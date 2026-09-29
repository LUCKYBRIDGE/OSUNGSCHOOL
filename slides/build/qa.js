// 렌더링 자동 검사: 넘침, 작은 글자, 안전영역 이탈, 상자 겹침을 #qa에 기록한다.
(async () => {
  await document.fonts.ready;
  const out = [];
  const slides = [...document.querySelectorAll('.slide')];
  slides.forEach((s, i) => {
    const n = i + 1;
    const sr = s.getBoundingClientRect();
    const label = (el) => `${el.tagName.toLowerCase()}.${[...el.classList].join('.')} "${el.textContent.trim().replace(/\s+/g, ' ').slice(0, 28)}"`;
    // 1) 넘침
    s.querySelectorAll('.bd, .card, .step, .code, .bub, .take, .tree, td, th, .it, .back').forEach((el) => {
      if (el.scrollHeight > el.clientHeight + 1 || el.scrollWidth > el.clientWidth + 1) out.push(`p${n} 넘침: ${label(el)}`);
    });
    // 2) 글자 크기와 안전영역
    const walker = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
    let t;
    while ((t = walker.nextNode())) {
      if (!t.textContent.trim()) continue;
      const el = t.parentElement;
      const range = document.createRange();
      range.selectNodeContents(t);
      const rr = range.getBoundingClientRect();
      if (rr.width === 0) continue;
      // 최소 크기(DESIGN.md): 본문 20px, 참고 자료 목록 17px, 바닥글 14px, 목업 속 글자는 제외
      if (!el.closest('.mock')) {
        const fs = parseFloat(getComputedStyle(el).fontSize);
        const min = el.closest('.ft') ? 14 : el.closest('.refs') ? 17 : 20;
        if (fs < min) out.push(`p${n} 작은 글자 ${fs}px (기준 ${min}px): "${t.textContent.trim().slice(0, 24)}"`);
      }
      if (rr.left < sr.left + 40 || rr.right > sr.right - 40 || rr.top < sr.top + 16 || rr.bottom > sr.bottom - 12) {
        out.push(`p${n} 안전영역 이탈: "${t.textContent.trim().slice(0, 24)}"`);
      }
      // 본문 영역 밖으로 밀려난 글자(부모가 잘라 숨긴 경우)
      const bd = s.querySelector('.bd');
      if (bd && bd.contains(el)) {
        const br = bd.getBoundingClientRect();
        if (rr.bottom > br.bottom + 1 || rr.right > br.right + 1 || rr.top < br.top - 1) out.push(`p${n} 본문 영역 밖: "${t.textContent.trim().slice(0, 24)}"`);
      }
    }
    // 3) 형제 상자 겹침
    const boxes = [...s.querySelectorAll('.card, .step, .code, .bub, .take, .tree, table, .it, .chip, .back, .quote, .big')];
    for (let a = 0; a < boxes.length; a++) {
      for (let b = a + 1; b < boxes.length; b++) {
        const A = boxes[a], B = boxes[b];
        if (A.contains(B) || B.contains(A)) continue;
        const ra = A.getBoundingClientRect(), rb = B.getBoundingClientRect();
        const ix = Math.min(ra.right, rb.right) - Math.max(ra.left, rb.left);
        const iy = Math.min(ra.bottom, rb.bottom) - Math.max(ra.top, rb.top);
        if (ix > 1 && iy > 1) out.push(`p${n} 겹침: ${label(A)} / ${label(B)}`);
      }
    }
  });
  document.getElementById('qa').textContent = `QA slides=${slides.length}\n` + (out.length ? out.join('\n') : 'OK');
})();
