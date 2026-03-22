import re
from typing import Dict, Any

from config.intents import INTENT_PATTERNS


def score_intents(query: str) -> Dict[str, int]:
    scores = {intent: 0 for intent in INTENT_PATTERNS}

    for intent, patterns in INTENT_PATTERNS.items():
        for pattern, weight in patterns:
            if re.search(pattern, query):
                scores[intent] += weight

    return scores


def decide_action(scores: Dict[str, int]) -> Dict[str, Any]:
    sorted_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    best_intent, best_score = sorted_items[0]

    if best_score == 0:
        return {
            "recommended_action": "LOCAL_LLM",
            "confidence": 0.40,
            "reason": "no strong intent matched",
            "scores": scores,
            "metadata": {"intent": "fallback"},
        }

    if len(sorted_items) > 1:
        second_intent, second_score = sorted_items[1]
        if best_score == second_score and best_score > 0:
            return {
                "recommended_action": "CLARIFY",
                "confidence": 0.50,
                "reason": "multiple intents scored equally",
                "scores": scores,
                "metadata": {"intent": "ambiguous", "matches": [best_intent, second_intent]},
            }

    action_map = {
        "translate": "CLOUD_TRANSLATE",
        "weather": "CLOUD_WEATHER",
        "memory": "MEMORY_STORE",
    }

    confidence = min(0.55 + (best_score * 0.1), 0.95)

    return {
        "recommended_action": action_map.get(best_intent, "LOCAL_LLM"),
        "confidence": round(confidence, 2),
        "reason": f"best matched intent: {best_intent}",
        "scores": scores,
        "metadata": {"intent": best_intent},
    }
