/* Pure parser for LeetCode problem descriptions.
 *
 * LeetCode descriptions are plain text strings with a consistent but
 * slightly irregular structure. This module identifies the sections and
 * returns a structured object. No HTML is generated here — the caller
 * is responsible for escaping and rendering.
 *
 * Observed format (from problem JSON files):
 *
 *   <statement prose, possibly containing inline bullet-like lists>
 *   \u00a0                         ← non-breaking space used as visual divider
 *   Example 1:
 *
 *   Input: ...
 *   Output: ...
 *   Explanation: ...               ← optional; may span multiple lines
 *
 *   Example 2:
 *   ...
 *   \u00a0
 *   Constraints:
 *
 *   <constraint line>
 *   <constraint line>
 *   \u00a0
 *   Follow-up: ...                 ← optional; also "Follow up:" (no hyphen)
 */

// Matches "Example 1:", "Example 2:", etc. at the start of a trimmed line.
const EXAMPLE_HEADER = /^Example\s+(\d+)\s*:/i;

// Matches the Constraints section header.
const CONSTRAINTS_HEADER = /^Constraints\s*:/i;

// Matches the Follow-up header. LeetCode uses both "Follow-up:" and "Follow up:".
const FOLLOWUP_HEADER = /^Follow[\s-]up\s*:?\s*/i;

// Matches a labelled field inside an example block.
const EXAMPLE_FIELD = /^(Input|Output|Explanation)\s*:\s*/i;

// The non-breaking space character LeetCode emits as a section divider.
const NBSP = '\u00a0';

/**
 * Normalises a section's extracted text by stripping trailing whitespace
 * and the \u00a0 separator characters LeetCode appends between sections.
 *
 * @param {string} text
 * @returns {string}
 */
function clean(text) {
    return text.replace(/[\u00a0\s]+$/, '').trim();
}

/**
 * Splits a raw description into lines, converting any line that consists
 * solely of \u00a0 into an empty string so that section-boundary detection
 * works uniformly throughout the parser.
 *
 * @param {string} rawText
 * @returns {string[]}
 */
function toLines(rawText) {
    return rawText.replace(/\r\n/g, '\n').split('\n').map(line =>
        line === NBSP ? '' : line
    );
}

/**
 * Parses the content of a single Example block.
 *
 * Fields (Input / Output / Explanation) are labelled lines; subsequent
 * non-blank lines are treated as continuation of the last field, which
 * handles multi-line explanations like numbered sub-steps. A blank line
 * between fields terminates the active field so continuation doesn't
 * accidentally bleed into the next field.
 *
 * @param {number} number  - The example number extracted from the header.
 * @param {string[]} lines - Lines belonging to this block (header excluded).
 * @returns {{ number: number, input: string, output: string, explanation: string|null }}
 */
function parseExampleBlock(number, lines) {
    let input = '';
    let output = '';
    let explanation = null;
    // Track which field is currently being accumulated for continuation lines.
    let currentField = null;

    for (const line of lines) {
        const fieldMatch = line.match(EXAMPLE_FIELD);
        if (fieldMatch) {
            // Start of a labelled field; the rest of this line is its value.
            currentField = fieldMatch[1].toLowerCase();
            const value = line.slice(fieldMatch[0].length);
            if (currentField === 'input') {
                input = value;
            } else if (currentField === 'output') {
                output = value;
            } else {
                // 'explanation'
                explanation = value;
            }
        } else if (currentField !== null) {
            if (line.trim() === '') {
                // A blank line between fields ends the current field's scope
                // so that only genuinely adjacent lines are joined.
                currentField = null;
            } else {
                // Continuation line: append with a newline to preserve structure
                // (e.g. the numbered sub-steps in climbing-stairs explanations).
                if (currentField === 'input') {
                    input += '\n' + line;
                } else if (currentField === 'output') {
                    output += '\n' + line;
                } else {
                    explanation = (explanation ?? '') + '\n' + line;
                }
            }
        }
        // Lines before the first labelled field (blank lines, image
        // placeholder text, etc.) are intentionally ignored.
    }

    return {
        number,
        input: clean(input),
        output: clean(output),
        explanation: explanation !== null ? clean(explanation) : null,
    };
}

