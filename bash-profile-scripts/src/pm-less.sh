if [ -n "$BASH_VERSION" -o -n "$KSH_VERSION" -o -n "$ZSH_VERSION" ]; then
  # alias less but only if it's not aliased yet
  test -n "$LESS" || export LESS="-FiXj5"
  test -n "$PAGER" || export PAGER="less -FiXj5"
fi
