#!/usr/bin/env bash
# Symlink the cpp-skills skill directory and its /cpp-skills command shim into OpenCode.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

mkdir -p "$HOME/.config/opencode/skills" "$HOME/.config/opencode/commands"

ln -sfn "$ROOT/cpp-skills" "$HOME/.config/opencode/skills/cpp-skills"
ln -sfn "$ROOT/.opencode/command/cpp-skills.md" "$HOME/.config/opencode/commands/cpp-skills.md"

echo "Linked cpp-skills skill and /cpp-skills command; restart OpenCode to apply."