/**
 * Parses the Constraints block.
 *
 * Each non-blank line after the "Constraints:" header is one constraint.
 * Leading blank lines (which appear between the header and the first
 * constraint in most problems) are skipped. Collection stops at the first
 * blank line that occurs *after* at least one constraint has been found,
 * which marks the section separator before Follow-up (or end of text).
 *
 * @param {string[]} lines - Lines after the "Constraints:" header.
 * @returns {string[]}
 */
function parseConstraints(lines) {
    const constraints = [];
    for (const line of lines) {
        const trimmed = line.trim();
        if (trimmed === '') {
            // Stop only once we have started collecting — leading blank
            // lines between the header and first constraint are skipped.
            if (constraints.length > 0) break;
        } else {
            constraints.push(trimmed);
        }
    }
    return constraints;
}

/**
 * Scans the line array and returns an ordered list of section boundary
 * markers. Each marker records the section type and the index of its
 * header line so that adjacent markers define slice ranges.
 *
 * @param {string[]} lines
 * @returns {Array<{ type: string, lineIndex: number, number?: number }>}
 */
function findSectionBoundaries(lines) {
    const boundaries = [];
    for (let i = 0; i < lines.length; i++) {
        const trimmed = lines[i].trim();
        const exampleMatch = trimmed.match(EXAMPLE_HEADER);
        if (exampleMatch) {
            boundaries.push({ type: 'example', lineIndex: i, number: parseInt(exampleMatch[1], 10) });
        } else if (CONSTRAINTS_HEADER.test(trimmed)) {
            boundaries.push({ type: 'constraints', lineIndex: i });
        } else if (FOLLOWUP_HEADER.test(trimmed)) {
            boundaries.push({ type: 'followup', lineIndex: i });
        }
    }
    return boundaries;
}

/**
 * Parses a raw LeetCode problem description string into a structured object.
 *
 * Returns a plain object — no HTML, no DOM manipulation. Strings are raw text
 * that the caller must escape before injecting into HTML.
 *
 * @param {string} rawText - The plain-text description from the problem JSON.
 * @returns {{
 *   statement: string,
 *   examples: Array<{ number: number, input: string, output: string, explanation: string|null }>,
 *   constraints: string[],
 *   followUp: string|null
 * }}
 */
export function parseDescription(rawText) {
    if (!rawText || typeof rawText !== 'string') {
        return { statement: '', examples: [], constraints: [], followUp: null };
    }

    const lines = toLines(rawText);
    const boundaries = findSectionBoundaries(lines);

    // Everything before the first recognised section header is the statement.
    // If there are no headers (plain prose only), the whole text is the statement.
    const firstBoundaryLine = boundaries.length > 0 ? boundaries[0].lineIndex : lines.length;
    const statement = clean(lines.slice(0, firstBoundaryLine).join('\n'));

    const examples = [];
    let constraints = [];
    let followUp = null;

    for (let b = 0; b < boundaries.length; b++) {
        const current = boundaries[b];
        // Lines for this section span from just after its header to the line
        // before the next boundary header (exclusive).
        const nextBoundaryLine = b + 1 < boundaries.length
            ? boundaries[b + 1].lineIndex
            : lines.length;
        const sectionLines = lines.slice(current.lineIndex + 1, nextBoundaryLine);

        if (current.type === 'example') {
            examples.push(parseExampleBlock(current.number, sectionLines));
        } else if (current.type === 'constraints') {
            constraints = parseConstraints(sectionLines);
        } else if (current.type === 'followup') {
            // The follow-up text may be inline on the same line as the header
            // (e.g. "Follow-up:\u00a0Can you...") or on the next line.
            // Strip the header prefix from the header line and use whatever remains.
            const headerLine = lines[current.lineIndex];
            const inlineText = headerLine.replace(FOLLOWUP_HEADER, '').trim();
            if (inlineText) {
                followUp = clean(inlineText);
            } else {
                // Fall back to the first non-empty line in the section body.
                const firstContent = sectionLines.find(l => l.trim() !== '');
                followUp = firstContent ? clean(firstContent) : null;
            }
        }
    }

    return { statement, examples, constraints, followUp };
}

