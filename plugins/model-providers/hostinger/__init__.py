"""Hostinger AI Router provider profile."""

from providers import register_provider
from providers.base import ProviderProfile


hostinger = ProviderProfile(
    name="hostinger",
    aliases=("hostinger-ai-router",),
    display_name="Hostinger AI Router",
    description="Hostinger AI Router — OpenAI-compatible multi-model routing",
    signup_url="https://hpanel.hostinger.com/ai-router",
    env_vars=("HOSTINGER_API_KEY", "HOSTINGER_BASE_URL"),
    base_url="https://router.hostinger.com/v1",
    models_url="https://router.hostinger.com/v1/models",
    auth_type="api_key",
    supports_vision=True,
    supports_prompt_cache_key=False,
)

register_provider(hostinger)
