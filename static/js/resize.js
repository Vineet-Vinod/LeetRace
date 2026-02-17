/* Draggable resize handles for split panels */

(function () {
    const resizeV = document.getElementById('resize-v');
    const resizeH = document.getElementById('resize-h');
    const problemPanel = document.getElementById('problem-panel');
    const outputPanel = document.getElementById('output-panel');
    const editorContainer = document.getElementById('editor-container');

    let dragging = null; // 'v' or 'h'

    // --- Vertical resize (problem | editor) ---
    resizeV.addEventListener('mousedown', (e) => {
        e.preventDefault();
        dragging = 'v';
        resizeV.classList.add('active');
        document.body.style.cursor = 'col-resize';
        document.body.style.userSelect = 'none';
    });

    // --- Horizontal resize (editor | output) ---
    resizeH.addEventListener('mousedown', (e) => {
        e.preventDefault();
        dragging = 'h';
        resizeH.classList.add('active');
        document.body.style.cursor = 'row-resize';
        document.body.style.userSelect = 'none';
    });

    document.addEventListener('mousemove', (e) => {
        if (!dragging) return;

        if (dragging === 'v') {
            const layout = problemPanel.parentElement;
            const rect = layout.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const pct = (x / rect.width) * 100;
            const clamped = Math.max(15, Math.min(85, pct));
            problemPanel.style.width = clamped + '%';
        } else if (dragging === 'h') {
            const editorPanel = outputPanel.parentElement;
            const rect = editorPanel.getBoundingClientRect();
            const y = e.clientY - rect.top;
            const totalH = rect.height;
            const handleH = resizeH.offsetHeight;
            const outputH = totalH - y - handleH / 2;
            const clamped = Math.max(50, Math.min(totalH - 100, outputH));
            outputPanel.style.height = clamped + 'px';
        }
    });

    document.addEventListener('mouseup', () => {
        if (!dragging) return;
        if (dragging === 'v') resizeV.classList.remove('active');
        if (dragging === 'h') resizeH.classList.remove('active');
        dragging = null;
        document.body.style.cursor = '';
        document.body.style.userSelect = '';
    });
})();
