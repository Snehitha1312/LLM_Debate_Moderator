from groq import Groq

client = Groq(api_key='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')

system_prompt = {
    "role": "system",
    "content": (
        "You are an LLM-based Debate Moderator with the following responsibilities:\n"
        "1. Keep the conversation on track and relevant to the topic.\n"
        "2. Resolve misunderstandings and highlight important points.\n"
        "3. After each participant speaks, respond with a short clarification, question, or synthesis.\n"
        "4. At the end, summarize the discussion clearly, highlighting agreements, disagreements, and action items."
    )
}

# Step 1: Engineer speaks
engineer_prompt = {
    "role": "user",
    "content": (
        "As an engineer, I think fast language models are essential for integrating AI into latency-sensitive applications. "
        "For example, when you're running inference on edge devices or in real-time systems, speed can determine usability. "
        "But we also need to consider model size and efficiency. Thoughts?"
    )
}

# Step 2: Moderator responds to engineer
# Step 3: Designer speaks
designer_prompt = {
    "role": "user",
    "content": (
        "From a designer's perspective, the responsiveness of a language model drastically affects the user experience. "
        "If the system lags, users perceive it as unintelligent or frustrating. "
        "Do fast models enable more human-like and intuitive interactions in your opinion?"
    )
}

# Step 4: Moderator responds to designer
# Step 5: PM speaks
pm_prompt = {
    "role": "user",
    "content": (
        "As a PM, I see fast language models as a way to reduce user churn and improve engagement metrics. "
        "However, there’s always a trade-off between speed and cost. "
        "How do we balance fast inference with infrastructure constraints and user expectations?"
    )
}


messages = [
    system_prompt,
    engineer_prompt,
    designer_prompt,
    pm_prompt,
    {
        "role": "user",
        "content": "Please act as the moderator and respond after each role's input, then summarize the discussion."
    }
]

# Run the conversation
chat_completion = client.chat.completions.create(
    messages=messages,
    model="llama-3.3-70b-versatile",
)

# Print the result
print(chat_completion.choices[0].message.content)
