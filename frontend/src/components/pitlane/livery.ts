import type { EditorTheme } from "../CodeEditor";

export const MONO = "'JetBrains Mono', ui-monospace, monospace";

export const pitLaneTheme: EditorTheme = {
  name: "pit-lane",
  data: {
    base: "vs-dark",
    inherit: true,
    rules: [
      { token: "comment", foreground: "5f6570", fontStyle: "italic" },
      { token: "keyword", foreground: "ff6b74" },
      { token: "string", foreground: "7ee2a0" },
      { token: "number", foreground: "ffd60a" },
      { token: "type", foreground: "3aa0ff" },
      { token: "delimiter", foreground: "9ba1ac" },
      { token: "operator", foreground: "9ba1ac" },
      { token: "identifier", foreground: "e6e8ec" },
    ],
    colors: {
      "editor.background": "#0c0e11",
      "editor.foreground": "#e6e8ec",
      "editor.lineHighlightBackground": "#14171c",
      "editor.lineHighlightBorder": "#00000000",
      "editor.selectionBackground": "#ff263333",
      "editor.inactiveSelectionBackground": "#ff26331a",
      "editorCursor.foreground": "#ff2633",
      "editorLineNumber.foreground": "#3a3f49",
      "editorLineNumber.activeForeground": "#ff4b55",
      "editorIndentGuide.background1": "#1c2027",
      "editorIndentGuide.activeBackground1": "#353a45",
      "editorBracketMatch.background": "#ff263320",
      "editorBracketMatch.border": "#ff263360",
      "editorWidget.background": "#121419",
      "editorWidget.border": "#23272f",
      "editorSuggestWidget.background": "#121419",
      "editorSuggestWidget.border": "#23272f",
      "editorSuggestWidget.selectedBackground": "#20242c",
      "editorHoverWidget.background": "#121419",
      "editorHoverWidget.border": "#23272f",
      "scrollbar.shadow": "#00000000",
      "scrollbarSlider.background": "#353a4560",
      "scrollbarSlider.hoverBackground": "#5f657080",
      "scrollbarSlider.activeBackground": "#ff263380",
    },
  },
};

export function driverCode(name: string) {
  const letters = name.replace(/[^\p{L}\p{N}]/gu, "");
  return (letters || name).slice(0, 3).toUpperCase();
}

const LIVERIES = [
  "#3671c6",
  "#27f4d2",
  "#ff8000",
  "#229971",
  "#ff87bc",
  "#64c4ff",
  "#b6babd",
  "#52e252",
  "#ffd60a",
  "#b65cff",
  "#ff5e3a",
  "#6692ff",
];

export function livery(name: string) {
  let hash = 7;
  for (const character of name)
    hash = (hash * 33) ^ (character.codePointAt(0) ?? 0);
  return LIVERIES[Math.abs(hash) % LIVERIES.length];
}

export const difficultyTone = {
  Easy: "bg-sector-green text-carbon",
  Medium: "bg-sector-yellow text-carbon",
  Hard: "bg-signal text-white",
} as const;
