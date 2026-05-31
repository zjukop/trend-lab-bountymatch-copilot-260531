from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Bounty:
    title: str
    reward_usd: int
    difficulty: str


def demo_feed() -> list[Bounty]:
    return [
        Bounty("Add OAuth login to OSS dashboard", 300, "medium"),
        Bounty("Fix flaky CI in monorepo", 150, "easy"),
        Bounty("Implement GraphQL subscriptions", 600, "hard"),
    ]


def rank_for_user(feed: list[Bounty], hourly_target: int = 40) -> list[Bounty]:
    # Simple placeholder ranking by reward-to-effort signal.
    order = {"easy": 1, "medium": 2, "hard": 3}
    return sorted(feed, key=lambda b: (b.reward_usd / hourly_target) / order[b.difficulty], reverse=True)


def main() -> None:
    ranked = rank_for_user(demo_feed())
    print("BountyMatch Copilot — top matches")
    for i, b in enumerate(ranked, start=1):
        print(f"{i}. {b.title} | ${b.reward_usd} | {b.difficulty}")


if __name__ == "__main__":
    main()
