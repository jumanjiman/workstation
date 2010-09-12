# sar display preferences
if [ -n "$BASH_VERSION" -o -n "$KSH_VERSION" -o -n "$ZSH_VERSION" ]; then
  # alias sar but only if it's not aliased yet
  alias sar &> /dev/null || alias sar="LANG=C sar"
fi
