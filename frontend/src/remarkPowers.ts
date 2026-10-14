import type { PhrasingContent, Root } from "mdast";
import { visit } from "unist-util-visit";

export function remarkPowers() {
  return (tree: Root) => {
    visit(tree, "text", (node, index, parent) => {
      if (index === undefined || !parent) return;
      const parts: PhrasingContent[] = [];
      let offset = 0;
      for (const match of node.value.matchAll(/\b10\^(\d+)\b/g)) {
        if (match.index > offset) {
          parts.push({ type: "text", value: node.value.slice(offset, match.index) });
        }
        const value = `10^{${match[1]}}`;
        parts.push({
          type: "inlineMath",
          value,
          data: {
            hName: "code",
            hProperties: { className: ["language-math", "math-inline"] },
            hChildren: [{ type: "text", value }],
          },
        });
        offset = match.index + match[0].length;
      }
      if (offset === 0) return;
      if (offset < node.value.length) {
        parts.push({ type: "text", value: node.value.slice(offset) });
      }
      parent.children.splice(index, 1, ...parts);
      return index + parts.length;
    });
  };
}
