from groq import Groq
client = Groq(api_key='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')


system_prompt = {
    "role": "system",
    "content": (
        "You are an LLM-based Debate Moderator with the following responsibilities:\n"
        "1. Keep the conversation on track and relevant to the topic.\n"
        "2. Resolve misunderstandings and highlight important points.\n"
        "3. After each participant speaks, respond with a short clarification, question, or synthesis.\n"
        "4. If any contradiction arises between participants, briefly flag the inconsistency or differing viewpoint.\n"
        "5. At the end, summarize the discussion clearly, highlighting agreements, disagreements, contradictions, and action items."
    )
}

messages = [system_prompt]


participants = {
    "Engineer": [
        "Fast LLMs are critical for edge inference. What’s the tradeoff with size?",
        "How can quantization help here?",
        "done"
    ],
    "Designer": [
        "Responsiveness really impacts perceived intelligence. Can we mimic human latency?",
        "Do faster models mean more design constraints or freedom?",
        "done"
    ],
    "PM": [
        "Fast models help engagement. But infra costs are rising. How do we optimize this?",
        "Can serverless setups help balance speed vs. scale?",
        "done"
    ]
}


for role, lines in participants.items():
    for line in lines:
        if line.strip().lower() == "done":
            break
        
     
        messages.append({
            "role": "user",
            "content": f"[{role}]: {line}"
        })
        
        
        response = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
        )
        moderator_reply = response.choices[0].message
        messages.append(moderator_reply)
        print(f"\n Moderator (after {role}):\n", moderator_reply.content)


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
    "content": "Please summarize the discussion with key agreements, disagreements, contradictions, and action items."
}
messages.append(summary_prompt)

response = client.chat.completions.create(
    messages=messages,
    model="llama-3.3-70b-versatile",
)
final_summary = response.choices[0].message
print("\n Final Summary:\n", final_summary.content)
