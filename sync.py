#!/usr/bin/env python3

import subprocess
import sys
from datetime import datetime
from pathlib import Path

# ─────────────────────────────────────────
# Config
# ─────────────────────────────────────────
STRATEGIES = {
    "1": ("Safe mode (manual conflict resolution)", []),
    "2": ("Local wins (override remote on conflicts)", ["-X", "theirs"]),
    "3": ("Remote wins (override local on conflicts)", ["-X", "ours"]),
}

# ─────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────
def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    """Run a shell command and return the result."""
    return subprocess.run(cmd, check=check, text=True, capture_output=True)


def git(*args, check: bool = True) -> subprocess.CompletedProcess:
    """Shorthand for running git commands."""
    return run(["git", *args], check=check)


def current_branch() -> str:
    return git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()


def has_staged_changes() -> bool:
    return git("diff", "--cached", "--quiet", check=False).returncode != 0


def prompt_strategy() -> tuple[str, list[str]]:
    print("\nSelect sync strategy:")
    for key, (label, _) in STRATEGIES.items():
        print(f"  {key}) {label}")

    while True:
        choice = input("\nEnter choice [1-3]: ").strip()
        if choice in STRATEGIES:
            return STRATEGIES[choice]
        print("  Invalid choice. Please enter 1, 2, or 3.")


# ─────────────────────────────────────────
# Core steps
# ─────────────────────────────────────────
def fetch_remote() -> None:
    print("\n→ Fetching remote updates...")
    git("fetch", "origin")


def stage_and_commit() -> None:
    print("→ Staging local changes...")
    git("add", ".")

    if not has_staged_changes():
        print("  No local changes to commit.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"auto-sync commit at {timestamp}"
    git("commit", "-m", commit_msg)
    print(f"  Committed: {commit_msg}")


def rebase(branch: str, extra_flags: list[str]) -> None:
    print(f"→ Rebasing onto origin/{branch}...")
    try:
        git("rebase", *extra_flags, f"origin/{branch}")
    except subprocess.CalledProcessError:
        print("\n✖ Rebase conflict detected.")
        print("  Resolve conflicts manually, then run:")
        print("    git rebase --continue")
        print("  Or abort with:")
        print("    git rebase --abort")
        sys.exit(1)


def push(branch: str) -> None:
    print(f"→ Pushing to origin/{branch}...")
    git("push", "origin", branch)


# ─────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────
def main() -> None:
    # Move to repo root
    repo_root = Path(__file__).resolve().parent
    import os
    os.chdir(repo_root)

    label, extra_flags = prompt_strategy()
    print(f"\nStrategy: {label}")

    branch = current_branch()
    print(f"Branch:   {branch}")

    fetch_remote()
    stage_and_commit()
    rebase(branch, extra_flags)
    push(branch)

    print("\n✔ Sync completed successfully.")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"\n✖ Git command failed:\n  {e.stderr.strip()}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nAborted by user.")
        sys.exit(0)