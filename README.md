ESHA Gatekeeper 🔒

Lightweight Hybrid AI Dispatcher for Local + Cloud Systems

ESHA Gatekeeper is an intelligent orchestration layer designed to bridge the gap between local edge computing and high-performance cloud AI. It acts as a traffic controller, deciding in real-time where a request should be processed based on complexity, cost, and connectivity.

🚀 The Core Philosophy

"Don't run everything everywhere."

Modern AI applications suffer from high latency/cost in the cloud or limited reliability on the edge. ESHA Gatekeeper solves this via a Decision-First Architecture.

* Normalize: Standardizing raw input JSON/Text.  
* Detect: Regex + Weighted keyword intent scoring.  
* Score: Ranking task complexity vs. available compute.  
* Route: Dispatching to the optimal execution layer.  
* Fallback: Auto-migrate to local backup if cloud APIs fail.

🏗️ Architecture
'''text
User Input → [ Gatekeeper Logic ] → [ Decision Engine ]  
                                            ↓  
                    ┌───────────────────────┴───────────────────────┐  
                    ↓                                               ↓  
            [ Path A: LOCAL ]                               [ Path B: CLOUD ]  
            Llama-3 / Whisper                               GPT-4 / Claude  
                    ↓                                               ↓  
                    └───────────────────────┬───────────────────────┘  
                                            ↓  
                                    [ Final Output ]

🛠️ Local Setup

Execute the following commands in your terminal to initialize the environment:

# 1. Clone the repository  
git clone [https://github.com/esha-hub/esha-gatekeeper.git](https://github.com/esha-hub/esha-gatekeeper.git)  
cd esha-gatekeeper

# 2. Setup Virtual Environment  
python -m venv venv  
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install Dependencies  
pip install -r requirements.txt

# 4. Configure Environment  
cp .env.example .env

⚡ Execution Feel

Start the dispatcher and monitor real-time routing:

uvicorn main:app --host 0.0.0.0 --port 8080

Terminal Output:

INFO:     Started server process [4412]  
INFO:     Waiting for application startup.  
INFO:     ESHA Gatekeeper: Local engine (Ollama) detected on 127.0.0.1:11434  
INFO:     ESHA Gatekeeper: Cloud API connectivity... OK.  
INFO:     Uvicorn running on [http://0.0.0.0:8080](http://0.0.0.0:8080) (Press CTRL+C to quit)

Testing the Health Endpoint:

curl http://127.0.0.1:8080/health (http://0.0.0.0:8080/health)

JSON Response:

{  
  "status": "healthy",  
  "routing\_mode": "hybrid",  
  "local\_engine": "connected",  
  "cloud\_api": "verified",  
  "uptime": "14h 22m"  
}

📂 Project Structure

esha-gatekeeper/  
├── main.py              # Application entry point (FastAPI)  
├── Dockerfile           # Multi-stage container config  
├── requirements.txt     # Pin-locked dependencies  
├── config/              # Decision thresholds & provider configs  
├── utils/               # Intent detection & weight scoring logic  
├── docs/                # Extended documentation  
└── .env.example         # Template for environment secrets

☁️ Cloud Deployment (GCP)

Submit a build to the Google Artifact Registry and deploy to Cloud Run:

# 1. Build and push to Artifact Registry  
gcloud builds submit \ 
  --tag asia-south1-docker.pkg.dev/PROJECT/esha-repo/esha-gatekeeper:latest

# 2. Deploy to Cloud Run  
gcloud run deploy esha-gatekeeper \ 
  --image asia-south1-docker.pkg.dev/PROJECT/esha-repo/esha-gatekeeper:latest \
  --region asia-south1 \ 
  --no-allow-unauthenticated

🔐 Configuration (.env)

| Variable | Required | Description |
| :---- | :---- | :---- |
| API\_KEY | Optional | External API key for Cloud services |
| LOCAL\_URL | Yes | Local engine endpoint (Default: 127.0.0.1:11434) |
| THRESHOLD | No | Complexity score to trigger Cloud (0.0 to 1.0) |

[!IMPORTANT] Security Note: Never commit .env files to version control. Use a Secret Manager for production deployments.

🛣️ Roadmap

* [ ] **AWS Planner**: Multi-region resource planning.  
* [ ] **Polyglot Routing**: Support for multi-language intent detection.  
* [ ] **AI4Bharat**: Specific routing for Indian language models.  
* [ ] **Native .gguf Support**: Direct loading of weights without sidecar engines.

📜 License

Custom ESHA License. See LICENSE for details.

This is the foundation for resilient hybrid AI systems. Built by ESHA Hub🚀
