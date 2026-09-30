// Windows/macOS 공통: NODE_PATH에 playwright 설치 위치를 지정해 실행한다.
// 예: node slides/build/build.cjs all (또는 part1, part2, handout)
const fs = require('fs');
const path = require('path');
const {pathToFileURL} = require('url');
const {chromium} = require('playwright');
const base=__dirname;
const names={part1:'../pdf/osung_ai_digital_problem_solving_part1_workspace_v24_20260930.pdf',part2:'../pdf/osung_ai_digital_problem_solving_part2_ux_implementation_v24_20260930.pdf',handout:'../../practice/osung_ai_digital_problem_solving_handout_a4_v24_20260930.pdf'};
const candidates=[process.env.CHROME_PATH,'C:/Program Files/Google/Chrome/Application/chrome.exe','C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe','/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','/usr/bin/google-chrome','/usr/bin/chromium'].filter(Boolean);
(async()=>{
 const executablePath=candidates.find(x=>fs.existsSync(x));
 const browser=await chromium.launch({headless:true,...(executablePath?{executablePath}:{})});
 try {
  const selected=process.argv[2]||'all';
  const parts=selected==='all'?Object.keys(names):[selected];
  for(const part of parts){
   if(!names[part]) throw new Error('Use all, part1, part2 or handout');
   const page=await browser.newPage({viewport:{width:1440,height:1000}});
   await page.emulateMedia({media:'print'});
   await page.goto(pathToFileURL(path.join(base,part+'.html')).href);
   await page.waitForFunction(()=>document.querySelector('#qa')?.textContent.includes('QA'));
   const qa=await page.locator('#qa').textContent();
   console.log(part+' '+qa);
   if(!qa.endsWith('\nOK')) throw new Error('Layout QA failed for '+part);
   const output=path.resolve(base,names[part]);
   fs.mkdirSync(path.dirname(output),{recursive:true});
   await page.pdf({path:output,preferCSSPageSize:true,printBackground:true,displayHeaderFooter:false});
   console.log(output);
   await page.close();
  }
 } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
