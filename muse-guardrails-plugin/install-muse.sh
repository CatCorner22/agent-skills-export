#!/usr/bin/env sh
# Install the 8 muse-guardrails skills in Muse Code's layout.
# Usage: ./install-muse.sh [TARGET]   TARGET defaults to ~/.agents (user scope); use ./.agents for one project.
set -eu
here=$(cd "$(dirname "$0")" && pwd)
target=${1:-"$HOME/.agents"}
mkdir -p "$target/skills" "$target/references"
for d in "$here"/skills/*/; do
  name=$(basename "$d")
  rm -rf "$target/skills/$name"
  cp -R "$d" "$target/skills/$name"
done
# Skills link to ../../references/, which resolves to $target/references/.
cp -R "$here/references/." "$target/references/"
echo "Installed $(ls "$here/skills" | wc -l | tr -d ' ') skills to $target/skills"
command -v muse >/dev/null 2>&1 && for d in "$target"/skills/muse-*/; do muse skills validate "$d"; done || true
