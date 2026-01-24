import json
import os
import platform as py_platform
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def main() -> None:
    out_dir = Path(os.getenv("ARTIFACT_DIR", "platform/model_artifacts/local"))
    out_dir.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(7)
    rows = 500
    x1 = rng.normal(0.0, 1.0, rows)
    x2 = rng.normal(0.0, 1.0, rows)
    x3 = rng.normal(0.0, 1.0, rows)

    df = pd.DataFrame({"x1": x1, "x2": x2, "x3": x3})
    y = ((df["x1"] + 0.6 * df["x2"] - 0.2 * df["x3"]) > 0.0).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        df, y, test_size=0.2, random_state=7, stratify=y
    )

    model = LogisticRegression(max_iter=300)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = float(accuracy_score(y_test, preds))

    model_path = out_dir / "model.joblib"
    joblib.dump(model, model_path)

    metrics = {
        "accuracy": acc,
        "rows": int(rows),
        "generated_at_utc": utc_now_iso(),
    }

    metadata = {
        "artifact_name": "mlops-platform-aws",
        "artifact_version": datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S"),
        "model_type": "LogisticRegression",
        "schema": {"x1": "float", "x2": "float", "x3": "float"},
        "python": py_platform.python_version(),
        "generated_at_utc": utc_now_iso(),
        "files": {
            "model": str(model_path.as_posix()),
            "metrics": str((out_dir / "metrics.json").as_posix()),
            "metadata": str((out_dir / "metadata.json").as_posix()),
        },
    }

    (out_dir / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    (out_dir / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    print(f"Artifact directory: {out_dir}")
    print(f"Model: {model_path}")
    print(f"Accuracy: {acc:.4f}")


if __name__ == "__main__":
    main()
