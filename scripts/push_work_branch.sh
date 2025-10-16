#!/usr/bin/env bash
set -euo pipefail

branch=${1:-work}

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "This script must be run inside a git repository." >&2
  exit 1
fi

if ! git remote get-url origin >/dev/null 2>&1; then
  echo "Remote 'origin' is not configured. Add it with:\n  git remote add origin <url>" >&2
  exit 1
fi

# Fetch latest refs so we can reuse an existing remote branch if it is present.
git fetch origin --quiet

if git rev-parse --verify "$branch" >/dev/null 2>&1; then
  git checkout "$branch"
elif git show-ref --verify --quiet "refs/remotes/origin/$branch"; then
  git checkout -b "$branch" "origin/$branch"
else
  git checkout -b "$branch"
fi

echo "\nCurrent branch: $(git rev-parse --abbrev-ref HEAD)"

git status --short

if git status --porcelain | grep -qE '^(M|A|D|R|C|\?\?)'; then
  cat <<'MSG'

⚠️  There are uncommitted changes listed above.
    Commit or stash them before pushing so that Git has something to upload.
MSG
  exit 1
fi

set +e
git push -u origin "$branch"
exit_code=$?
set -e

if [ $exit_code -ne 0 ]; then
  echo "\nPush failed. Double-check that you have at least one commit on the branch." >&2
  exit $exit_code
fi

echo "\n✅ Branch '$branch' is now published to origin."
