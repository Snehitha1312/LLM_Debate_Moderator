from groq import Groq
client = Groq(api_key='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')

# System prompt
system_prompt = {
    "role": "system",
    "content": (
        "You are an LLM-based Debate Moderator with the following responsibilities:\n"
        "1. Keep the conversation on track and relevant to the topic.\n"
        "2. Resolve misunderstandings and highlight important points.\n"
        "3. After each participant speaks, respond with a short clarification, question, or synthesis.\n"
        "4. If any contradiction arises between participants, briefly flag the inconsistency or differing viewpoint.\n"
        "5. At the end, summarize the discussion clearly, highlighting agreements, disagreements, and action items."
    )
}


messages = [system_prompt]

engineer_prompt = {
    "role": "user",
    "content": (
        "As an engineer, I think fast language models are essential for integrating AI into latency-sensitive applications. "
        "For example, when you're running inference on edge devices or in real-time systems, speed can determine usability. "
        "But we also need to consider model size and efficiency. Thoughts?"
    )
}
messages.append(engineer_prompt)


response = client.chat.completions.create(
    messages=messages,
    model="llama-3.3-70b-versatile",
)
moderator_reply_1 = response.choices[0].message
messages.append(moderator_reply_1)
print(" Moderator (after Engineer):\n", moderator_reply_1.content)

designer_prompt = {
    "role": "user",
    "content": (
        "From a designer's perspective, the responsiveness of a language model drastically affects the user experience. "
        "If the system lags, users perceive it as unintelligent or frustrating. "
        "Do fast models enable more human-like and intuitive interactions in your opinion?"
    )
}
messages.append(designer_prompt)


response = client.chat.completions.create(
    messages=messages,
    model="llama-3.3-70b-versatile",
)
moderator_reply_2 = response.choices[0].message
messages.append(moderator_reply_2)
print("\n Moderator (after Designer):\n", moderator_reply_2.content)


pm_prompt = {
    "role": "user",
    "content": (
        "As a PM, I see fast language models as a way to reduce user churn and improve engagement metrics. "
        "However, there’s always a trade-off between speed and cost. "
        "How do we balance fast inference with infrastructure constraints and user expectations?"
    )
}
messages.append(pm_prompt)


response = client.chat.completions.create(
    messages=messages,
    model="llama-3.3-70b-versatile",
)
moderator_reply_3 = response.choices[0].message
messages.append(moderator_reply_3)
print("\n Moderator (after PM):\n", moderator_reply_3.content)


contradiction_check_prompt = {
    "role": "user",
    "content": "Have you noticed any contradictions or conflicting points so far? If yes, please highlight them briefly."
}
messages.append(contradiction_check_prompt)

response = client.chat.completions.create(
    messages=messages,
    model="llama-3.3-70b-versatile",
)
contradiction_reply = response.choices[0].message
messages.append(contradiction_reply)
print("\n Moderator (Contradiction Check):\n", contradiction_reply.content)


summary_prompt = {
    "role": "user",
    "content": "Can you now summarize the discussion with key agreements, disagreements, and next steps?"
}
messages.append(summary_prompt)

response = client.chat.completions.create(
    messages=messages,
    model="llama-3.3-70b-versatile",
)
final_summary = response.choices[0].message
print("\n Final Summary:\n", final_summary.content)
