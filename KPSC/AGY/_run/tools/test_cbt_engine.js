// test_cbt_engine.js - Unit tests for CbtCore pure engine logic
const assert = require('assert');
const { scoreExam, computeRemainingTime } = require('./cbt_core');

console.log("=== Running Comprehensive CBT Engine Unit Tests (Node.js) ===");

// Build synthetic 100-question test set mimicking KPSC Prelims Paper 1
const mockSections = [
  { id: 'SEC-1', name: 'Section 1: Current Events', total: 40 },
  { id: 'SEC-2', name: 'Section 2: Humanities', total: 60 }
];

const mockQuestions = [];
for (let i = 1; i <= 100; i++) {
  const isSec1 = i <= 40;
  mockQuestions.push({
    id: `Q-${String(i).padStart(3, '0')}`,
    text: `Sample Question ${i}`,
    section_id: isSec1 ? 'SEC-1' : 'SEC-2',
    subject: isSec1 ? 'Current Affairs' : (i <= 70 ? 'History' : 'Polity'),
    answer_id: 'opt_b',
    answer: 'B',
    options: [
      { id: 'opt_a', label: 'A', text: 'Opt A' },
      { id: 'opt_b', label: 'B', text: 'Opt B' },
      { id: 'opt_c', label: 'C', text: 'Opt C' },
      { id: 'opt_d', label: 'D', text: 'Opt D' }
    ]
  });
}

const standardMarking = { positiveMarks: 2.0, negativePenalty: 0.5 };

let passedCount = 0;

// TEST 1: ALL CORRECT
{
  const answers = {};
  mockQuestions.forEach(q => {
    answers[q.id] = { selectedOptionId: 'opt_b', status: 'answered' };
  });
  const res = scoreExam(answers, mockQuestions, mockSections, standardMarking);
  assert.strictEqual(res.totalQuestions, 100);
  assert.strictEqual(res.attemptedCount, 100);
  assert.strictEqual(res.correctCount, 100);
  assert.strictEqual(res.incorrectCount, 0);
  assert.strictEqual(res.unattemptedCount, 0);
  assert.strictEqual(res.positiveMarks, 200.0);
  assert.strictEqual(res.negativePenalty, 0.0);
  assert.strictEqual(res.netScore, 200.0);
  assert.strictEqual(res.accuracy, 100.0);
  console.log("  [PASS] Test 1: All Correct -> +200.0 Marks, 100% Accuracy");
  passedCount++;
}

// TEST 2: ALL WRONG (TRUE NEGATIVE SCORE REPORTING)
{
  const answers = {};
  mockQuestions.forEach(q => {
    answers[q.id] = { selectedOptionId: 'opt_c', status: 'answered' }; // wrong option
  });
  const res = scoreExam(answers, mockQuestions, mockSections, standardMarking);
  assert.strictEqual(res.totalQuestions, 100);
  assert.strictEqual(res.attemptedCount, 100);
  assert.strictEqual(res.correctCount, 0);
  assert.strictEqual(res.incorrectCount, 100);
  assert.strictEqual(res.positiveMarks, 0.0);
  assert.strictEqual(res.negativePenalty, 50.0);
  assert.strictEqual(res.netScore, -50.0); // Verifies NO CLAMPING to 0!
  assert.strictEqual(res.accuracy, 0.0);
  console.log("  [PASS] Test 2: All Wrong -> -50.0 Net Score (No 0-clamping verified)");
  passedCount++;
}

// TEST 3: NONE ATTEMPTED
{
  const answers = {};
  const res = scoreExam(answers, mockQuestions, mockSections, standardMarking);
  assert.strictEqual(res.totalQuestions, 100);
  assert.strictEqual(res.attemptedCount, 0);
  assert.strictEqual(res.unattemptedCount, 100);
  assert.strictEqual(res.netScore, 0.0);
  assert.strictEqual(res.accuracy, 0.0);
  console.log("  [PASS] Test 3: None Attempted -> 0.0 Marks, 100 Unattempted");
  passedCount++;
}

// TEST 4: MIXED ATTEMPTS WITH HAND-COMPUTED SCORE
{
  // 60 Correct, 20 Wrong, 20 Unattempted
  // Score = (60 * 2) - (20 * 0.5) = 120 - 10 = +110.0 Marks
  // Accuracy = 60 / 80 = 75.0%
  const answers = {};
  for (let i = 0; i < 60; i++) {
    answers[mockQuestions[i].id] = { selectedOptionId: 'opt_b', status: 'answered' };
  }
  for (let i = 60; i < 80; i++) {
    answers[mockQuestions[i].id] = { selectedOptionId: 'opt_a', status: 'answered' };
  }
  // Questions 80..99 unattempted

  const res = scoreExam(answers, mockQuestions, mockSections, standardMarking);
  assert.strictEqual(res.attemptedCount, 80);
  assert.strictEqual(res.correctCount, 60);
  assert.strictEqual(res.incorrectCount, 20);
  assert.strictEqual(res.unattemptedCount, 20);
  assert.strictEqual(res.positiveMarks, 120.0);
  assert.strictEqual(res.negativePenalty, 10.0);
  assert.strictEqual(res.netScore, 110.0);
  assert.strictEqual(res.accuracy, 75.0);
  console.log("  [PASS] Test 4: Mixed Case (60 C, 20 W, 20 S) -> +110.0 Marks, 75.0% Accuracy");
  passedCount++;
}

