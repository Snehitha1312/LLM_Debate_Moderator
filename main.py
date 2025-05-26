from config import DEBATE_TOPIC, DEBATE_ROUNDS
from agents import engineer_response, designer_response, pm_response
from moderator import moderator_intervene
from summarizer import generate_summary

def run_debate():
    history = ""
    print(f"\n🎯 Debate Topic: {DEBATE_TOPIC}\n")

    for round_no in range(1, DEBATE_ROUNDS + 1):
        print(f"--- Round {round_no} ---")

        engineer = engineer_response(DEBATE_TOPIC, history)
        history += f"\nEngineer: {engineer}\n"
        print(f"👷 Engineer:\n{engineer}\n")

        designer = designer_response(DEBATE_TOPIC, history)
        history += f"\nDesigner: {designer}\n"
        print(f"🎨 Designer:\n{designer}\n")

        pm = pm_response(DEBATE_TOPIC, history)
        history += f"\nProduct Manager: {pm}\n"
        print(f"📈 Product Manager:\n{pm}\n")

        mod = moderator_intervene(DEBATE_TOPIC, history)
        history += f"\nModerator: {mod}\n"
        print(f"🧑‍⚖️ Moderator:\n{mod}\n")

    # Final Summary
    print("🧾 Final Summary:\n")
    summary = generate_summary(history)
    print(summary)

if __name__ == "__main__":
    run_debate()
