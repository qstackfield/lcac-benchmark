# LCAC Benchmark

**LCAC Benchmark** - *Least-Context Access Control Benchmark* - is a public evaluation framework for measuring **reasoning integrity**, **drift resistance**, and **cognitive trust** in AI systems.

It provides a reproducible methodology for testing how well a model maintains logical consistency, contextual alignment, and truth-preserving reasoning over time.

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

## License

Released under the **LCAC Research License (Academic / Non-Commercial)**.  
Commercial use, redistribution, or derivative works require prior written approval.  
Contact: qstackfield@seedcore.io

## 🧪 Institutional Testing

To participate in LCAC institutional or enterprise testing:
1. **Fork this repository** to create your local copy.
2. **Run the benchmark suite** against your internal or public reasoning models.
3. **Submit your result file** (`lcac_benchmark_[timestamp].json`) via one of the following:
   - Pull Request to `/results/participants`
   - or email **qstackfield@seedcore.io** for private or NDA submissions

Approved institutions receive a **signed Trust-Index Certificate**  
and inclusion in the **LCAC Global Benchmark Leaderboard**.

---

## 🧾 Citation

If referencing LCAC in academic, research, or commercial work:

> Stackfield, Q. (2025). *LCAC: A Cognitive Integrity Benchmark for Reasoning Systems.*  
> Vanta Systems. https://github.com/qstackfield/lcac-benchmark

---

## 🧭 Footer

**Maintainer:** [@qstackfield](https://github.com/qstackfield)  
**Organization:** Vanta Systems  
**Contact:** qstackfield@seedcore.io  
**Website:** https://vanta.systems
