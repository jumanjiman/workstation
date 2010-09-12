if [ -n "$BASH_VERSION" -o -n "$KSH_VERSION" -o -n "$ZSH_VERSION" ]; then
  # alias c but only if it's not aliased yet
  alias c &> /dev/null || alias c="clear"
fi
