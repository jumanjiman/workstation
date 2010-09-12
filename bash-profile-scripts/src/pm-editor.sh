if [ -n "$BASH_VERSION" -o -n "$KSH_VERSION" -o -n "$ZSH_VERSION" ]; then
  # use vim wherever possible
  test -n "$EDITOR" || export EDITOR="vim"
fi
