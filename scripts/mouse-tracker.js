// Keep mouse or trackpad position on the stimulus clock. Each recorded display
// frame carries its own sample, so it can be joined directly to its dot positions.
function useStimulusMouse() {
  const position = A.useRef(null);
  const forget = A.useCallback(() => { position.current = null; }, []);
  const observe = A.useCallback(event => {
    if (event.pointerType !== "mouse") return;
    position.current = {
      clientX: event.clientX,
      clientY: event.clientY,
      buttons: event.buttons,
      eventTime: performance.now()
    };
  }, []);
  A.useEffect(() => {
    const hidden = () => { if (document.hidden) forget(); };
    window.addEventListener("blur", forget);
    document.addEventListener("visibilitychange", hidden);
    return () => {
      window.removeEventListener("blur", forget);
      document.removeEventListener("visibilitychange", hidden);
      forget();
    };
  }, [forget]);
  const sample = A.useCallback((canvas, frameTime) => {
    const point = position.current;
    if (!point || document.hidden || !canvas.clientWidth || !canvas.clientHeight) return null;
    const rect = canvas.getBoundingClientRect();
    const x = (point.clientX - rect.left - canvas.clientLeft) * lt.width / canvas.clientWidth;
    const y = (point.clientY - rect.top - canvas.clientTop) * lt.height / canvas.clientHeight;
    if (x < 0 || x >= lt.width || y < 0 || y >= lt.height) return null;
    return {
      x, y, clientX: point.clientX, clientY: point.clientY,
      buttons: point.buttons, eventAgeMs: Math.max(0,frameTime-point.eventTime)
    };
  }, []);
  return {sample, observe, forget};
}
