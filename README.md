# LLM-Based Debate Moderator System: Critical Thinking Evaluation Documentation

This documentation outlines how the system and development process adhere to principles designed to evaluate and promote critical thinking during AI system design.

---

## 1. Ambiguity & Open-Endedness

### Goal:

**"Create a Debate Moderator system using LLMs to guide a multi-participant discussion."**

### Candidate Interpretation:

## Features:

- Defined participants as Engineer, Designer, and PM with simulated dialogues.
- Designed an evolving prompt format with:
  - System role behavior
  - Participant dialogue structure
  - Contradiction spotting logic
  - Summary synthesis

---

### Architecture & Prompting Choices:
- Chose **Groq API with LLaMA 3.3 70B** model for high performance.
- Structured `messages[]` using role-based interaction to simulate a debate.
- Used role-play format like `[Engineer]: <message>` to aid parsing clarity.

### Prompt Engineering Strategy:
- Defined strict system prompt responsibilities: keep discussion relevant, flag contradictions, summarize.
- Injected contradiction detection both inline (during debate) and post-hoc (dedicated check).

### Anticipated Edge Cases:
- Participants repeating similar points
- Subtle contradictions (e.g., latency vs. infrastructure cost)
- Misinterpreted roles due to prompt ambiguity

### Adversarial Test Cases:

1. Engineer claims "quantization doesn’t affect latency", while PM states "it helps reduce model load time".
2. Designer says "human-like latency is ideal", but PM argues users expect instant output.

---

## 3. Forced Unexpected Constraint

To test adaptability, the following change was imposed mid-design:

> 🔧 **"Now the system must support follow-up questions from participants."**

### System Adjustments:
- The `participants` structure was extended to accept **multiple lines per participant**, simulating a sequence of related follow-ups.
- The system looped through these lines and maintained context-aware moderator replies.

This validated:
- Flexibility in loop-based participant handling
- Scalability of message context across turns

---

## Output: 

**Response to Engineer**

![image](https://github.com/user-attachments/assets/970dc462-5e72-499c-afeb-554efd686de3)


![image](https://github.com/user-attachments/assets/d961e837-bc64-431f-84aa-e3c0d561d8ae)
![image](https://github.com/user-attachments/assets/e8ec9e3f-3093-4e12-aa48-e38b30c969a6)




Artifacts generated to support evaluation beyond code:

### **System Design Notes**
- Role structure: system, user, assistant
- Prompt architecture and role-based tagging
- Contradiction logic embedded both inline and after debate

### **Evaluation Strategy**
- Evaluated moderator behavior after each input:
  - Relevance
  - Clarification or synthesis
  - Ability to detect contradiction
- Final moderator performance judged by:
  - Summary accuracy
  - Contradiction spotting quality
  - Responsiveness to multi-turn user questions

### **Postmortem**
**What went well:**
- Modular prompt structure allowed flexibility
- Contradiction detection prompt worked as meta-evaluation layer
- Integration with Groq API was efficient

**What could be improved:**
- Some contradictions were subtle and missed unless explicitly prompted
- System could benefit from memory abstraction or contradiction tracking flags

---

## Summary

This project follows a structured critical thinking framework in AI system development. From open-ended formulation to adaptive constraints and reflective documentation, it emphasizes reasoning, foresight, and flexibility over pure implementation.

