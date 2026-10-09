import { useEffect, useRef } from "react";
import Editor, { loader, type OnMount } from "@monaco-editor/react";
import * as monaco from "monaco-editor/esm/vs/editor/editor.api.js";
import "monaco-editor/esm/vs/basic-languages/python/python.contribution.js";
import EditorWorker from "monaco-editor/esm/vs/editor/editor.worker?worker";

self.MonacoEnvironment = {
  getWorker() {
    return new EditorWorker();
  },
};
loader.config({ monaco });

interface Props {
  value: string;
  onChange: (value: string) => void;
  readOnly: boolean;
  onSubmit: () => void;
}

export default function CodeEditor({
  value,
  onChange,
  readOnly,
  onSubmit,
}: Props) {
  const submit = useRef(onSubmit);
  const currentValue = useRef(value);
  currentValue.current = value;
  useEffect(() => {
    submit.current = onSubmit;
  }, [onSubmit]);

  const onMount: OnMount = (editor, instance) => {
    instance.editor.defineTheme("leetrace", {
      base: "vs-dark",
      inherit: true,
      rules: [
        { token: "comment", foreground: "4e506a", fontStyle: "italic" },
        { token: "keyword", foreground: "00e5c7" },
        { token: "string", foreground: "ff5a9d" },
        { token: "number", foreground: "a855f7" },
      ],
      colors: {
        "editor.background": "#0b0b16",
        "editor.foreground": "#e4e6f0",
        "editor.lineHighlightBackground": "#111122",
        "editor.selectionBackground": "#00e5c730",
        "editorCursor.foreground": "#00e5c7",
        "editorLineNumber.foreground": "#4e506a",
      },
    });
    instance.editor.setTheme("leetrace");
    editor.addCommand(instance.KeyMod.CtrlCmd | instance.KeyCode.Enter, () =>
      submit.current(),
    );
    editor.setValue(currentValue.current);
    editor.focus();
  };

  return (
    <Editor
      language="python"
      path="file:///solution.py"
      keepCurrentModel
      value={value}
      onChange={(value) => onChange(value ?? "")}
      onMount={onMount}
      options={{
        readOnly,
        fontSize: 14,
        fontFamily: "'JetBrains Mono', monospace",
        tabSize: 4,
        wordWrap: "on",
        // Monaco 0.55 leaves occurrence requests unhandled when editors close.
        occurrencesHighlight: "off",
        minimap: { enabled: false },
        scrollBeyondLastLine: false,
        automaticLayout: true,
        padding: { top: 12, bottom: 12 },
      }}
      loading={<p className="p-5 text-muted">Loading editor...</p>}
    />
  );
}
