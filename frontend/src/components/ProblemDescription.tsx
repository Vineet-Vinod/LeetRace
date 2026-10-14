import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import { remarkPowers } from "../remarkPowers.js";
import "katex/dist/katex.min.css";

export function ProblemDescription({ statement }: { statement: string }) {
  return (
    <article className="problem-description">
      <ReactMarkdown
        remarkPlugins={[remarkGfm, [remarkMath, { singleDollarTextMath: false }], remarkPowers]}
        rehypePlugins={[rehypeKatex]}
      >
        {statement}
      </ReactMarkdown>
    </article>
  );
}
