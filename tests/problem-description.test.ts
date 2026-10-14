import { readFileSync } from 'node:fs';
import { createElement } from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { describe, expect, it } from 'vitest';
import { problemSchema } from '../server/problems.js';
import { ProblemDescription } from '../frontend/src/components/ProblemDescription.js';

function render(statement: string) {
  return renderToStaticMarkup(createElement(ProblemDescription, { statement }));
}

describe('problem description rendering', () => {
  it('renders High Five indices and exponents while keeping explanations outside example snippets', () => {
    const data: unknown = JSON.parse(readFileSync('problems/high-five.json', 'utf8'));
    const html = render(problemSchema.parse(data).statement);
    expect(html).toContain('<code>items[i]</code>');
    expect(html).toContain('<msub>');
    expect(html).toContain('<msup>');
    expect(html).not.toContain('katex-error');
    const snippets = [...html.matchAll(/<pre>([\s\S]*?)<\/pre>/g)];
    expect(snippets).toHaveLength(2);
    for (const snippet of snippets) {
      expect(snippet[1]).toContain('Input:');
      expect(snippet[1]).toContain('Output:');
      expect(snippet[1]).not.toContain('Explanation');
    }
    expect(html).toContain('<strong>Explanation:</strong>');
  });

  it('renders authored inline and display math and legacy powers without consuming currency or code', () => {
    const html = render('Price $5 or $10; literal "$easy$". Powers 10^3 and 10^12. $$x_{i+1}$$.\n\n$$\nx^{2} + 10^{3}\n$$\n\n`10^3` and `$$x_i$$`\n\n```text\nInput: ["$easy$", "10^3"]\n```');
    expect(html).toContain('Price $5 or $10; literal &quot;$easy$&quot;.');
    expect(html).toContain('class="katex-display"');
    expect(html).toContain('<msub>');
    expect(html.match(/<msup>/g)).toHaveLength(4);
    expect(html).toContain('<code>10^3</code>');
    expect(html).toContain('<code>$$x_i$$</code>');
    expect(html).toContain('Input: [&quot;$easy$&quot;, &quot;10^3&quot;]');
    expect(html).not.toContain('katex-error');
  });
});
