import { describe, expect, it } from 'vitest';
import { formatSolveTime } from '../frontend/src/formatSolveTime.js';

describe('solve time formatting', () => {
  it.each([
    [0, '0.0 sec'],
    [9.74, '9.7 sec'],
    [9.76, '9.8 sec'],
    [59.949, '59.9 sec'],
    [59.95, '01:00.0'],
    [60, '01:00.0'],
    [125.74, '02:05.7'],
    [3599.949, '59:59.9'],
    [3599.95, '01:00:00.0'],
    [3600, '01:00:00.0'],
    [3725.76, '01:02:05.8'],
  ])('formats %s seconds as %s with tenths and correct clock carries', (seconds, expected) => {
    expect(formatSolveTime(seconds)).toBe(expected);
  });
});
