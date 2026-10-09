import { execFileSync } from 'node:child_process';
import { readdirSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { inflateSync } from 'node:zlib';
import { describe, expect, it } from 'vitest';
import { z } from 'zod';
import { problemSchema, publicProblem, type Problem } from '../server/problems.js';
import { runCode } from '../server/runner.js';
import { decodeJsonValue, jsonValueBytes } from '../server/problem-values.js';

const directory = resolve('problems');
const corpusSchema = problemSchema.omit({ tests: true }).strict().extend({
  tests: z.array(z.object({ input: z.array(z.unknown()), expected: z.unknown() }).strict()).min(1),
});

function load(id: string): Problem {
  const data: unknown = JSON.parse(readFileSync(resolve(directory, `${id}.json`), 'utf8'));
  return { ...problemSchema.strict().parse(data), id };
}

describe('repaired problem data', () => {
  it('retains every repaired testcase and original Python signature with a valid starter body', () => {
    const files = readdirSync(directory).sort();
    expect(files).toHaveLength(2469);
    let testCount = 0;
    const signatures: Pick<Problem, 'id' | 'starterCode' | 'entryPoint' | 'parameters' | 'returnType'>[] = [];
    for (const file of files) {
      expect(file).toMatch(/^[a-z0-9-]+\.json$/);
      const data: unknown = JSON.parse(readFileSync(resolve(directory, file), 'utf8'));
      const problem = corpusSchema.parse(data);
      for (const test of problem.tests) {
        if (test.input.length !== problem.parameters.length || !('expected' in test)) {
          throw new Error(`Invalid testcase in ${file}`);
        }
      }
      testCount += problem.tests.length;
      signatures.push({ id: file.slice(0, -5), starterCode: problem.starterCode, entryPoint: problem.entryPoint, parameters: problem.parameters, returnType: problem.returnType });
      expect(problem.statement).not.toContain('## TypeScript interface');
    }
    expect(testCount).toBe(1_466_499);
    execFileSync('python3', ['-c', `import ast, json, sys
for problem in json.load(sys.stdin):
    compile(problem['starterCode'], problem['id'], 'exec')
    tree = ast.parse(problem['starterCode'])
    method = next(node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))
    parameters = [{'name': arg.arg, 'type': ast.unparse(arg.annotation)} for arg in method.args.args if arg.arg != 'self']
    assert parameters == problem['parameters'], problem['id']
    assert ast.unparse(method.returns) == problem['returnType'], problem['id']
    assert problem['entryPoint'] == 'Solution().' + method.name, problem['id']
`], { input: JSON.stringify(signatures), encoding: 'utf8' });
  }, 30_000);

  it('preserves cyclic list inputs and original mutation contracts', () => {
    const cycle = load('linked-list-cycle');
    expect(cycle.tests[0]).toEqual({ input: [{ values: [-54], cycle: 0 }], expected: true });
    const acyclic = cycle.tests.find((test) => test.expected === false);
    expect(decodeJsonValue(acyclic?.input[0] ?? null)).toMatchObject({ cycle: -1 });
    expect(publicProblem(cycle).starterCode).toContain('head: Optional[ListNode]');
    expect(publicProblem(cycle).starterCode).toContain('def hasCycle');

    const deduplicate = load('remove-duplicates-from-sorted-array');
    const sample = deduplicate.tests[0];
    const input = z.array(z.number()).parse(decodeJsonValue(sample?.input[0] ?? null));
    const unique = [...new Set(input)];
    expect(decodeJsonValue(sample?.expected ?? null)).toEqual([unique.length, unique]);
    expect(deduplicate.returnType).toBe('int');
    expect(deduplicate.adapter).toBe('prefix');

    const middle = load('middle-of-the-linked-list');
    const list = z.array(z.number()).parse(decodeJsonValue(middle.tests[0]?.input[0] ?? null));
    expect(decodeJsonValue(middle.tests[0]?.expected ?? null)).toEqual(list.slice(Math.floor(list.length / 2)));
    expect(middle.adapter).toBe('middle-list');
    expect(load('reverse-nodes-in-k-group').adapter).toBe('reuse-list');
    expect(load('convert-bst-to-greater-tree').adapter).toBe('mutated-tree');
    expect(load('height-of-special-binary-tree').adapter).toBe('special-tree');
  });

  it('stores exact Python integer products and repaired floating point tolerances', () => {
    const problem = load('product-of-array-except-self');
    expect(problem.returnType).toBe('List[int]');
    const sample = problem.tests[0];
    const values = z.array(z.number().int()).parse(decodeJsonValue(sample?.input[0] ?? null));
    const exact = values.map((_, index) => ({
      $bigint: values.reduce((product, value, other) => other === index ? product : product * BigInt(value), 1n).toString(),
    }));
    expect(decodeJsonValue(sample?.expected ?? null)).toEqual(exact);
    expect(exact.some((value) => BigInt(value.$bigint) > BigInt(Number.MAX_SAFE_INTEGER) || BigInt(value.$bigint) < BigInt(Number.MIN_SAFE_INTEGER))).toBe(true);
    expect(load('powx-n').comparison).toEqual({ absoluteTolerance: 0.000001, relativeTolerance: 0 });
  });

  it('runs original Python submissions against repaired list, tree, mutation, cycle, and large integer cases', async () => {
    const solutions = [
      ['add-two-numbers', `class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l1 or l2 or carry:
            total = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry, digit = divmod(total, 10)
            tail.next = ListNode(digit)
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
`],
      ['same-tree', `class Solution:
    def isSameTree(self, p, q):
        if not p or not q:
            return p is q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
`],
      ['remove-duplicates-from-sorted-array', `class Solution:
    def removeDuplicates(self, nums):
        prefix = sorted(set(nums))
        nums[:len(prefix)] = prefix
        return len(prefix)
`],
      ['product-of-array-except-self', `class Solution:
    def productExceptSelf(self, nums):
        result = [1] * len(nums)
        prefix = suffix = 1
        for index in range(len(nums)):
            result[index] *= prefix
            prefix *= nums[index]
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= suffix
            suffix *= nums[index]
        return result
`],
      ['linked-list-cycle', `class Solution:
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
`],
      ['middle-of-the-linked-list', `class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
`],
      ['convert-bst-to-greater-tree', `class Solution:
    def convertBST(self, root):
        total = 0
        def visit(node):
            nonlocal total
            if node:
                visit(node.right)
                total += node.val
                node.val = total
                visit(node.left)
        visit(root)
        return root
`],
      ['height-of-special-binary-tree', `class Solution:
    def heightOfTree(self, root):
        if root is None:
            return -1
        if root.left and root.left.right is root:
            return 0
        return 1 + max(self.heightOfTree(root.left), self.heightOfTree(root.right))
`],
    ] as const;
    for (const [id, code] of solutions) {
      const problem = load(id);
      const result = await runCode(code, { ...problem, tests: problem.tests.slice(0, 3) });
      expect(result, id).toMatchObject({ passed: 3, total: 3, error: null });
    }
  }, 30_000);

  it('rejects copied list nodes and unchanged input trees even when returned values match', async () => {
    const middle = load('middle-of-the-linked-list');
    const copiedMiddle = await runCode(`class Solution:
    def middleNode(self, head):
        return ListNode(head.val)
`, { ...middle, tests: middle.tests.slice(0, 1) });
    expect(copiedMiddle).toMatchObject({ passed: 0, solved: false });

    const reverse = load('reverse-nodes-in-k-group');
    const relinked = await runCode(`class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        previous = dummy
        while True:
            kth = previous
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next
            following = kth.next
            current = previous.next
            first = current
            tail = following
            while current is not following:
                next_node = current.next
                current.next = tail
                tail = current
                current = next_node
            previous.next = kth
            previous = first
`, reverse);
    expect(relinked).toMatchObject({ passed: reverse.tests.length, solved: true, error: null });
    const copiedReverse = await runCode(`class Solution:
    def reverseKGroup(self, head, k):
        return ListNode(head.val)
`, { ...reverse, tests: reverse.tests.slice(0, 1) });
    expect(copiedReverse).toMatchObject({ passed: 0, solved: false });

    const tree = load('convert-bst-to-greater-tree');
    const copiedTree = await runCode(`class Solution:
    def convertBST(self, root):
        def copy(node):
            return TreeNode(node.val, copy(node.left), copy(node.right)) if node else None
        root = copy(root)
        total = 0
        def visit(node):
            nonlocal total
            if node:
                visit(node.right)
                total += node.val
                node.val = total
                visit(node.left)
        visit(root)
        return root
`, { ...tree, tests: tree.tests.slice(0, 1) });
    expect(copiedTree).toMatchObject({ passed: 0, solved: false });
  });

  it('requires the canonical restored path rather than a permutation or reversal', async () => {
    const original = load('restore-the-array-from-adjacent-pairs');
    const sample = original.tests[0];
    if (!sample) throw new Error('Missing restored-path testcase');
    const expected = z.array(z.number()).parse(decodeJsonValue(sample.expected));
    const problem = { ...original, tests: [sample] };
    expect(original.comparison).toBeUndefined();
    const correct = await runCode(`class Solution:\n    def restoreArray(self, adjacentPairs):\n        return ${JSON.stringify(expected)}\n`, problem);
    expect(correct).toMatchObject({ passed: 1, solved: true });
    const reversed = await runCode(`class Solution:\n    def restoreArray(self, adjacentPairs):\n        return ${JSON.stringify([...expected].reverse())}\n`, problem);
    expect(reversed).toMatchObject({ passed: 0, solved: false });
    const shuffled = await runCode(`class Solution:\n    def restoreArray(self, adjacentPairs):\n        return ${JSON.stringify([...expected].sort((left, right) => left - right))}\n`, problem);
    expect(shuffled).toMatchObject({ passed: 0, solved: false });
  });

  it('losslessly stores large repaired outputs as compressed JSON values', () => {
    const problem = load('combinations');
    const sample = [...problem.tests].sort((left, right) => jsonValueBytes(right.expected) - jsonValueBytes(left.expected))[0];
    if (!sample) throw new Error('Missing combinations testcase');
    const tag = z.object({ $json: z.string(), bytes: z.number().int().positive() }).parse(sample.expected);
    const raw = inflateSync(Buffer.from(tag.$json, 'base64'));
    expect(raw.byteLength).toBe(tag.bytes);
    const original: unknown = JSON.parse(raw.toString('utf8'));
    const combinations = z.array(z.array(z.number().int())).parse(decodeJsonValue(sample.expected));
    expect(combinations).toEqual(original);
    const [n, k] = z.tuple([z.number().int(), z.number().int()]).parse(sample.input.map(decodeJsonValue));
    let count = 1;
    for (let index = 1; index <= k; index++) count = count * (n - index + 1) / index;
    expect(combinations).toHaveLength(Math.round(count));
    for (const combination of combinations) {
      if (combination.length !== k || combination.some((value, index) => value < 1 || value > n || (index > 0 && value <= combination[index - 1]!))) {
        throw new Error('Invalid compressed combination');
      }
    }
  });
});
