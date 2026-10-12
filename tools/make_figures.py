#!/usr/bin/env python3
"""Generate the computed figures used in the book.

Deterministic (fixed seeds). Run from the repo root:
    python3 tools/make_figures.py
Writes PNGs into figures/.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import make_s_curve, make_classification
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, precision_recall_curve, roc_auc_score, average_precision_score
from itertools import combinations

FIG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 140, "font.size": 9, "axes.titlesize": 10})


def figure_dim_reduction():
    X, t = make_s_curve(n_samples=1200, noise=0.05, random_state=0)
    z_pca = PCA(n_components=2, random_state=0).fit_transform(X)
    z_tsne = TSNE(n_components=2, perplexity=30, init="pca",
                  learning_rate="auto", random_state=0).fit_transform(X)

    fig, ax = plt.subplots(1, 3, figsize=(11, 3.4))
    for a, Z, title in [(ax[0], z_pca, "PCA (linear)"),
                        (ax[1], z_tsne, "t-SNE (nonlinear)")]:
        s = a.scatter(Z[:, 0], Z[:, 1], c=t, cmap="viridis", s=5, linewidths=0)
        a.set_title(title)
        a.set_xticks([]); a.set_yticks([])
    fig.colorbar(s, ax=ax[1], fraction=0.046, pad=0.02, label="intrinsic coordinate")

    # distance preservation: original pairwise distances vs embedded distances
    idx = np.random.RandomState(1).choice(len(X), 300, replace=False)
    i, j = np.array(list(combinations(idx, 2))).T
    d_orig = np.linalg.norm(X[i] - X[j], axis=1)
    for Z, name, color in [(z_pca, "PCA", "#1b4965"), (z_tsne, "t-SNE", "#c1666b")]:
        d_emb = np.linalg.norm(Z[i] - Z[j], axis=1)
        r = np.corrcoef(d_orig, d_emb)[0, 1]
        ax[2].scatter(d_orig, d_emb, s=3, alpha=0.3, color=color,
                      label=f"{name} (r = {r:.2f})")
    ax[2].set_xlabel("distance in 3D")
    ax[2].set_ylabel("distance in 2D projection")
    ax[2].set_title("Distance preservation")
    ax[2].legend(loc="upper left", fontsize=8, frameon=False)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "dim-reduction.png"), bbox_inches="tight")
    plt.close(fig)
    print("wrote figures/dim-reduction.png")


def figure_roc_vs_pr():
    X, y = make_classification(n_samples=20000, n_features=20, n_informative=6,
                               n_redundant=2, weights=[0.99, 0.01],
                               flip_y=0.02, class_sep=0.9, random_state=0)
    p = LogisticRegression(max_iter=2000, class_weight=None).fit(X, y).predict_proba(X)[:, 1]
    fpr, tpr, _ = roc_curve(y, p)
    prec, rec, _ = precision_recall_curve(y, p)
    au = roc_auc_score(y, p)
    ap = average_precision_score(y, p)

    fig, ax = plt.subplots(1, 2, figsize=(8.4, 3.5))
    ax[0].plot(fpr, tpr, color="#1b4965", lw=2, label=f"AUROC = {au:.2f}")
    ax[0].plot([0, 1], [0, 1], "--", color="grey", lw=1, label="chance")
    ax[0].set_xlabel("false positive rate"); ax[0].set_ylabel("true positive rate")
    ax[0].set_title("ROC curve"); ax[0].legend(frameon=False, loc="lower right")

    prev = y.mean()
    ax[1].plot(rec, prec, color="#c1666b", lw=2, label=f"AP (AUPRC) = {ap:.2f}")
    ax[1].axhline(prev, ls="--", color="grey", lw=1, label=f"chance = {prev:.2f}")
    ax[1].set_xlabel("recall"); ax[1].set_ylabel("precision")
    ax[1].set_title("Precision–recall curve")
    ax[1].set_ylim(0, 1.02); ax[1].legend(frameon=False, loc="upper right")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "roc-vs-pr.png"), bbox_inches="tight")
    plt.close(fig)
    print("wrote figures/roc-vs-pr.png")


if __name__ == "__main__":
    figure_dim_reduction()
    figure_roc_vs_pr()
