import { useEffect, useRef } from 'react';
import Editor from '@monaco-editor/react';
import { useGame } from '../context/GameContext';

const EMBER_THEME = {
  base: 'vs-dark',
  inherit: true,
  rules: [
    { token: 'keyword', foreground: 'f0a830', fontStyle: 'bold' },
    { token: 'string', foreground: 'e06050' },
    { token: 'number', foreground: 'c77dff' },
    { token: 'function', foreground: 'f0c060' },
    { token: 'comment', foreground: '605848', fontStyle: 'italic' },
    { token: 'variable', foreground: 'ede6d8' },
    { token: 'type', foreground: '8dd35f' },
    { token: 'delimiter', foreground: '9a9080' },
    { token: 'operator', foreground: 'e06050' },
  ],
  colors: {
    'editor.background': '#0d0b09',
    'editor.foreground': '#ede6d8',
    'editor.lineHighlightBackground': '#1a1713',
    'editor.selectionBackground': '#f0a83030',
    'editorCursor.foreground': '#f0a830',
    'editorLineNumber.foreground': '#605848',
    'editorLineNumber.activeForeground': '#9a9080',
    'editorIndentGuide.background': '#252119',
    'editorBracketMatch.background': '#f0a83020',
    'editorBracketMatch.border': '#f0a83050',
    'scrollbarSlider.background': '#2e2a2060',
    'editorSuggestWidget.background': '#1a1713',
    'editorHoverWidget.background': '#1a1713',
  },
};

export default function CodeEditor({ editorRef, onCharCount, onSubmit }) {
  const { starterCode, userCode, lockedIn, reviewMode, updateCode } = useGame();
  const monacoRef = useRef(null);
  const themeRegistered = useRef(false);

  function handleBeforeMount(monaco) {
    if (!themeRegistered.current) {
      monaco.editor.defineTheme('ember', EMBER_THEME);
      themeRegistered.current = true;
    }
  }

  function handleMount(editor, monaco) {
    monacoRef.current = editor;

    editorRef.current = () => editor.getValue();

    editor.onDidChangeModelContent(() => {
      const code = editor.getValue();
      onCharCount(code.length);
      updateCode(code);
    });

    editor.addAction({
      id: 'submit-code',
      label: 'Submit Code',
      keybindings: [monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter],
      run: () => onSubmit(),
    });

    onCharCount(editor.getValue().length);
  }

  useEffect(() => {
    if (monacoRef.current) {
      monacoRef.current.updateOptions({ readOnly: lockedIn || reviewMode });
    }
  }, [lockedIn, reviewMode]);

  // In review mode show the user's code; otherwise show starter code
  const editorValue = reviewMode ? userCode : starterCode;

  return (
    <div className="h-full border-l border-white/[0.06]">
      <Editor
        height="100%"
        language="python"
        theme="ember"
        value={editorValue}
        beforeMount={handleBeforeMount}
        onMount={handleMount}
        options={{
          fontSize: 14,
          fontFamily: "'JetBrains Mono', 'Cascadia Code', 'Fira Code', monospace",
          fontLigatures: true,
          tabSize: 4,
          wordWrap: 'on',
          minimap: { enabled: false },
          lineNumbers: 'on',
          scrollBeyondLastLine: false,
          automaticLayout: true,
          renderLineHighlight: 'line',
          cursorBlinking: 'smooth',
          cursorSmoothCaretAnimation: 'on',
          smoothScrolling: true,
          padding: { top: 12, bottom: 12 },
          bracketPairColorization: { enabled: true },
          suggest: { showIcons: true },
          scrollbar: {
            verticalScrollbarSize: 6,
            horizontalScrollbarSize: 6,
          },
          readOnly: lockedIn || reviewMode,
        }}
      />
    </div>
  );
}
