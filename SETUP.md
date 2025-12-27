# WhatsApp RAG Bot - Setup Guide

## ✅ Quick Start (5 minutes)

### 1. Prerequisites
- Python 3.11+
- - Docker & Docker Compose
  - - OpenAI API key OR Anthropic API key
    - - Wassenger API key
     
      - ### 2. Clone & Setup
      - ```bash
        git clone https://github.com/nbhola01/whatsapp-rag-bot.git
        cd whatsapp-rag-bot
        cp .env.example .env
        ```

        ### 3. Configure .env
        Edit `.env` and add your API keys:
        ```env
        WASSENGER_API_KEY=your_key_here
        OPENAI_API_KEY=sk-...
        # OR
        ANTHROPIC_API_KEY=sk-ant-...
        ```

        ### 4. Start Services
        ```bash
        docker-compose up
        ```

        The bot will be running at: `http://localhost:5000`

        ## 📋 Configuration

        ### Required Environment Variables
        - `WASSENGER_API_KEY` - Your Wassenger API key
        - - `OPENAI_API_KEY` - OpenAI API key (or use Anthropic)
          - - `ANTHROPIC_API_KEY` - Anthropic Claude API key (alternative to OpenAI)
           
            - ### Optional Variables
            - - `PORT` - Server port (default: 5000)
              - - `HOST` - Server host (default: 0.0.0.0)
                - - `CHROMA_HOST` - Vector DB host (default: localhost)
                  - - `CHROMA_PORT` - Vector DB port (default: 8000)
                   
                    - ## 🚀 Deployment
                   
                    - ### Local Development
                    - ```bash
                      pip install -r requirements.txt
                      python src/main.py
                      ```

                      ### Docker Deployment
                      ```bash
                      docker-compose up -d
                      ```

                      ### Cloud Deployment (AWS/GCP/Heroku)
                      1. Build Docker image
                      2. 2. Set environment variables in cloud platform
                         3. 3. Deploy container
                            4. 4. Update Wassenger webhook URL
                              
                               5. ## 📚 API Endpoints
                              
                               6. | Endpoint | Method | Purpose |
                               7. |----------|--------|---------|
                               8. | `/webhook` | POST | Receive messages from WhatsApp |
                               9. | `/api/health` | GET | Health check |
                               10. | `/api/query` | POST | Direct RAG query |
                               11. | `/api/ingest` | POST | Ingest data from URL |
                               12. | `/api/stats` | GET | Vector store statistics |
                              
                               13. ## 🔧 Ingesting Data
                              
                               14. ### From Website
                               15. ```bash
                                   curl -X POST http://localhost:5000/api/ingest \
                                     -H "Content-Type: application/json" \
                                     -d '{"url": "https://example.com"}'
                                   ```

                                   The bot will automatically crawl, chunk, embed, and store all content.

                                   ## 📞 Wassenger Setup

                                   1. Sign up at https://wassenger.app
                                   2. 2. Create WhatsApp Business Account
                                      3. 3. Get API key from dashboard
                                         4. 4. Set webhook URL to: `https://your-domain/webhook`
                                           
                                            5. ## ✨ Features
                                           
                                            6. ✅ Real-time message processing
                                            7. ✅ RAG pipeline with semantic search
                                            8. ✅ Vector database (Chroma)
                                            9. ✅ Multiple LLM support (OpenAI, Claude)
                                            10. ✅ Automatic web crawling and indexing
                                            11. ✅ Docker containerization
                                           
                                            12. ## 🐛 Troubleshooting
                                           
                                            13. **Vector DB Connection Error**
                                            14. ```bash
                                                # Ensure Chroma is running
                                                docker-compose logs chroma
                                                ```

                                                **API Key Issues**
                                                - Verify keys in `.env`
                                                - - Restart bot: `docker-compose restart bot`
                                                 
                                                  - **Webhook Not Receiving**
                                                  - - Check firewall
                                                    - - Verify webhook URL in Wassenger
                                                      - - Check bot logs: `docker-compose logs bot`
                                                       
                                                        - ## 📖 Documentation
                                                       
                                                        - See [README.md](README.md) for full documentation.
