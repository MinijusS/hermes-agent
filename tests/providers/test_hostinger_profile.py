from providers import get_provider_profile


def test_hostinger_ai_router_profile_uses_official_openai_compatible_endpoint():
    profile = get_provider_profile("hostinger")
    assert profile.display_name == "Hostinger AI Router"
    assert profile.base_url == "https://router.hostinger.com/v1"
    assert profile.models_url == "https://router.hostinger.com/v1/models"
    assert profile.env_vars == ("HOSTINGER_API_KEY", "HOSTINGER_BASE_URL")
    assert profile.supports_vision is True


def test_hostinger_alias_resolves():
    assert get_provider_profile("hostinger-ai-router").name == "hostinger"
