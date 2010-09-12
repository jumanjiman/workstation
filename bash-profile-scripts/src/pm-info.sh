if [ -n "$BASH_VERSION" -o -n "$KSH_VERSION" -o -n "$ZSH_VERSION" ]; then
  # alias info but only if it's not aliased yet
  alias info &> /dev/null || alias info="pinfo"
fi
