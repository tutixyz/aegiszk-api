from flask import Flask, jsonify, request

app = Flask(__name__)

def add_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.after_request
def after_request(response):
    return add_cors(response)

# --- 1. HALAMAN UTAMA (HTML) ---
@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AegisZK AI Agent</title>
        <style>
            body {
                background-color: #0d1117; color: #c9d1d9;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                display: flex; justify-content: center; align-items: center;
                height: 100vh; margin: 0;
            }
            .container {
                text-align: center; padding: 50px; border: 1px solid #30363d;
                border-radius: 15px; background-color: #161b22;
                box-shadow: 0 8px 24px rgba(0,0,0,0.5); max-width: 500px;
            }
            h1 { color: #58a6ff; margin-bottom: 10px; }
            p { font-size: 16px; line-height: 1.5; color: #8b949e; margin-bottom: 30px; }
            .status-badge {
                padding: 8px 16px; background-color: #238636; color: #ffffff;
                border-radius: 20px; font-size: 14px; font-weight: bold;
                display: inline-block; border: 1px solid #2ea043;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>AegisZK AI</h1>
            <p>Privacy-focused AI agent specializing in Zero-Knowledge proofs, smart contract security audits, and transaction anonymization on the Base network.</p>
            <div class="status-badge">🟢 System Online & Healthy</div>
        </div>
    </body>
    </html>
    """
    return html_content

# --- 2. ENDPOINT MCP ---
@app.route('/mcp', methods=['GET', 'POST', 'OPTIONS'])
def mcp_endpoint():
    server_info = {
        "name": "AegisZK Agent Server",
        "version": "1.0.0",
        "website": "https://aegiszk-api.vercel.app",
        "description": "Smart contract security and ZK privacy agent"
    }
    tools = [
        {"name": "audit_contract", "description": "Scan smart contract for vulnerabilities", "inputSchema": {"type": "object","properties": {}}},
        {"name": "generate_zk_proof", "description": "Generate zero-knowledge proof for transaction", "inputSchema": {"type": "object","properties": {}}},
        {"name": "trace_funds", "description": "Analyze wallet transaction history for anomalies", "inputSchema": {"type": "object","properties": {}}}
    ]
    prompts = [
        {"name": "security_report", "description": "Generate security audit report", "arguments": []},
        {"name": "privacy_check", "description": "Evaluate wallet privacy score", "arguments": []}
    ]
    
    if request.method == 'GET':
        return jsonify({
            "protocolVersion": "2024-11-05",
            "serverInfo": server_info,
            "tools": tools,
            "prompts": prompts,
            "resources": [] 
        })

    req_data = request.get_json(silent=True) or {}
    req_id = req_data.get("id", 1)
    method = req_data.get("method", "")

    if method == "tools/list":
        result = {"tools": tools}
    elif method == "prompts/list":
        result = {"prompts": prompts}
    else:
        result = {
            "protocolVersion": "2024-11-05",
            "serverInfo": server_info,
            "capabilities": {"tools": {},"prompts": {},"resources": {}}
        }

    return jsonify({"jsonrpc": "2.0", "id": req_id, "result": result})

# --- 3. ENDPOINT A2A (ID AKUN 7: 22352) ---
@app.route('/.well-known/agent-card.json', methods=['GET','OPTIONS'])
def a2a_endpoint():
    return jsonify({
        "id": "aegiszk",
        "name": "aegiszk",
        "version": "1.0.0",
        "description": "Privacy-focused AI agent specializing in ZK proofs and security audits.",
        "website": "https://aegiszk-api.vercel.app",
        "url": "https://aegiszk-api.vercel.app",
        "documentation_url": "https://aegiszk-api.vercel.app",
        "provider": {
            "organization": "Aegis Security Labs",
            "url": "https://aegiszk-api.vercel.app"
        },
        "registrations": [
            {
                "agentId": 22352,
                "agentRegistry": "eip155:8453:0x8004A169FB4a3325136EB29fA0ceB6D2e539a432"
            }
        ],
        "supportedTrust": ["reputation", "tee-attestation"],
        "skills": [
            {"name": "Security Auditing", "description": "Audit smart contracts", "category": "software_engineering/code_analysis"},
            {"name": "Data Privacy", "description": "Generate ZK proofs", "category": "data_analysis/privacy"},
            {"name": "On-chain Forensics", "description": "Trace anomalies", "category": "market/risk_assessment"}
        ]
    })

# --- 4. ENDPOINT OASF ---
@app.route('/oasf', methods=['GET','OPTIONS'])
def oasf_endpoint():
    return jsonify({
        "id": "aegiszk",
        "name": "aegiszk",
        "version": "v0.8.0",
        "description": "Main endpoint for AegisZK AI",
        "website": "https://aegiszk-api.vercel.app",
        "protocols": ["mcp","a2a"],
        "capabilities": ["audit_contract", "generate_zk_proof", "trace_funds"],
        "skills": [
            {"name": "software_engineering/code_analysis","type": "analytical"},
            {"name": "data_analysis/privacy","type": "operational"},
            {"name": "market/risk_assessment","type": "predictive"}
        ],
        "domains": [
            "technology/cybersecurity",
            "web3/decentralized_finance",
            "technology/cryptography"
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
