if [ -n "$BASH_VERSION" -o -n "$KSH_VERSION" -o -n "$ZSH_VERSION" ]; then
  # alias grep but only if it's not aliased yet
  alias grep &> /dev/null || alias grep="grep --color"
  test -n "$GREP_COLOR" || export GREP_COLOR="32"
  test -n "$GREP_COLORS" || export GREP_COLORS="32"
fi
