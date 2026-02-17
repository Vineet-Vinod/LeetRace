/* Monaco editor wrapper + character counter */

let editor = null;
let onChangeCallback = null;
let onSubmitCallback = null;

function initEditor(containerId, starterCode, onChange) {
    onChangeCallback = onChange;

    require.config({
        paths: { vs: 'https://cdn.jsdelivr.net/npm/monaco-editor@0.45.0/min/vs' }
    });

    require(['vs/editor/editor.main'], function () {
        editor = monaco.editor.create(document.getElementById(containerId), {
            value: starterCode || '',
            language: 'python',
            theme: 'vs-dark',
            fontSize: 14,
            fontFamily: "'Cascadia Code', 'Fira Code', Consolas, monospace",
            minimap: { enabled: false },
            lineNumbers: 'on',
            scrollBeyondLastLine: false,
            automaticLayout: true,
            tabSize: 4,
            wordWrap: 'on',
            padding: { top: 10 },
        });

        editor.onDidChangeModelContent(() => {
            if (onChangeCallback) {
                onChangeCallback(getCode());
            }
        });

        editor.addAction({
            id: 'submit-code',
            label: 'Submit Code',
            keybindings: [monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter],
            run: () => { if (onSubmitCallback) onSubmitCallback(); },
        });

        // Trigger initial count
        if (onChangeCallback) onChangeCallback(getCode());
    });
}

function getCode() {
    return editor ? editor.getValue() : '';
}

function setEditorReadOnly(readOnly) {
    if (editor) editor.updateOptions({ readOnly });
}

function setEditorSubmitCallback(callback) {
    onSubmitCallback = callback;
}

function charCount(code) {
    return code.replace(/\s/g, '').length;
}
