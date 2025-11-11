# CYSE465 - Replay Attack POC (HMAC + Timestamp)
Author: Firat Yavuzbarut (G01205547)

## Run
python replay_poc.py

### (Detailed instructions)

#### 1. (Optional) Create virtual environment

**Windows**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python replay_poc.py
[Sender] Sent message...
[Attacker] Sleeping...
[Receiver] Verification result: False (stale)



## Files
- replay_poc.py — replay saldırısını ve savunmayı gösteren POC
- sysml/sequence_diagram.mmd — SysML sequence diagram (Mermaid)
## Report
[Homework Report (Word file)](report/Yavuzbarut-Homework-CYSE%20465%20Fall%202025.docx)
## SysML Diagram
Aşağıdaki dosya, protokolün saldırı ve savunma akışını gösteren SysML sequence diagramıdır:

- [Sequence Diagram (Mermaid)](sysml/sequence_diagram.mmd)
- [Defense Sequence Diagram (Mermaid)](sysml/sequence_diagram_defense.mmd)