// TEST 5: MARKED FOR REVIEW BEHAVIOR
{
  const answers = {
    'Q-001': { selectedOptionId: null, status: 'marked' }, // marked without answer -> unattempted
    'Q-002': { selectedOptionId: 'opt_b', status: 'marked-answered' }, // marked with answer -> correct
    'Q-003': { selectedOptionId: 'opt_c', status: 'marked-answered' } // marked with answer -> wrong
  };
  const threeQs = mockQuestions.slice(0, 3);
  const res = scoreExam(answers, threeQs, mockSections, standardMarking);
  assert.strictEqual(res.attemptedCount, 2);
  assert.strictEqual(res.unattemptedCount, 1);
  assert.strictEqual(res.correctCount, 1);
  assert.strictEqual(res.incorrectCount, 1);
  assert.strictEqual(res.netScore, 1.50); // 2.0 - 0.5 = 1.5
  assert.strictEqual(res.markedCount, 3);
  console.log("  [PASS] Test 5: Marked for Review (Unanswered counts as skipped; Answered evaluated)");
  passedCount++;
}

// TEST 6: SECTIONAL AND THEMATIC BREAKDOWNS
{
  const answers = {};
  // In Section 1 (Q1..Q40): 30 correct, 10 wrong -> Net = (30*2)-(10*0.5) = 60 - 5 = 55.0
  for (let i = 0; i < 30; i++) {
    answers[mockQuestions[i].id] = { selectedOptionId: 'opt_b', status: 'answered' };
  }
  for (let i = 30; i < 40; i++) {
    answers[mockQuestions[i].id] = { selectedOptionId: 'opt_d', status: 'answered' };
  }
  // In Section 2 (Q41..Q100): 40 correct, 10 wrong, 10 skipped -> Net = (40*2)-(10*0.5) = 80 - 5 = 75.0
  for (let i = 40; i < 80; i++) {
    answers[mockQuestions[i].id] = { selectedOptionId: 'opt_b', status: 'answered' };
  }
  for (let i = 80; i < 90; i++) {
    answers[mockQuestions[i].id] = { selectedOptionId: 'opt_a', status: 'answered' };
  }
  const res = scoreExam(answers, mockQuestions, mockSections, standardMarking);
  assert.strictEqual(res.sectionBreakdown.length, 2);
  const s1 = res.sectionBreakdown.find(s => s.id === 'SEC-1');
  const s2 = res.sectionBreakdown.find(s => s.id === 'SEC-2');
  assert.strictEqual(s1.total, 40);
  assert.strictEqual(s1.netMarks, 55.0);
  assert.strictEqual(s2.total, 60);
  assert.strictEqual(s2.netMarks, 75.0);
  assert.strictEqual(res.netScore, 130.0); // 55 + 75 = 130
  console.log("  [PASS] Test 6: Sectional Breakdown Sums Perfectly to Overall Net Score");
  passedCount++;
}

// TEST 7: WALL-CLOCK TIMER DERIVATION
{
  const baseTime = 1000000000;
  const durationMs = 120 * 60 * 1000; // 7200s
  const endTime = baseTime + durationMs;

  // 1. Midway check (after 30 mins = 1800s)
  const tMid = computeRemainingTime(endTime, baseTime + (30 * 60 * 1000));
  assert.strictEqual(tMid.remainingSeconds, 5400); // 90 mins = 5400s
  assert.strictEqual(tMid.isExpired, false);
  assert.strictEqual(tMid.formatted, '01:30:00');

  // 2. Exactly expired
  const tEnd = computeRemainingTime(endTime, endTime);
  assert.strictEqual(tEnd.remainingSeconds, 0);
  assert.strictEqual(tEnd.isExpired, true);

  // 3. Past expired
  const tPast = computeRemainingTime(endTime, endTime + 5000);
  assert.strictEqual(tPast.remainingSeconds, 0);
  assert.strictEqual(tPast.isExpired, true);

  console.log("  [PASS] Test 7: Wall-Clock Timer (Midway, Expired, Auto-Submit Trigger verified)");
  passedCount++;
}

console.log(`\n=== ALL ${passedCount} UNIT TESTS PASSED WITH 100% SUCCESS ===`);
