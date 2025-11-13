"""Application configuration using Pydantic Settings"""
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )

    # Redis Configuration
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0
    redis_password: Optional[str] = None

    # MongoDB Configuration
    mongodb_host: str = "localhost"
    mongodb_port: int = 27017
    mongodb_username: str = "admin"
    mongodb_password: str = "password123"
    mongodb_database: str = "ai_trading"
    mongodb_auth_source: str = "admin"

    # MongoDB Connection Pool & Timeout Settings
    mongodb_min_pool_size: int = 10
    mongodb_max_pool_size: int = 100
    mongodb_timeout_ms: int = 5000
    mongodb_max_idle_time_ms: int = 45000

    # API Configuration
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_reload: bool = True
    api_version: str = "v1"

    # CoinGecko Configuration
    coingecko_api_key: Optional[str] = None
    coingecko_base_url: str = "https://api.coingecko.com/api/v3"

    # Alternative.me Configuration (Fear & Greed Index)
    alternative_base_url: str = "https://api.alternative.me"
    fear_greed_default_limit: int = 30

    # Cache Configuration (seconds)
    cache_ttl: int = 300
    market_data_refresh_interval: int = 600
    fear_greed_refresh_interval: int = 3600  # 1 hour

    # SotaDex Exchange Configuration
    sotadex_base_url: Optional[str] = None
    sotadex_email_1: Optional[str] = None
    sotadex_password_1: Optional[str] = None
    sotadex_email_2: Optional[str] = None
    sotadex_password_2: Optional[str] = None
    sotadex_client_id: Optional[str] = None
    sotadex_client_secret: Optional[str] = None

    # Default exchange selection: binance | sotadex
    default_exchange: str = "binance"

    # Binance Exchange Configuration
    binance_api_key: Optional[str] = None
    binance_api_secret: Optional[str] = None
    binance_testnet: bool = True

    # Auto Trading Configuration
    auto_trading_enabled: bool = False
    auto_trading_interval: int = 300  # 5 minutes

    # AI Auto Trading Configuration
    ai_auto_trading_enabled: bool = False
    ai_auto_trading_interval: int = 600  # 10 minutes

    # AI Service Configuration
    ai_service_url: str = "https://resolve-township-contacts-heart.trycloudflare.com/recommendation"

    # Application
    app_name: str = "AI Trading Platform"
    app_version: str = "0.1.0"
    debug: bool = True


# Global settings instance
settings = Settings()
