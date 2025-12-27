"""
Configuration settings for WhatsApp RAG Bot
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
      """Application settings"""

    # Wassenger
      WASSENGER_API_KEY = os.getenv('WASSENGER_API_KEY', '')
      WASSENGER_WEBHOOK_SECRET = os.getenv('WASSENGER_WEBHOOK_SECRET', '')

    # LLM Providers
      OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
      ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY', '')

    # Vector DB
      VECTOR_DB_TYPE = os.getenv('VECTOR_DB_TYPE', 'chroma')
      CHROMA_HOST = os.getenv('CHROMA_HOST', 'localhost')
      CHROMA_PORT = int(os.getenv('CHROMA_PORT', 8000))

    # Server
      HOST = os.getenv('HOST', '0.0.0.0')
      PORT = int(os.getenv('PORT', 5000))
      DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'

    # Crawler
      CRAWLER_MAX_PAGES = int(os.getenv('CRAWLER_MAX_PAGES', 50))