// ---------------------------------------------------------------------------
// Test cases
//
// Call runDescriptionParserTests() from the browser console or a Node script
// (with --experimental-vm-modules) to exercise the parser against known inputs.
//
// Example:
//   import { parseDescription, runDescriptionParserTests } from './descriptionParser.js';
//   runDescriptionParserTests();
// ---------------------------------------------------------------------------

export function runDescriptionParserTests() {
    let passed = 0;
    let failed = 0;

    function assert(label, condition) {
        if (condition) {
            console.log(`  PASS  ${label}`);
            passed++;
        } else {
            console.error(`  FAIL  ${label}`);
            failed++;
        }
    }

    // ------------------------------------------------------------------
    // Test 1: Two-Sum-like description.
    // Exercises: statement, three examples (first has explanation, second
    // and third do not), four constraints, follow-up with inline text after
    // the header and a trailing \u00a0.
    // ------------------------------------------------------------------
    {
        const raw = 'Given an array of integers nums\u00a0and an integer target, return indices of the two numbers such that they add up to target.\nYou may assume that each input would have exactly one solution, and you may not use the same element twice.\nYou can return the answer in any order.\n\u00a0\nExample 1:\n\nInput: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].\n\nExample 2:\n\nInput: nums = [3,2,4], target = 6\nOutput: [1,2]\n\nExample 3:\n\nInput: nums = [3,3], target = 6\nOutput: [0,1]\n\n\u00a0\nConstraints:\n\n2 <= nums.length <= 104\n-109 <= nums[i] <= 109\n-109 <= target <= 109\nOnly one valid answer exists.\n\n\u00a0\nFollow-up:\u00a0Can you come up with an algorithm that is less than O(n2)\u00a0time complexity?';

        const r = parseDescription(raw);

        assert('two-sum: statement is non-empty', r.statement.length > 0);
        assert('two-sum: statement does not include "Example"', !r.statement.includes('Example'));
        assert('two-sum: three examples', r.examples.length === 3);
        assert('two-sum: example 1 number', r.examples[0].number === 1);
        assert('two-sum: example 1 input', r.examples[0].input === 'nums = [2,7,11,15], target = 9');
        assert('two-sum: example 1 output', r.examples[0].output === '[0,1]');
        assert('two-sum: example 1 has explanation', r.examples[0].explanation !== null);
        assert('two-sum: example 1 explanation content', r.examples[0].explanation?.includes('nums[0] + nums[1]'));
        assert('two-sum: example 2 no explanation', r.examples[1].explanation === null);
        assert('two-sum: example 3 no explanation', r.examples[2].explanation === null);
        assert('two-sum: four constraints', r.constraints.length === 4);
        assert('two-sum: follow-up present', r.followUp !== null);
        // Follow-up text should start with the actual question, not "Follow-up:"
        assert('two-sum: follow-up stripped of header', !r.followUp?.startsWith('Follow'));
        assert('two-sum: follow-up content', r.followUp?.includes('O(n'));
    }

    // ------------------------------------------------------------------
    // Test 2: Multi-line explanation (climbing-stairs).
    // Exercises: explanation continuation lines that form a numbered list.
    // ------------------------------------------------------------------
    {
        const raw = 'You are climbing a staircase. It takes n steps to reach the top.\nEach time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?\n\u00a0\nExample 1:\n\nInput: n = 2\nOutput: 2\nExplanation: There are two ways to climb to the top.\n1. 1 step + 1 step\n2. 2 steps\n\nExample 2:\n\nInput: n = 3\nOutput: 3\nExplanation: There are three ways to climb to the top.\n1. 1 step + 1 step + 1 step\n2. 1 step + 2 steps\n3. 2 steps + 1 step\n\n\u00a0\nConstraints:\n\n1 <= n <= 45\n\n';

        const r = parseDescription(raw);

        assert('climbing-stairs: two examples', r.examples.length === 2);
        assert('climbing-stairs: example 1 explanation starts correctly', r.examples[0].explanation?.startsWith('There are two ways'));
        // Numbered continuation lines should be present in the explanation.
        assert('climbing-stairs: explanation contains continuation lines', r.examples[0].explanation?.includes('1. 1 step'));
        assert('climbing-stairs: explanation contains second continuation line', r.examples[0].explanation?.includes('2. 2 steps'));
        assert('climbing-stairs: one constraint', r.constraints.length === 1);
        assert('climbing-stairs: constraint value', r.constraints[0] === '1 <= n <= 45');
        assert('climbing-stairs: no follow-up', r.followUp === null);
    }

    // ------------------------------------------------------------------
    // Test 3: Missing explanation in examples + statement contains a
    //         bullet-like list (valid-parentheses style).
    // ------------------------------------------------------------------
    {
        const raw = "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.\nAn input string is valid if:\n\nOpen brackets must be closed by the same type of brackets.\nOpen brackets must be closed in the correct order.\nEvery close bracket has a corresponding open bracket of the same type.\n\n\u00a0\nExample 1:\n\nInput: s = \"()\"\nOutput: true\n\nExample 2:\n\nInput: s = \"()[]{}\"\nOutput: true\n\nExample 3:\n\nInput: s = \"(]\"\nOutput: false\n\n\u00a0\nConstraints:\n\n1 <= s.length <= 104\ns consists of parentheses only '()[]{}'.\n\n";

        const r = parseDescription(raw);

        // The statement includes the intro sentence and the validity conditions.
        assert('valid-parens: statement includes validity conditions', r.statement.includes('Open brackets'));
        assert('valid-parens: statement does not begin with Example', !r.statement.trim().startsWith('Example'));
        assert('valid-parens: three examples', r.examples.length === 3);
        assert('valid-parens: all examples lack explanation', r.examples.every(e => e.explanation === null));
        assert('valid-parens: example 1 input', r.examples[0].input === 's = "()"');
        assert('valid-parens: example 2 output', r.examples[1].output === 'true');
        assert('valid-parens: two constraints', r.constraints.length === 2);
        assert('valid-parens: no follow-up', r.followUp === null);
    }

    // ------------------------------------------------------------------
    // Test 4: "Follow up:" variant (no hyphen) at the end of the description.
    // ------------------------------------------------------------------
    {
        const raw = 'Given the head of a singly linked list, reverse the list, and return the reversed list.\n\u00a0\nExample 1:\n\nInput: head = [1,2,3,4,5]\nOutput: [5,4,3,2,1]\n\n\u00a0\nConstraints:\n\nThe number of nodes in the list is the range [0, 5000].\n-5000 <= Node.val <= 5000\n\n\u00a0\nFollow up: A linked list can be reversed either iteratively or recursively. Could you implement both?\n';

        const r = parseDescription(raw);

        assert('reverse-list: follow-up parsed', r.followUp !== null);
        assert('reverse-list: follow-up starts with content', r.followUp?.startsWith('A linked list'));
        assert('reverse-list: two constraints', r.constraints.length === 2);
        assert('reverse-list: one example', r.examples.length === 1);
    }

    // ------------------------------------------------------------------
    // Test 5: No examples, no constraints — plain prose only.
    // ------------------------------------------------------------------
    {
        const raw = 'Just a plain statement with no examples or constraints.';
        const r = parseDescription(raw);

        assert('plain-prose: statement equals full text', r.statement === raw);
        assert('plain-prose: no examples', r.examples.length === 0);
        assert('plain-prose: no constraints', r.constraints.length === 0);
        assert('plain-prose: no follow-up', r.followUp === null);
    }

    // ------------------------------------------------------------------
    // Test 6: Null and empty input guard.
    // ------------------------------------------------------------------
    {
        const nullResult = parseDescription(null);
        assert('null input: empty statement', nullResult.statement === '');
        assert('null input: no examples', nullResult.examples.length === 0);
        assert('null input: no constraints', nullResult.constraints.length === 0);
        assert('null input: null follow-up', nullResult.followUp === null);

        const emptyResult = parseDescription('');
        assert('empty string: empty statement', emptyResult.statement === '');
        assert('empty string: no examples', emptyResult.examples.length === 0);
    }

    console.log(`\nDescription parser: ${passed} passed, ${failed} failed`);
    return { passed, failed };
}
