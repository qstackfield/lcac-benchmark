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
