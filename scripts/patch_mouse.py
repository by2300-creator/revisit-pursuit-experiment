from pathlib import Path
import hashlib,json
root=Path('site')
bundle=next((root/'assets').glob('index-*.js'))
s=bundle.read_text()
def rep(a,b):
 global s
 assert s.count(a)==1,a
 s=s.replace(a,b)
rep('function Oae({trial:e',Path(__file__).with_name('mouse-tracker.js').read_text()+'\nfunction Oae({trial:e')
rep('onComplete:g}){const v=A.useRef(null),[b,x]=A.useState("fixation")','onComplete:g}){const mouse=useStimulusMouse();const v=A.useRef(null),[b,x]=A.useState("fixation")')
rep('o?.(ce,P),s?.(ce,P)','if(o) {if(ce.phase!=="response")ce.mouse=mouse.sample(P,ce.wallTime);o(ce,P)}s?.(ce,P)')
rep('[e,t,n,i,u,g,d,s,o,l]','[e,t,n,i,u,g,d,s,o,l,mouse.sample]')
rep('"data-training-feedback":!!p,','onPointerEnter:o?mouse.observe:undefined,onPointerMove:o?mouse.observe:undefined,onPointerUp:o?mouse.observe:undefined,onPointerLeave:o?mouse.forget:undefined,onPointerCancel:o?mouse.forget:undefined,"data-training-feedback":!!p,')
rep('onPointerDown:P=>{if(!h||_.length','onPointerDown:P=>{if(o)mouse.observe(P);if(!h||_.length')
rep('NB="pursuit-detailed-v3"','NB="pursuit-detailed-v4"')
rep('and keep this browser window open.', 'and keep this browser window open. During each moving-dot trial, the study records your mouse or trackpad cursor position over the dots, including during the starting fixation point. Use your cursor naturally.')
new=bundle.with_name('index-'+hashlib.sha256(s.encode()).hexdigest()[:12]+'.js');new.write_text(s)
idx=root/'index.html';idx.write_text(idx.read_text().replace(bundle.name,new.name));bundle.unlink()
cfg=root/'six-dot-motion/config.json';v=json.loads(cfg.read_text());v['studyMetadata']['version']='4.3.0';cfg.write_text(json.dumps(v,indent=2)+'\n')
