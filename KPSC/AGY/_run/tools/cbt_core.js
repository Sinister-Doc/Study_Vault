// cbt_core.js - Pure scoring, timing, and state logic for KPSC CBT Simulator
(function(exports) {
  'use strict';

  /**
   * Pure evaluation function:
   * @param {Object} answers - Map of { [questionId]: { selectedOptionId: string, status: string } }
   * @param {Array} questions - Array of question objects from bank
   * @param {Array} sections - Array of section definitions
   * @param {Object} markingScheme - { positiveMarks: 2.0, negativePenalty: 0.5 }
   * @returns {Object} Comprehensive evaluation metrics
   */
  function scoreExam(answers, questions, sections, markingScheme) {
    const posMark = (markingScheme && markingScheme.positiveMarks !== undefined) ? markingScheme.positiveMarks : 2.0;
    const negPenalty = (markingScheme && markingScheme.negativePenalty !== undefined) ? markingScheme.negativePenalty : 0.5;

    let totalQuestions = questions.length;
    let correctCount = 0;
    let incorrectCount = 0;
    let unattemptedCount = 0;
    let markedCount = 0;

    // Per-section tracking
    const sectionMap = {};
    if (sections && sections.length > 0) {
      sections.forEach(s => {
        sectionMap[s.id || s.name] = {
          id: s.id || s.name,
          name: s.name,
          total: 0,
          attempted: 0,
          correct: 0,
          incorrect: 0,
          unattempted: 0,
          positiveMarks: 0,
          negativePenalty: 0,
          netMarks: 0,
          accuracy: 0
        };
      });
    }

    // Per-topic tracking
    const topicMap = {};

    questions.forEach(q => {
      const qSectionKey = q.section_id || (q.section ? q.section.id || q.section.name : null);
      let secTracker = qSectionKey && sectionMap[qSectionKey] ? sectionMap[qSectionKey] : null;
      if (!secTracker && sections && sections.length > 0) {
        // Find section containing question
        for (const s of sections) {
          if (s.question_ids && s.question_ids.includes(q.id)) {
            secTracker = sectionMap[s.id || s.name];
            break;
          }
        }
      }

      const subjectKey = q.subject || 'General Studies';
      if (!topicMap[subjectKey]) {
        topicMap[subjectKey] = {
          subject: subjectKey,
          total: 0,
          attempted: 0,
          correct: 0,
          incorrect: 0,
          unattempted: 0,
          netMarks: 0
        };
      }
      const topTracker = topicMap[subjectKey];

      if (secTracker) secTracker.total++;
      topTracker.total++;

      const userAns = answers ? answers[q.id] : null;
      const selectedOptionId = userAns ? userAns.selectedOptionId : null;
      const status = userAns ? userAns.status : 'not-visited';

      if (status === 'marked') {
        markedCount++;
      } else if (status === 'marked-answered') {
        markedCount++;
      }

      // Candidate attempted if an option was selected
      const isAttempted = !!selectedOptionId;

      if (!isAttempted) {
        unattemptedCount++;
        if (secTracker) secTracker.unattempted++;
        topTracker.unattempted++;
      } else {
        // Compare option ID or option label
        const correctOptId = q.answer_id || q.answer;
        const isCorrect = (selectedOptionId === correctOptId || selectedOptionId === q.answer);

        if (isCorrect) {
          correctCount++;
          if (secTracker) {
            secTracker.attempted++;
            secTracker.correct++;
            secTracker.positiveMarks += posMark;
          }
          topTracker.attempted++;
          topTracker.correct++;
          topTracker.netMarks += posMark;
        } else {
          incorrectCount++;
          if (secTracker) {
            secTracker.attempted++;
            secTracker.incorrect++;
            secTracker.negativePenalty += negPenalty;
          }
          topTracker.attempted++;
          topTracker.incorrect++;
          topTracker.netMarks -= negPenalty;
        }
      }
    });

    const attemptedCount = correctCount + incorrectCount;
    const positiveMarks = correctCount * posMark;
    const negativePenalty = incorrectCount * negPenalty;
    const netScore = positiveMarks - negativePenalty; // Exact raw score, NOT clamped to 0
    const accuracy = attemptedCount > 0 ? Number(((correctCount / attemptedCount) * 100).toFixed(2)) : 0;

    // Finalize section metrics
    const sectionBreakdown = Object.values(sectionMap).map(sec => {
      sec.netMarks = Number((sec.positiveMarks - sec.negativePenalty).toFixed(2));
      sec.accuracy = sec.attempted > 0 ? Number(((sec.correct / sec.attempted) * 100).toFixed(2)) : 0;
      return sec;
    });

    // Finalize topic metrics
    const topicBreakdown = Object.values(topicMap).map(top => {
      top.netMarks = Number(top.netMarks.toFixed(2));
      top.accuracy = top.attempted > 0 ? Number(((top.correct / top.attempted) * 100).toFixed(2)) : 0;
      return top;
    });

    return {
      totalQuestions,
      attemptedCount,
      unattemptedCount,
      correctCount,
      incorrectCount,
      markedCount,
      positiveMarks: Number(positiveMarks.toFixed(2)),
      negativePenalty: Number(negativePenalty.toFixed(2)),
      netScore: Number(netScore.toFixed(2)),
      accuracy,
      sectionBreakdown,
      topicBreakdown
    };
  }

  /**
   * Pure wall-clock timer computation:
   * @param {number} endTime - Absolute timestamp in milliseconds
   * @param {number} now - Current timestamp in milliseconds (defaults to Date.now())
   * @returns {Object} { remainingSeconds: number, isExpired: boolean, formatted: string }
   */
  function computeRemainingTime(endTime, now) {
    const current = (now !== undefined) ? now : Date.now();
    const diffMs = endTime - current;
    if (diffMs <= 0) {
      return {
        remainingSeconds: 0,
        isExpired: true,
        formatted: "00:00:00"
      };
    }
    const totalSecs = Math.round(diffMs / 1000);
    const hrs = Math.floor(totalSecs / 3600);
    const mins = Math.floor((totalSecs % 3600) / 60);
    const secs = totalSecs % 60;
    const formatted = `${String(hrs).padStart(2, '0')}:${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    return {
      remainingSeconds: totalSecs,
      isExpired: false,
      formatted
    };
  }

  exports.scoreExam = scoreExam;
  exports.computeRemainingTime = computeRemainingTime;

})(typeof exports !== 'undefined' ? exports : (window.CbtCore = {}));
