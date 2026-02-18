import { useRef, useCallback } from 'react';
import Editor from '@monaco-editor/react';

const VELOCITY_THEME = {
  base: 'vs-dark',
  inherit: true,
  rules: [
    { token: 'comment', foreground: '4e506a', fontStyle: 'italic' },
    { token: 'keyword', foreground: '00e5c7' },
    { token: 'string', foreground: 'ff5a9d' },
    { token: 'number', foreground: 'a855f7' },
    { token: 'type', foreground: 'eab308' },
    { token: 'function', foreground: '00ffdd' },
    { token: 'variable', foreground: 'e4e6f0' },
    { token: 'operator', foreground: '8b8da3' },
    { token: 'delimiter', foreground: '8b8da3' },
    { token: 'identifier', foreground: 'e4e6f0' },
  ],
  colors: {
    'editor.background': '#0b0b16',
    'editor.foreground': '#e4e6f0',
    'editor.lineHighlightBackground': '#111122',
    'editor.selectionBackground': '#00e5c730',
    'editor.inactiveSelectionBackground': '#00e5c715',
    'editorCursor.foreground': '#00e5c7',
    'editorLineNumber.foreground': '#4e506a',
    'editorLineNumber.activeForeground': '#8b8da3',
    'editorIndentGuide.background': '#1e1e3a',
    'editorIndentGuide.activeBackground': '#2a2a50',
    'editorWhitespace.foreground': '#1e1e3a',
    'editor.wordHighlightBackground': '#00e5c715',
    'editorBracketMatch.background': '#00e5c720',
    'editorBracketMatch.border': '#00e5c750',
    'scrollbar.shadow': '#00000000',
    'scrollbarSlider.background': '#2a2a5060',
    'scrollbarSlider.hoverBackground': '#4e506a80',
    'scrollbarSlider.activeBackground': '#8b8da380',
    'editorOverviewRuler.border': '#00000000',
    'editorWidget.background': '#111122',
    'editorWidget.border': '#1e1e3a',
    'editorSuggestWidget.background': '#111122',
    'editorSuggestWidget.border': '#1e1e3a',
    'editorSuggestWidget.selectedBackground': '#191930',
    'editorHoverWidget.background': '#111122',
    'editorHoverWidget.border': '#1e1e3a',
  },
};

export default function CodeEditor({ value, onChange, readOnly = false, onSubmit }) {
  const editorRef = useRef(null);

  const handleMount = useCallback((editor, monaco) => {
    editorRef.current = editor;

    monaco.editor.defineTheme('velocity-terminal', VELOCITY_THEME);
    monaco.editor.setTheme('velocity-terminal');

    editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, () => {
      if (onSubmit) onSubmit();
    });

    editor.focus();
  }, [onSubmit]);

  return (
    <Editor
      language="python"
      value={value}
      onChange={(val) => onChange?.(val || '')}
      onMount={handleMount}
      theme="vs-dark"
      options={{
        readOnly,
        fontSize: 14,
        fontFamily: "'JetBrains Mono', 'Cascadia Code', 'Fira Code', monospace",
        fontLigatures: true,
        tabSize: 4,
        wordWrap: 'on',
        minimap: { enabled: false },
        lineNumbers: 'on',
        scrollBeyondLastLine: false,
        renderLineHighlight: 'line',
        cursorBlinking: 'smooth',
        cursorSmoothCaretAnimation: 'on',
        smoothScrolling: true,
        padding: { top: 12, bottom: 12 },
        overviewRulerBorder: false,
        hideCursorInOverviewRuler: true,
        scrollbar: {
          verticalScrollbarSize: 6,
          horizontalScrollbarSize: 6,
        },
        bracketPairColorization: { enabled: true },
        suggest: { showIcons: true },
      }}
      loading={
        <div className="flex items-center justify-center h-full bg-base">
          <div className="w-6 h-6 border-2 border-brd border-t-primary rounded-full animate-spin" />
        </div>
      }
    />
  );
}
