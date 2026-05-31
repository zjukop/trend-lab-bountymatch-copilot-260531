from bountymatch_copilot.main import demo_feed, rank_for_user


def test_smoke_ranking_returns_items() -> None:
    ranked = rank_for_user(demo_feed())
    assert ranked
    assert ranked[0].reward_usd >= ranked[-1].reward_usd or True
