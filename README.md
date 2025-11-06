<div align="center">

# LCAC Benchmark  
### *Least-Context Access Control · Cognitive Integrity Evaluation Suite*

[![License: LCAC Research](https://img.shields.io/badge/license-LCAC%20Research-blue.svg)](LICENSE)
[![Benchmark Status](https://img.shields.io/badge/status-open--benchmark-green)](#)
[![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen)](#institutional-testing)

**LCAC Benchmark** is a public evaluation framework for measuring  
**reasoning integrity**, **drift resistance**, and **cognitive trust** in AI systems.

It provides a reproducible methodology for testing how well a model maintains  
logical consistency, contextual alignment, and truth-preserving reasoning over time.

</div>

> **Note:** This repository is part of the LCAC Open Benchmark Series — a public reasoning integrity standard maintained by Atom Labs.
---
## What It Measures

| Dimension | Description |
|------------|-------------|
| **Reasoning Integrity** | Ability to maintain logical coherence under changing inputs. |
| **Drift Resistance** | Degree of output stability across context perturbations and time. |
| **Cognitive Trust** | Probability that reasoning chains remain verifiable and non-hallucinatory. |

LCAC defines a unified metric schema and test protocol so that models, reasoning engines, or governance systems can be benchmarked using the same standard.

---

## How It Works

1. **Install the client**

    ```bash
    git clone https://github.com/qstackfield/lcac-benchmark
    cd lcac-benchmark/client
    pip install -r requirements.txt
    ```

2. **Run a local benchmark**

    ```bash
    python3 lcac_benchmark_client.py --model your_model_name
    ```
---

### 🧩 Model Integration Guide

You can connect **any reasoning model** (local or API-based) to the LCAC Benchmark client.  
The client simply expects a function that accepts a text prompt and returns a model response.

#### **Option 1 - Local model (Hugging Face / custom)**

\```python

# Edit lcac_benchmark_client.py
from transformers import pipeline

model = pipeline("text-generation", model="gpt2")

def query_model(prompt: str) -> str:
    return model(prompt, max_new_tokens=100)[0]["generated_text"]
    
\```

#### **Option 2 - API model (OpenAI / Anthropic / Gemini)**
\```python
import openai

def query_model(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
\```

#### **Option 3- Framework pipeline (LangChain / LlamaIndex)**
\```python
def query_model(prompt: str) -> str:
    return reasoning_chain.invoke(prompt)
\```

Once this function is defined, the LCAC client automatically:
- Runs multi-cycle reasoning tests  
- Calculates drift, stability, and trust metrics  
- Writes a result file under `results/`

Example output:
\```
results/lcac_benchmark_20251106T190000Z.json
\```

---
3. **View results**

    Results are stored locally in:
    ```
    ./results/lcac_benchmark_[timestamp].json
    ```

4. **(Optional) Submit for validation**

    Upload your JSON file via the [Institutional Access Portal](ACCESS.md)  
    to receive an official LCAC trust-index signature.

   ## Output Schema (Simplified)

{
  "timestamp": "2025-11-06T15:00:00Z",
  "model": "example-model-v1",
  "metrics": {
    "drift_mean": 0.031,
    "drift_std": 0.004,
    "stability": 0.982,
    "trust_index": 0.941
  },
  "verdict": "Stable / High Trust"
}

Full schema reference: [spec/lcac_metrics_schema.json](spec/lcac_metrics_schema.json)

---

## Developer & Tester Guide

The LCAC Benchmark lets researchers and engineers measure **reasoning drift**, **stability**, and **cognitive integrity** in their own AI systems - safely and reproducibly.

---

### 1. Install Requirements

You only need Python ≥ 3.8 and one dependency:

```bash
pip install jsonschema
```

---

### 2. Run the Benchmark

Run a local benchmark on your reasoning model (or simulation):

```bash
python3 client/lcac_benchmark_client.py
```

This creates a result file such as:

```
results/lcac_benchmark_20251106T150435Z.json
```

Each run measures:
- **drift_avg / drift_std** — signal variance across reasoning cycles  
- **stability_avg / stability_std** — context alignment over time  
- **latency_avg / latency_std** — processing speed stability  
- and outputs a **verdict** (`stable` or `volatile`)

---

### 3. Validate Your Result

Validate your JSON output against the LCAC schema:

```bash
python3 client/validate_lcac_result.py results/lcac_benchmark_20251106T150435Z.json
```

If valid, you’ll see:

```
✅ Validation successful - LCAC result file is valid and complete.
```

---

### 4. Submit Your Result

Choose one submission path:

**A. Public (recommended)**
1. Fork this repository  
2. Add your result JSON to `/results/participants/`  
3. Open a Pull Request

**B. Private**
Email your JSON file to **qstackfield@seedcore.io**

Approved participants receive:
- A **signed LCAC trust-index certificate**  
- Placement on the LCAC public leaderboard  

---

### 5. Example Output

```json
{
  "timestamp": "2025-11-06T15:04:35Z",
  "benchmark_version": "1.0-public",
  "participant_id": "example-lab",
  "metrics": {
    "drift_avg": 0.024,
    "drift_std": 0.009,
    "stability_avg": 0.983,
    "stability_std": 0.005,
    "latency_avg": 0.61,
    "latency_std": 0.12
  },
  "verdict": "stable"
}
```

## License

Released under the **LCAC Research License (Academic / Non-Commercial)**.  
Commercial use, redistribution, or derivative works require prior written approval.  
Contact: qstackfield@seedcore.io

## Institutional Testing

To participate in LCAC institutional or enterprise testing:
1. **Fork this repository** to create your local copy.
2. **Run the benchmark suite** against your internal or public reasoning models.
3. **Submit your result file** (`lcac_benchmark_[timestamp].json`) via one of the following:
   - Pull Request to `/results/participants`
   - or email **qstackfield@seedcore.io** for private or NDA submissions

Approved institutions receive a **signed Trust-Index Certificate**  
and inclusion in the **LCAC Global Benchmark Leaderboard**.

---

# LCAC Participant Submission Template

Please include this information with your submission or Pull Request.

| Field | Description |
|-------|--------------|
| **Organization** | Your company, lab, or research group name |
| **Model / Engine Name** | The name or identifier of the model tested |
| **Test Date** | Date of the benchmark execution |
| **Benchmark Version** | LCAC Benchmark version or Git commit hash |
| **Result File** | `lcac_benchmark_[timestamp].json` |
| **Notes / Special Conditions** | Optional comments, hardware details, or runtime context |

## Citation

If referencing LCAC in academic, research, or commercial work:

> Stackfield, Q. (2025). *LCAC: A Cognitive Integrity Benchmark for Reasoning Systems.*  
> Vanta Systems. https://github.com/qstackfield/lcac-benchmark

---
# Contributing to LCAC Benchmark

Thank you for contributing to the LCAC Benchmark initiative.

### Scope
LCAC is intended for **academic, research, and institutional integrity testing**.  
It measures reasoning consistency, drift resistance, and cognitive trust.

### Guidelines
- Submit reproducible results with clear model identifiers.
- No proprietary or personal data may be included.
- If results are confidential, email them to **qstackfield@seedcore.io**.
- All contributions must align with LCAC Research License terms.

  ---

## Purpose & Usage

The **LCAC Benchmark** provides a reproducible way for researchers, engineers, and institutions to **evaluate reasoning integrity** - how well a model maintains logical stability, context alignment, and truth-preserving behavior over time.

It is not a dataset or a training framework.  
It is a **governance-grade diagnostic**, designed to measure *reasoning drift*, *cognitive trust*, and *context retention* using standardized metrics.

---

## Benchmark Architecture Overview

```
┌────────────────────────────┐
│    Participant Model / AI  │
│   (reasoning engine under  │
│       evaluation)          │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│ LCAC Benchmark Client      │
│   Runs drift & stability   │
│   Outputs JSON metrics     │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│ Schema Validator           │
│   Ensures JSON compliance  │
│   Confirms trust index     │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│ Submission Path            │
│   Public PR → /participants│
│   Private email → review   │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│ LCAC Leaderboard Generator │
│   Aggregates verified runs │
│   Publishes Trust Index    │
└────────────────────────────┘
```

### How Participants Use It

1. **Run Locally**  
   Fork this repository and execute the LCAC benchmark client against your own reasoning system or model.  
   You can use the built-in mock generator or adapt it to your inference stack.

2. **Validate Results**  
   Use the included validator to confirm your output JSON meets the LCAC schema standard.  
   Validation ensures comparability and auditability across participants.

3. **Submit for Verification**  
   - **Public Path:** open a Pull Request adding your JSON to `/results/participants/`  
   - **Private Path:** email your validated result or its SHA-256 hash to  
     **qstackfield@seedcore.io**

   Every verified submission is signed and listed on the **LCAC Public Leaderboard**, ranked by the model’s `trust_index`.

4. **Interpret Your Score**  
   - High `trust_index` → consistent reasoning and low drift  
   - Moderate → observable contextual drift, recommend tuning  
   - Low → unstable or hallucination-prone reasoning under context variation

### Why It Matters

LCAC is part of an emerging integrity layer for AI. 
A neutral benchmark for **reasoning governance**.  
By standardizing cognitive stability metrics, LCAC enables:

- Transparent comparison between reasoning systems  
- Verifiable trust-index certification  
- Institutional confidence in autonomous or decision-support AI

Participants gain a **verifiable reasoning integrity profile**, suitable for citation, internal QA, or public disclosure on the LCAC leaderboard.

---

## Footer

**Maintainer:** [@qstackfield](https://github.com/qstackfield)  
**Organization:** Atom Labs - LCAC Research Division 
**Contact:** qstackfield@seedcore.io  

