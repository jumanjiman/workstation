if [ -n "$BASH_VERSION" -o -n "$KSH_VERSION" -o -n "$ZSH_VERSION" ]; then
  # alias kcscope but only if it's not aliased yet
  alias kcscope &> /dev/null || alias kcscope="cscope -Rk -p4"
fi
